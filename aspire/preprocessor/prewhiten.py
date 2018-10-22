""" Prewhiten projections.
    converted (and adjusted) from MATLAB module/function "cryo_prewhiten.m".
"""
from aspire.utils.data_utils import mat_to_npy, mat_to_npy_vec
import numpy as np
import time
import pyfftw
from pyfftw.interfaces.numpy_fft import fft2, ifft2, fftshift, ifftshift


np.random.seed(1137)


def run():
    input_images = mat_to_npy('input_images')
    noise_response, _, _ = cryo_noise_estimation(input_images)
    output_images, _, _ = cryo_prewhiten(input_images, noise_response)
    return output_images


def cryo_noise_estimation(projections, radius_of_mask=None):
    p = projections.shape[0]

    if radius_of_mask is None:
        radius_of_mask = p // 2 - 1

    center_polar_samples = cart2rad(p)
    noise_idx = np.where(center_polar_samples >= radius_of_mask)

    power_spectrum, r, r2, x = cryo_epsds(projections, noise_idx, p // 3)
    power_spectrum = np.real(power_spectrum)

    return power_spectrum, r, r2


def cryo_epsds(imstack, samples_idx, max_d, verbose=None):
    p = imstack.shape[0]
    if max_d >= p:
        max_d = p-1
        print('max_d too large. Setting max_d to {}'.format(max_d))

    r, x, _ = cryo_epsdr(imstack, samples_idx, max_d, verbose)

    r2 = np.zeros((2 * p - 1, 2 * p - 1))
    dsquare = np.square(x)
    for i in range(-max_d, max_d + 1):
        for j in range(-max_d, max_d + 1):
            d = i ** 2 + j ** 2
            if d <= max_d ** 2:
                idx, _ = bsearch(dsquare, d*(1-1e-13), d*(1+1e-13))
                if idx is None:
                    raise Warning('something went wrong in bsearch')
                r2[i+p-1, j+p-1] = r[idx-1]

    w = gwindow(p, max_d)
    p2 = cfft2(r2 * w)
    err = np.linalg.norm(p2.imag) / np.linalg.norm(p2)
    if err > 1e-12:
        raise Warning('Large imaginary components in P2 = {}'.format(err))

    p2 = p2.real

    e = 0
    for i in range(imstack.shape[2]):
        im = imstack[:, :, i]
        e += np.sum(np.square(im[samples_idx] - np.mean(im[samples_idx])))

    mean_e = e / (len(samples_idx[0]) * imstack.shape[2])
    p2 = (p2 / p2.sum()) * mean_e * p2.size
    neg_idx = np.where(p2 < 0)
    if len(neg_idx[0]) != 0:
        max_neg_err = np.max(np.abs(p2[neg_idx]))
        if max_neg_err > 1e-2:
            neg_norm = np.linalg.norm(p2[neg_idx])
            raise Warning('Power specrtum P2 has negative values with energy {}'.format(neg_norm))
        p2[neg_idx] = 0
    return p2, r, r2, x


def gwindow(p, max_d):
    x, y = np.meshgrid(np.arange(-(p-1), p), np.arange(-(p-1), p))
    alpha = 3.0
    w = np.exp(-alpha * (np.square(x) + np.square(y)) / (2 * max_d ** 2))
    return w


def cryo_epsdr(vol, samples_idx, max_d, verbose):
    p = vol.shape[0]
    k = vol.shape[2]
    i, j = np.meshgrid(np.arange(max_d + 1), np.arange(max_d + 1))
    dists = np.square(i) + np.square(j)
    dsquare = np.sort(np.unique(dists[np.where(dists <= max_d ** 2)]))

    corrs = np.zeros(len(dsquare))
    corr_count = np.zeros(len(dsquare))
    x = np.sqrt(dsquare)

    dist_map = np.zeros(dists.shape)
    for i in range(max_d + 1):
        for j in range(max_d + 1):
            d = i ** 2 + j ** 2
            if d <= max_d ** 2:
                idx, _ = bsearch(dsquare, d - 1e-13, d + 1e-13)
                if idx is None:
                    raise Warning('something went wrong in bsearch')
                dist_map[i, j] = idx

    dist_map = dist_map.astype('int') - 1
    valid_dists = np.where(dist_map != -1)

    mask = np.zeros((p, p))
    mask[samples_idx] = 1
    tmp = np.zeros((2 * p + 1, 2 * p + 1))
    tmp[:p, :p] = mask
    ftmp = np.fft.fft2(tmp)
    c = np.fft.ifft2(ftmp * np.conj(ftmp))
    c = c[:max_d+1, :max_d+1]
    c = np.round(c).astype('int')

    r = np.zeros(len(corrs))

    print('Processing projections')

    # optimized version
    vol = vol.transpose((2, 0, 1)).copy()
    input_fft2 = np.zeros((2 * p + 1, 2 * p + 1), dtype='complex128')
    output_fft2 = np.zeros((2 * p + 1, 2 * p + 1), dtype='complex128')
    input_ifft2 = np.zeros((2 * p + 1, 2 * p + 1), dtype='complex128')
    output_ifft2 = np.zeros((2 * p + 1, 2 * p + 1), dtype='complex128')
    flags = ('FFTW_MEASURE', 'FFTW_UNALIGNED')
    fft2 = pyfftw.FFTW(input_fft2, output_fft2, axes=(0, 1), direction='FFTW_FORWARD', flags=flags)
    ifft2 = pyfftw.FFTW(input_ifft2, output_ifft2, axes=(0, 1), direction='FFTW_BACKWARD', flags=flags)
    sum_s = np.zeros(output_ifft2.shape, output_ifft2.dtype)
    sum_c = c * vol.shape[0]
    for i in range(k):
        proj = vol[i]

        input_fft2[samples_idx] = proj[samples_idx]
        fft2()
        np.multiply(output_fft2, np.conj(output_fft2), out=input_ifft2)
        ifft2()
        sum_s += output_ifft2

    for curr_dist in zip(valid_dists[0], valid_dists[1]):
        dmidx = dist_map[curr_dist]
        corrs[dmidx] += sum_s[curr_dist]
        corr_count[dmidx] += sum_c[curr_dist]

    idx = np.where(corr_count != 0)[0]
    r[idx] += corrs[idx] / corr_count[idx]
    cnt = corr_count[idx]

    idx = np.where(corr_count == 0)[0]
    r[idx] = 0
    x[idx] = 0
    return r, x, cnt


def cryo_epsdr_ref(vol, samples_idx, max_d, verbose):
    p = vol.shape[0]
    k = vol.shape[2]
    i, j = np.meshgrid(np.arange(max_d + 1), np.arange(max_d + 1))
    dists = np.square(i) + np.square(j)
    dsquare = np.sort(np.unique(dists[np.where(dists <= max_d ** 2)]))

    corrs = np.zeros(len(dsquare))
    corr_count = np.zeros(len(dsquare))
    x = np.sqrt(dsquare)

    dist_map = np.zeros(dists.shape)
    for i in range(max_d + 1):
        for j in range(max_d + 1):
            d = i ** 2 + j ** 2
            if d <= max_d ** 2:
                idx, _ = bsearch(dsquare, d - 1e-13, d + 1e-13)
                if idx is None:
                    raise Warning('something went wrong in bsearch')
                dist_map[i, j] = idx

    dist_map = dist_map.astype('int') - 1
    valid_dists = np.where(dist_map != -1)

    mask = np.zeros((p, p))
    mask[samples_idx] = 1
    tmp = np.zeros((2 * p + 1, 2 * p + 1))
    tmp[:p, :p] = mask
    ftmp = np.fft.fft2(tmp)
    c = np.fft.ifft2(ftmp * np.conj(ftmp))
    c = c[:max_d+1, :max_d+1]
    c = np.round(c).astype('int')

    r = np.zeros(len(corrs))

    print('Processing projections')

    for i in range(k):
        proj = vol[:, :, i]

        samples = np.zeros((p, p))
        samples[samples_idx] = proj[samples_idx]

        tmp = np.zeros((2 * p + 1, 2 * p + 1))
        tmp[:p, :p] = samples
        ftmp = np.fft.fft2(tmp)
        s = np.fft.ifft2(ftmp * np.conj(ftmp))
        s = s[:max_d+1, :max_d+1]

        for curr_dist in zip(valid_dists[0], valid_dists[1]):
            dmidx = dist_map[curr_dist]
            corrs[dmidx] += s[curr_dist]
            corr_count[dmidx] += c[curr_dist]

    idx = np.where(corr_count != 0)[0]
    r[idx] += corrs[idx] / corr_count[idx]
    cnt = corr_count[idx]

    idx = np.where(corr_count == 0)[0]
    r[idx] = 0
    x[idx] = 0
    return r, x, cnt


def bsearch(x, lower_bound, upper_bound):
    if lower_bound > x[-1] or upper_bound < x[0] or upper_bound < lower_bound:
        return None, None
    lower_idx_a = 1
    lower_idx_b = len(x)
    upper_idx_a = 1
    upper_idx_b = len(x)

    while lower_idx_a + 1 < lower_idx_b or upper_idx_a + 1 < upper_idx_b:
        lw = int(np.floor((lower_idx_a + lower_idx_b) / 2))
        if x[lw-1] >= lower_bound:
            lower_idx_b = lw
        else:
            lower_idx_a = lw
            if upper_idx_a < lw < upper_idx_b:
                upper_idx_a = lw

        up = int(np.ceil((upper_idx_a + upper_idx_b) / 2))
        if x[up-1] <= upper_bound:
            upper_idx_a = up
        else:
            upper_idx_b = up
            if lower_idx_a < up < lower_idx_b:
                lower_idx_b = up

    if x[lower_idx_a-1] >= lower_bound:
        lower_idx = lower_idx_a
    else:
        lower_idx = lower_idx_b
    if x[upper_idx_b-1] <= upper_bound:
        upper_idx = upper_idx_b
    else:
        upper_idx = upper_idx_a

    if upper_idx < lower_idx:
        return None, None

    return lower_idx, upper_idx


def cryo_prewhiten(proj, noise_response, rel_threshold=None):
    """
    Pre-whiten a stack of projections using the power spectrum of the noise.


    :param proj: stack of images/projections
    :param noise_response: 2d image with the power spectrum of the noise. If all
                           images are to be whitened with respect to the same power spectrum,
                           this is a single image. If each image is to be whitened with respect
                           to a different power spectrum, this is a three-dimensional array with
                           the same number of 2d slices as the stack of images.

    :param rel_threshold: The relative threshold used to determine which frequencies
                          to whiten and which to set to zero. If empty (the default)
                          all filter values less than 100*eps(class(proj)) are
                          zeroed out, while otherwise, all filter values less than
                          threshold times the maximum filter value for each filter
                          is set to zero.

    :return: Pre-whitened stack of images.
    """

    delta = np.finfo(proj.dtype).resolution

    resolution, _, num_images = proj.shape
    l = resolution // 2
    k = int(np.ceil(noise_response.shape[0] / 2))

    filter_var = np.sqrt(noise_response)
    filter_var /= np.linalg.norm(filter_var)

    filter_var = (filter_var + np.flipud(filter_var)) / 2
    filter_var = (filter_var + np.fliplr(filter_var)) / 2

    if rel_threshold is None:
        nzidx = np.where(filter_var > 100 * delta)
    else:
        raise NotImplementedError('not implemented for rel_threshold != None')

    start_idx = k - l - 1
    end_idx = k + l
    if resolution % 2 == 0:
        end_idx -= 1

    fnz = filter_var[nzidx]
    one_over_fnz = 1 / fnz
    one_over_fnz_as_mat = np.ones((noise_response.shape[0], noise_response.shape[0]))
    one_over_fnz_as_mat[nzidx] *= one_over_fnz
    pp = np.zeros((noise_response.shape[0], noise_response.shape[0]))
    p2 = np.zeros((num_images, resolution, resolution), dtype='complex128')
    proj = proj.transpose((2, 0, 1)).copy()

    for i in range(num_images):
        pp[start_idx:end_idx, start_idx:end_idx] = proj[i]

        fp = fast_cfft2(pp)
        fp *= one_over_fnz_as_mat
        pp2 = fast_icfft2(fp)

        p2[i] = pp2[start_idx:end_idx, start_idx:end_idx]

    proj = p2.real.transpose((1, 2, 0)).copy()
    return proj, filter_var, nzidx


def cryo_prewhiten_ref(proj, noise_response, rel_threshold=None):
    """
    Pre-whiten a stack of projections using the power spectrum of the noise.


    :param proj: stack of images/projections
    :param noise_response: 2d image with the power spectrum of the noise. If all
                           images are to be whitened with respect to the same power spectrum,
                           this is a single image. If each image is to be whitened with respect
                           to a different power spectrum, this is a three-dimensional array with
                           the same number of 2d slices as the stack of images.

    :param rel_threshold: The relative threshold used to determine which frequencies
                          to whiten and which to set to zero. If empty (the default)
                          all filter values less than 100*eps(class(proj)) are
                          zeroed out, while otherwise, all filter values less than
                          threshold times the maximum filter value for each filter
                          is set to zero.

    :return: Pre-whitened stack of images.
    """

    delta = np.finfo(proj.dtype).resolution

    resolution, _, num_images = proj.shape
    l = resolution // 2
    k = int(np.ceil(noise_response.shape[0] / 2))

    filter_var = np.sqrt(noise_response)
    filter_var /= np.linalg.norm(filter_var)

    filter_var = (filter_var + np.flipud(filter_var)) / 2
    filter_var = (filter_var + np.fliplr(filter_var)) / 2

    if rel_threshold is None:
        nzidx = np.where(filter_var > 100 * delta)
    else:
        raise NotImplementedError('not implemented for rel_threshold != None')

    start_idx = k - l - 1
    end_idx = k + l
    if resolution % 2 == 0:
        end_idx -= 1

    fnz = filter_var[nzidx]
    pp = np.zeros((noise_response.shape[0], noise_response.shape[0]))
    p2 = np.zeros((num_images, resolution, resolution), dtype='complex128')
    proj = proj.transpose((2, 0, 1)).copy()

    for i in range(num_images):
        pp[start_idx:end_idx, start_idx:end_idx] = proj[i]

        fp = cfft2(pp)
        fp[nzidx] /= fnz
        pp2 = icfft2(fp)

        p2[i] = pp2[start_idx:end_idx, start_idx:end_idx]

    proj = p2.real.transpose((1, 2, 0)).copy()
    return proj, filter_var, nzidx


def cfft2(x):
    if len(x.shape) == 2:
        return np.fft.fftshift(np.transpose(np.fft.fft2(np.transpose(np.fft.ifftshift(x)))))
    elif len(x.shape) == 3:
        y = np.fft.ifftshift(x, (1, 2))
        y = np.transpose(y, (0, 2, 1))
        y = np.fft.fft2(y)
        y = np.transpose(y, (0, 2, 1))
        y = np.fft.fftshift(y, (1, 2))
        return y
    else:
        raise ValueError("x must be 2D or 3D")


def icfft2(x):
    if len(x.shape) == 2:
        return np.fft.fftshift(np.transpose(np.fft.ifft2(np.transpose(np.fft.ifftshift(x)))))
    elif len(x.shape) == 3:
        y = np.fft.ifftshift(x, (1, 2))
        y = np.transpose(y, (0, 2, 1))
        y = np.fft.ifft2(y)
        y = np.transpose(y, (0, 2, 1))
        y = np.fft.fftshift(y, (1, 2))
        return y
    else:
        raise ValueError("x must be 2D or 3D")


def fast_cfft2(x):
    if len(x.shape) == 2:
        return fftshift(np.transpose(fft2(np.transpose(ifftshift(x)))))
    elif len(x.shape) == 3:
        y = ifftshift(x, (1, 2))
        y = np.transpose(y, (0, 2, 1))
        y = fft2(y)
        y = np.transpose(y, (0, 2, 1))
        y = fftshift(y, (1, 2))
        return y
    else:
        raise ValueError("x must be 2D or 3D")


def fast_icfft2(x):
    if len(x.shape) == 2:
        return fftshift(np.transpose(ifft2(np.transpose(ifftshift(x)))))
    elif len(x.shape) == 3:
        y = ifftshift(x, (1, 2))
        y = np.transpose(y, (0, 2, 1))
        y = ifft2(y)
        y = np.transpose(y, (0, 2, 1))
        y = fftshift(y, (1, 2))
        return y
    else:
        raise ValueError("x must be 2D or 3D")


def cart2rad(n):
    n = int(np.floor(n))
    p = (n - 1) / 2
    x, y = np.meshgrid(np.arange(-p, p + 1), np.arange(-p, p + 1))
    center_polar_samples = np.sqrt(np.square(x) + np.square(y))
    return center_polar_samples


def comp(a, b):
    return np.linalg.norm(a - b) / np.linalg.norm(a)

run()

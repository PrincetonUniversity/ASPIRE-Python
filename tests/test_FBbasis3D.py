import os.path
from unittest import TestCase

import numpy as np

from aspire.basis.fb_3d import FBBasis3D

DATA_DIR = os.path.join(os.path.dirname(__file__), 'saved_test_data')


class FBBasis3DTestCase(TestCase):
    def setUp(self):
        self.basis = FBBasis3D((8, 8, 8))

    def tearDown(self):
        pass

    def testFBBasis3DIndices(self):
        indices = self.basis.indices()

        self.assertTrue(np.allclose(
            indices['ells'],
            [
                0., 0., 0., 1., 1., 1., 1., 1., 1., 1., 1., 1., 2., 2., 2.,
                2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 3., 3., 3.,
                3., 3., 3., 3., 3., 3., 3., 3., 3., 3., 3., 4., 4., 4., 4.,
                4., 4., 4., 4., 4., 4., 4., 4., 4., 4., 4., 4., 4., 4., 5.,
                5., 5., 5., 5., 5., 5., 5., 5., 5., 5., 6., 6., 6., 6., 6.,
                6., 6., 6., 6., 6., 6., 6., 6., 7., 7., 7., 7., 7., 7., 7.,
                7., 7., 7., 7., 7., 7., 7., 7.
            ]
        ))

        self.assertTrue(np.allclose(
            indices['ms'],
            [
                0., 0., 0., -1., -1., -1., 0., 0., 0., 1., 1., 1., -2., -2., -2.,
                -1., -1., -1., 0., 0., 0., 1., 1., 1., 2., 2., 2., -3., -3., -2.,
                -2., -1., -1., 0., 0., 1., 1., 2., 2., 3., 3., -4., -4., -3., -3.,
                -2., -2., -1., -1., 0., 0., 1., 1., 2., 2., 3., 3., 4., 4., -5.,
                -4., -3., -2., -1., 0., 1., 2., 3., 4., 5., -6., -5., -4., -3., -2.,
                -1., 0., 1., 2., 3., 4., 5., 6., -7., -6., -5., -4., -3., -2., -1.,
                0., 1., 2., 3., 4., 5., 6., 7.
            ]
        ))

        self.assertTrue(np.allclose(
            indices['ks'],
            [
                0., 1., 2., 0., 1., 2., 0., 1., 2., 0., 1., 2., 0., 1., 2., 0., 1., 2., 0.,
                1., 2., 0., 1., 2., 0., 1., 2., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0.,
                1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1.,
                0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
                0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
                0., 0., 0
            ]
        ))

    def testFBBasis3DNorms(self):
        norms = self.basis.norms()
        self.assertTrue(np.allclose(
            norms,
            [
                1.80063263231421, 0.900316316157109, 0.600210877438065, 1.22885897287928, 0.726196138639673,
                0.516613361675378, 0.936477951517100, 0.610605075148750, 0.454495363516488, 0.756963071176142,
                0.527618747123993, 0.635005913075500, 0.464867421846148, 0.546574142892508, 0.479450758110826,
                0.426739123914569
            ]
        ))

    def testFBBasis3DEvaluate(self):
        coeffs = np.array(
              [
                 1.07338590e-01,   1.23690941e-01,   6.44482039e-03,  -5.40484306e-02,
                -4.85304586e-02,   1.09852144e-02,   3.87838396e-02,   3.43796455e-02,
                -6.43284705e-03,  -2.86677145e-02,  -1.42313328e-02,  -2.25684091e-03,
                -3.31840727e-02,  -2.59706174e-03,  -5.91919887e-04,  -9.97433028e-03,
                 9.19123928e-04,   1.19891589e-03,   7.49154982e-03,   6.18865229e-03,
                -8.13265715e-04,  -1.30715655e-02,  -1.44160603e-02,   2.90379956e-03,
                 2.37066082e-02,   4.88805735e-03,   1.47870707e-03,   7.63376018e-03,
                -5.60619559e-03,   1.05165081e-02,   3.30510143e-03,  -3.48652120e-03,
                -4.23228797e-04,   1.40484061e-02,   1.42914291e-03,  -1.28129504e-02,
                 2.19868825e-03,  -6.30835037e-03,   1.18524223e-03,  -2.97855052e-02,
                 1.15491057e-03,  -8.27947006e-03,   3.45442781e-03,  -4.72868856e-03,
                 2.66615329e-03,  -7.87929790e-03,   8.84126590e-04,   1.59402808e-03,
                -9.06854048e-05,  -8.79119004e-03,   1.76449039e-03,  -1.36414673e-02,
                 1.56793855e-03,   1.44708445e-02,  -2.55974802e-03,   5.38506357e-03,
                -3.24188673e-03,   4.81582945e-04,   7.74260101e-05,   5.48772082e-03,
                 1.92058500e-03,  -4.63538896e-03,  -2.02735133e-03,   3.67592386e-03,
                 7.23486969e-04,   1.81838422e-03,   1.78793284e-03,  -8.01474060e-03,
                -8.54007528e-03,   1.96353845e-03,  -2.16254252e-03,  -3.64243996e-05,
                -2.27329863e-03,   1.11424393e-03,  -1.39389189e-03,   2.57787159e-04,
                 3.66918811e-03,   1.31477774e-03,   6.82220128e-04,   1.41822851e-03,
                -1.89476924e-03,  -6.43966255e-05,  -7.87888465e-04,  -6.99459279e-04,
                 1.08918981e-03,   2.25264584e-03,  -1.43651015e-04,   7.68377620e-04,
                 5.05955256e-04,   2.66936132e-06,   2.24934884e-03,   6.70529439e-04,
                 4.81121742e-04,  -6.40789745e-05,  -3.35915672e-04,  -7.98651783e-04,
                -9.82705453e-04,   6.46337066e-05
            ]
        )
        result = self.basis.evaluate(coeffs)

        self.assertTrue(np.allclose(
            result,
            np.load(os.path.join(DATA_DIR, 'hbbasis_evaluation_8_8_8.npy'))
        ))

    def testFBBasis3DEvaluate_t(self):
        v = np.load(os.path.join(DATA_DIR, 'hbbasis_coefficients_8_8_8.npy'))
        result = self.basis.evaluate_t(v)
        self.assertTrue(np.allclose(
            result,
            [
                 1.07338590e-01,   1.23690941e-01,   6.44482039e-03,  -5.40484306e-02,
                -4.85304586e-02,   1.09852144e-02,   3.87838396e-02,   3.43796455e-02,
                -6.43284705e-03,  -2.86677145e-02,  -1.42313328e-02,  -2.25684091e-03,
                -3.31840727e-02,  -2.59706174e-03,  -5.91919887e-04,  -9.97433028e-03,
                 9.19123928e-04,   1.19891589e-03,   7.49154982e-03,   6.18865229e-03,
                -8.13265715e-04,  -1.30715655e-02,  -1.44160603e-02,   2.90379956e-03,
                 2.37066082e-02,   4.88805735e-03,   1.47870707e-03,   7.63376018e-03,
                -5.60619559e-03,   1.05165081e-02,   3.30510143e-03,  -3.48652120e-03,
                -4.23228797e-04,   1.40484061e-02,   1.42914291e-03,  -1.28129504e-02,
                 2.19868825e-03,  -6.30835037e-03,   1.18524223e-03,  -2.97855052e-02,
                 1.15491057e-03,  -8.27947006e-03,   3.45442781e-03,  -4.72868856e-03,
                 2.66615329e-03,  -7.87929790e-03,   8.84126590e-04,   1.59402808e-03,
                -9.06854048e-05,  -8.79119004e-03,   1.76449039e-03,  -1.36414673e-02,
                 1.56793855e-03,   1.44708445e-02,  -2.55974802e-03,   5.38506357e-03,
                -3.24188673e-03,   4.81582945e-04,   7.74260101e-05,   5.48772082e-03,
                 1.92058500e-03,  -4.63538896e-03,  -2.02735133e-03,   3.67592386e-03,
                 7.23486969e-04,   1.81838422e-03,   1.78793284e-03,  -8.01474060e-03,
                -8.54007528e-03,   1.96353845e-03,  -2.16254252e-03,  -3.64243996e-05,
                -2.27329863e-03,   1.11424393e-03,  -1.39389189e-03,   2.57787159e-04,
                 3.66918811e-03,   1.31477774e-03,   6.82220128e-04,   1.41822851e-03,
                -1.89476924e-03,  -6.43966255e-05,  -7.87888465e-04,  -6.99459279e-04,
                 1.08918981e-03,   2.25264584e-03,  -1.43651015e-04,   7.68377620e-04,
                 5.05955256e-04,   2.66936132e-06,   2.24934884e-03,   6.70529439e-04,
                 4.81121742e-04,  -6.40789745e-05,  -3.35915672e-04,  -7.98651783e-04,
                -9.82705453e-04,   6.46337066e-05
            ]
        ))

    def testFBBasis3DExpand(self):
        v = np.load(os.path.join(DATA_DIR, 'hbbasis_coefficients_8_8_8.npy'))
        result = self.basis.expand(v)
        self.assertTrue(np.allclose(
            result,
            [
                +0.10743660, +0.12346847, +0.00684837, -0.05410818, -0.04840195, +0.01071116, +0.03878536, +0.03437083,
                -0.00638332, -0.02865552, -0.01425294, -0.00223313, -0.03317134, -0.00261654, -0.00056954, -0.00997264,
                +0.00091569, +0.00123042, +0.00754713, +0.00606669, -0.00043233, -0.01306626, -0.01443522, +0.00301968,
                +0.02375521, +0.00477979, +0.00166319, +0.00780333, -0.00601982, +0.01052385, +0.00328666, -0.00336805,
                -0.00070688, +0.01409127, +0.00127259, -0.01289172, +0.00234488, -0.00630249, +0.00117541, -0.02974037,
                +0.00108834, -0.00823955, +0.00340772, -0.00471875, +0.00266391, -0.00789639, +0.00093529, +0.00160710,
                -0.00011925, -0.00817443, +0.00046713, -0.01357463, +0.00145920, +0.01452459, -0.00267202, +0.00535952,
                -0.00322100, +0.00092083, -0.00075300, +0.00509418, +0.00193687, -0.00483399, -0.00204537, +0.00338492,
                +0.00111248, +0.00194841, +0.00174416, -0.00814324, -0.00839777, +0.00199974, -0.00196156, -0.00014695,
                -0.00245317, +0.00109957, -0.00146145, +0.00015149, +0.00415232, +0.00121810, +0.00066095, +0.00166167,
                -0.00231911, -0.00025819, -0.00086808, -0.00074656, +0.00110445, +0.00285573, -0.00014959, +0.00093241,
                +0.00051144, +0.00004805, +0.00250166, +0.00059104, +0.00066592, +0.00019188, -0.00079074, -0.00068995,
                -0.00087668, +0.00052913
            ]
        ))

    def testFBBasis3DExpand_t(self):
        v = np.array(
            [
                +0.10743660, +0.12346847, +0.00684837, -0.05410818, -0.04840195, +0.01071116, +0.03878536, +0.03437083,
                -0.00638332, -0.02865552, -0.01425294, -0.00223313, -0.03317134, -0.00261654, -0.00056954, -0.00997264,
                +0.00091569, +0.00123042, +0.00754713, +0.00606669, -0.00043233, -0.01306626, -0.01443522, +0.00301968,
                +0.02375521, +0.00477979, +0.00166319, +0.00780333, -0.00601982, +0.01052385, +0.00328666, -0.00336805,
                -0.00070688, +0.01409127, +0.00127259, -0.01289172, +0.00234488, -0.00630249, +0.00117541, -0.02974037,
                +0.00108834, -0.00823955, +0.00340772, -0.00471875, +0.00266391, -0.00789639, +0.00093529, +0.00160710,
                -0.00011925, -0.00817443, +0.00046713, -0.01357463, +0.00145920, +0.01452459, -0.00267202, +0.00535952,
                -0.00322100, +0.00092083, -0.00075300, +0.00509418, +0.00193687, -0.00483399, -0.00204537, +0.00338492,
                +0.00111248, +0.00194841, +0.00174416, -0.00814324, -0.00839777, +0.00199974, -0.00196156, -0.00014695,
                -0.00245317, +0.00109957, -0.00146145, +0.00015149, +0.00415232, +0.00121810, +0.00066095, +0.00166167,
                -0.00231911, -0.00025819, -0.00086808, -0.00074656, +0.00110445, +0.00285573, -0.00014959, +0.00093241,
                +0.00051144, +0.00004805, +0.00250166, +0.00059104, +0.00066592, +0.00019188, -0.00079074, -0.00068995,
                -0.00087668, +0.00052913
            ]
        )
        result = self.basis.expand_t(v)
        self.assertTrue(np.allclose(
            result[:, :, 4],
            np.array([
                [+0.00000000, +0.00000000, +0.00000000, +0.00000000, -0.00000000, +0.00000000, +0.00000000, +0.00000000],
                [+0.00000000, +0.00000000, -0.00082447, -0.00501736, -0.00540824, -0.00469159, -0.00351230, +0.00000000],
                [+0.00000000, +0.00079290, -0.00438718, -0.00759907, +0.00352330, +0.00934700, +0.00080984, -0.00224754],
                [+0.00000000, -0.00145279, -0.01091470, +0.00208184, +0.03345656, +0.04013643, +0.01804092, -0.00052682],
                [+0.00000000, -0.00531538, -0.01070807, +0.01977898, +0.05884156, +0.05290487, +0.01851250, -0.00244280],
                [+0.00000000, -0.00665870, -0.00839966, +0.02050697, +0.05232750, +0.03999358, +0.00403108, -0.00844911],
                [+0.00000000, -0.00258625, -0.00258453, +0.00966552, +0.01986598, +0.00768192, -0.01180773, -0.00736751],
                [+0.00000000, +0.00000000, +0.00164587, +0.00441885, -0.00045751, -0.00891542, -0.00792309, +0.00000000],
            ])
        ))

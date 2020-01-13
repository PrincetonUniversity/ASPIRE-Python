import numpy as np
from unittest import TestCase

from aspire.utils.blk_diag_func import *


class BlkDiagFuncTestCase(TestCase):
    def setUp(self):
        self.blk_a = [
            np.array([[-0.30656809, -0.34287864, -0.00854488,  0.5275285 ],
                      [-0.34287864, -0.19752432,  0.17833916, -0.22052178],
                      [-0.00854488,  0.17833916, -0.4125285 , -0.30338836],
                      [ 0.5275285 , -0.22052178, -0.30338836,  0.12254553]]),
            np.array([[-0.08041961, -0.29729055, -0.3960436 ],
                      [-0.29729055, -0.56196307,  0.0607334 ],
                      [-0.3960436 ,  0.0607334 , -0.09843568]]),
            np.array([[-0.08041961, -0.29729055, -0.3960436 ],
                      [-0.29729055, -0.56196307,  0.0607334 ],
                      [-0.3960436 ,  0.0607334 , -0.09843568]]),
            np.array([[ 0.04041207, -0.05335218, -0.55965714],
                      [-0.05335218, -0.62303735, -0.26739795],
                      [-0.55965714, -0.26739795,  0.07961834]]),
            np.array([[ 0.04041207, -0.05335218, -0.55965714],
                      [-0.05335218, -0.62303735, -0.26739795],
                      [-0.55965714, -0.26739795,  0.07961834]]),
            np.array([[ 0.05209133,  0.17877923],
                      [ 0.17877923, -0.43246999]]),
            np.array([[ 0.05209133,  0.17877923],
                      [ 0.17877923, -0.43246999]]),
            np.array([[ 0.00296652,  0.32398467],
                      [ 0.32398467, -0.12518209]]),
            np.array([[ 0.00296652,  0.32398467],
                      [ 0.32398467, -0.12518209]]),
            np.array([[-0.06749134,  0.37452234],
                      [ 0.37452234,  0.1789093 ]]),
            np.array([[-0.06749134,  0.37452234],
                      [ 0.37452234,  0.1789093 ]]),
            np.array([[-0.13551364]]), np.array([[-0.13551364]]),
            np.array([[-0.18975111]]), np.array([[-0.18975111]]),
            np.array([[-0.22661312]]), np.array([[-0.22661312]])
        ]

        self.blk_b = [
            np.array([[-0.27457111, -0.33770709, -0.09067737,  0.52007584],
                      [-0.33770709, -0.24677034,  0.20639731, -0.2078888 ],
                      [-0.09067737,  0.20639731, -0.36507922, -0.37742705],
                      [ 0.52007584, -0.2078888 , -0.37742705,  0.30641696]]),
            np.array([[-0.05219921, -0.23403317, -0.46057571],
                      [-0.23403317, -0.58669018,  0.02892691],
                      [-0.46057571,  0.02892691, -0.01291359]]),
            np.array([[-0.05219921, -0.23403317, -0.46057571],
                      [-0.23403317, -0.58669018,  0.02892691],
                      [-0.46057571,  0.02892691, -0.01291359]]),
            np.array([[ 0.04180323,  0.03254542, -0.56899236],
                      [ 0.03254542, -0.5865448 , -0.33459247],
                      [-0.56899236, -0.33459247,  0.23441378]]),
            np.array([[ 0.04180323,  0.03254542, -0.56899236],
                      [ 0.03254542, -0.5865448 , -0.33459247],
                      [-0.56899236, -0.33459247,  0.23441378]]),
            np.array([[ 0.02685116,  0.25494821],
                      [ 0.25494821, -0.33546046]]),
            np.array([[ 0.02685116,  0.25494821],
                      [ 0.25494821, -0.33546046]]),
            np.array([[-0.04041477,  0.36934457],
                      [ 0.36934457,  0.0278976 ]]),
            np.array([[-0.04041477,  0.36934457],
                      [ 0.36934457,  0.0278976 ]]),
            np.array([[-0.11861509,  0.37524325],
                      [ 0.37524325,  0.38311618]]),
            np.array([[-0.11861509,  0.37524325],
                      [ 0.37524325,  0.38311618]]),
            np.array([[-0.18418421]]), np.array([[-0.18418421]]),
            np.array([[-0.22672867]]), np.array([[-0.22672867]]),
            np.array([[-0.24393745]]), np.array([[-0.24393745]])
        ]

        self.blk_partition = blk_diag_partition(self.blk_a)

    def tearDown(self):
        pass

    def testBlkDiagPartition(self):
        result = [(4, 4), (3, 3), (3, 3), (3, 3), (3, 3), (2, 2), (2, 2), (2, 2), (2, 2),
                  (2, 2), (2, 2), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)
                  ]
        blk_partition = blk_diag_partition(self.blk_a)
        self.assertTrue(result, blk_partition)

    def testBlkDiagZeros(self):
        result = [
            np.array([[0., 0., 0., 0.],
                      [0., 0., 0., 0.],
                      [0., 0., 0., 0.],
                      [0., 0., 0., 0.]]),
            np.array([[0., 0., 0.],
                      [0., 0., 0.],
                      [0., 0., 0.]]),
            np.array([[0., 0., 0.],
                      [0., 0., 0.],
                      [0., 0., 0.]]),
            np.array([[0., 0., 0.],
                      [0., 0., 0.],
                      [0., 0., 0.]]),
            np.array([[0., 0., 0.],
                      [0., 0., 0.],
                      [0., 0., 0.]]),
            np.array([[0., 0.],
                      [0., 0.]]),
            np.array([[0., 0.],
                      [0., 0.]]),
            np.array([[0., 0.],
                      [0., 0.]]),
            np.array([[0., 0.],
                      [0., 0.]]),
            np.array([[0., 0.],
                      [0., 0.]]),
            np.array([[0., 0.],
                      [0., 0.]]),
            np.array([[0.]]), np.array([[0.]]),
            np.array([[0.]]), np.array([[0.]]),
            np.array([[0.]]), np.array([[0.]])
        ]
        blk_zeros = blk_diag_zeros(self.blk_partition)
        im = 0
        for mat in result:
            self.assertTrue(np.allclose(mat, blk_zeros[im]))
            im += 1

    def testBlkDiagEye(self):
        result = [
            np.array([[1., 0., 0., 0.],
                      [0., 1., 0., 0.],
                      [0., 0., 1., 0.],
                      [0., 0., 0., 1.]]),
            np.array([[1., 0., 0.],
                      [0., 1., 0.],
                      [0., 0., 1.]]),
            np.array([[1., 0., 0.],
                      [0., 1., 0.],
                      [0., 0., 1.]]),
            np.array([[1., 0., 0.],
                      [0., 1., 0.],
                      [0., 0., 1.]]),
            np.array([[1., 0., 0.],
                      [0., 1., 0.],
                      [0., 0., 1.]]),
            np.array([[1., 0.],
                      [0., 1.]]),
            np.array([[1., 0.],
                      [0., 1.]]),
            np.array([[1., 0.],
                      [0., 1.]]),
            np.array([[1., 0.],
                      [0., 1.]]),
            np.array([[1., 0.],
                      [0., 1.]]),
            np.array([[1., 0.],
                      [0., 1.]]),
            np.array([[1.]]), np.array([[1.]]),
            np.array([[1.]]), np.array([[1.]]),
            np.array([[1.]]), np.array([[1.]])
        ]

        blk_eye = blk_diag_eye(self.blk_partition)
        im = 0
        for mat in result:
            self.assertTrue(np.allclose(mat, blk_eye[im]))
            im += 1

    def testBlkDiagAdd(self):
        result = [
            np.array([[-0.5811392 , -0.68058573, -0.09922225,  1.04760434],
                      [-0.68058573, -0.44429466,  0.38473647, -0.42841058],
                      [-0.09922225,  0.38473647, -0.77760772, -0.68081541],
                      [ 1.04760434, -0.42841058, -0.68081541,  0.42896249]]),
            np.array([[-0.13261882, -0.53132372, -0.85661931],
                      [-0.53132372, -1.14865325,  0.08966031],
                      [-0.85661931,  0.08966031, -0.11134927]]),
            np.array([[-0.13261882, -0.53132372, -0.85661931],
                      [-0.53132372, -1.14865325,  0.08966031],
                      [-0.85661931,  0.08966031, -0.11134927]]),
            np.array([[ 0.0822153 , -0.02080676, -1.1286495 ],
                      [-0.02080676, -1.20958215, -0.60199042],
                      [-1.1286495 , -0.60199042,  0.31403212]]),
            np.array([[ 0.0822153 , -0.02080676, -1.1286495 ],
                      [-0.02080676, -1.20958215, -0.60199042],
                      [-1.1286495 , -0.60199042,  0.31403212]]),
            np.array([[ 0.07894249,  0.43372744],
                      [ 0.43372744, -0.76793045]]),
            np.array([[ 0.07894249,  0.43372744],
                      [ 0.43372744, -0.76793045]]),
            np.array([[-0.03744825,  0.69332924],
                      [ 0.69332924, -0.09728449]]),
            np.array([[-0.03744825,  0.69332924],
                      [ 0.69332924, -0.09728449]]),
            np.array([[-0.18610643,  0.74976559],
                      [ 0.74976559,  0.56202548]]),
            np.array([[-0.18610643,  0.74976559],
                      [ 0.74976559,  0.56202548]]),
            np.array([[-0.31969785]]), np.array([[-0.31969785]]),
            np.array([[-0.41647978]]), np.array([[-0.41647978]]),
            np.array([[-0.47055057]]), np.array([[-0.47055057]])
        ]

        blk_c = blk_diag_add(self.blk_a, self.blk_b)

        im = 0
        for mat in result:
            self.assertTrue(np.allclose(mat, blk_c[im]))
            im += 1

    def testBlkDiagMinus(self):
        result = [
                np.array([[-0.03199698, -0.00517155,  0.08213249,  0.00745266],
                          [-0.00517155,  0.04924602, -0.02805815, -0.01263298],
                          [ 0.08213249, -0.02805815, -0.04744928,  0.07403869],
                          [ 0.00745266, -0.01263298,  0.07403869, -0.18387143]]),
                np.array([[-0.0282204 , -0.06325738,  0.06453211],
                          [-0.06325738,  0.02472711,  0.03180649],
                          [ 0.06453211,  0.03180649, -0.08552209]]),
                np.array([[-0.0282204 , -0.06325738,  0.06453211],
                          [-0.06325738,  0.02472711,  0.03180649],
                          [ 0.06453211,  0.03180649, -0.08552209]]),
                np.array([[-0.00139116, -0.0858976 ,  0.00933522],
                          [-0.0858976 , -0.03649255,  0.06719452],
                          [ 0.00933522,  0.06719452, -0.15479544]]),
                np.array([[-0.00139116, -0.0858976 ,  0.00933522],
                          [-0.0858976 , -0.03649255,  0.06719452],
                          [ 0.00933522,  0.06719452, -0.15479544]]),
                np.array([[ 0.02524017, -0.07616898],
                          [-0.07616898, -0.09700953]]),
                np.array([[ 0.02524017, -0.07616898],
                          [-0.07616898, -0.09700953]]),
                np.array([[ 0.04338129, -0.0453599 ],
                          [-0.0453599 , -0.15307969]]),
                np.array([[ 0.04338129, -0.0453599 ],
                          [-0.0453599 , -0.15307969]]),
                np.array([[ 0.05112375, -0.00072091],
                          [-0.00072091, -0.20420688]]),
                np.array([[ 0.05112375, -0.00072091],
                          [-0.00072091, -0.20420688]]),
                np.array([[0.04867057]]), np.array([[0.04867057]]),
                np.array([[0.03697756]]), np.array([[0.03697756]]),
                np.array([[0.01732433]]), np.array([[0.01732433]])
        ]

        blk_c = blk_diag_minus(self.blk_a, self.blk_b)

        im = 0
        for mat in result:
            self.assertTrue(np.allclose(mat, blk_c[im]))
            im += 1

    def testBlkDiagApply(self):

        mean_coeff = np.array([
            [ 4.53531036e-04],
            [ 2.29341625e-04],
            [ 9.65040155e-05],
            [-1.19442447e-04],
            [ 0.00000000e+00],
            [ 0.00000000e+00],
            [ 0.00000000e+00],
            [ 0.00000000e+00],
            [ 0.00000000e+00],
            [ 0.00000000e+00],
            [ 0.00000000e+00],
            [ 0.00000000e+00],
            [ 0.00000000e+00],
            [ 0.00000000e+00],
            [ 0.00000000e+00],
            [ 0.00000000e+00],
            [ 0.00000000e+00],
            [ 0.00000000e+00],
            [ 0.00000000e+00],
            [ 0.00000000e+00],
            [ 0.00000000e+00],
            [ 0.00000000e+00],
            [ 0.00000000e+00],
            [ 0.00000000e+00],
            [ 0.00000000e+00],
            [ 0.00000000e+00],
            [ 0.00000000e+00],
            [ 0.00000000e+00],
            [ 0.00000000e+00],
            [ 0.00000000e+00],
            [ 0.00000000e+00],
            [ 0.00000000e+00],
            [ 0.00000000e+00],
            [ 0.00000000e+00]
        ])

        result = np.array([
            [-2.81508398e-04],
            [-1.57256547e-04],
            [ 3.34520158e-05],
            [ 1.44760391e-04],
            [ 0.00000000e+00],
            [ 0.00000000e+00],
            [ 0.00000000e+00],
            [ 0.00000000e+00],
            [ 0.00000000e+00],
            [ 0.00000000e+00],
            [ 0.00000000e+00],
            [ 0.00000000e+00],
            [ 0.00000000e+00],
            [ 0.00000000e+00],
            [ 0.00000000e+00],
            [ 0.00000000e+00],
            [ 0.00000000e+00],
            [ 0.00000000e+00],
            [ 0.00000000e+00],
            [ 0.00000000e+00],
            [ 0.00000000e+00],
            [ 0.00000000e+00],
            [ 0.00000000e+00],
            [ 0.00000000e+00],
            [ 0.00000000e+00],
            [ 0.00000000e+00],
            [ 0.00000000e+00],
            [ 0.00000000e+00],
            [-0.00000000e+00],
            [-0.00000000e+00],
            [-0.00000000e+00],
            [-0.00000000e+00],
            [-0.00000000e+00],
            [-0.00000000e+00]])

        blk_c = blk_diag_apply(self.blk_a, mean_coeff)
        self.assertTrue(np.allclose(result, blk_c))

    def testBlkDiagMult(self):
        result = [
            np.array([[ 0.47509694,  0.07671159, -0.23895441,  0.07671072],
                      [ 0.02999056,  0.24718842,  0.00844581, -0.27214144],
                      [-0.17825818, -0.06319688,  0.30269611,  0.02121738],
                      [ 0.02087111, -0.21182626, -0.02884121,  0.47225584]]),
            np.array([[0.25618175, 0.18178198, 0.03355397],
                      [0.119064  , 0.40103089, 0.11988466],
                      [0.05179662, 0.05420821, 0.18543605]]),
            np.array([[0.25618175, 0.18178198, 0.03355397],
                      [0.119064  , 0.40103089, 0.11988466],
                      [0.05179662, 0.05420821, 0.18543605]]),
            np.array([[ 0.31839362,  0.21986574, -0.13633427],
                      [ 0.12964008,  0.45317229,  0.17613882],
                      [-0.07740028,  0.1119869 ,  0.42657361]]),
            np.array([[ 0.31839362,  0.21986574, -0.13633427],
                      [ 0.12964008,  0.45317229,  0.17613882],
                      [-0.07740028,  0.1119869 ,  0.42657361]]),
            np.array([[ 0.04697816, -0.04669277],
                      [-0.10545702,  0.19065603]]),
            np.array([[ 0.04697816, -0.04669277],
                      [-0.10545702,  0.19065603]]),
            np.array([[ 0.11954209,  0.01013406],
                      [-0.05932909,  0.1161697 ]]),
            np.array([[ 0.11954209,  0.01013406],
                      [-0.05932909,  0.1161697 ]]),
            np.array([[0.14854247, 0.1181599 ],
                      [0.02271051, 0.20908003]]),
            np.array([[0.14854247, 0.1181599 ],
                      [0.02271051, 0.20908003]]),
            np.array([[0.02495947]]), np.array([[0.02495947]]),
            np.array([[0.04302202]]), np.array([[0.04302202]]),
            np.array([[0.05527943]]), np.array([[0.05527943]])
        ]

        blk_c = blk_diag_mult(self.blk_a, self.blk_b)

        im = 0
        for mat in result:
            self.assertTrue(np.allclose(mat, blk_c[im]))
            im += 1

    def testBlkDiagNorm(self):
        result = 0.8235750261689248
        norm = blk_diag_norm(self.blk_a)
        self.assertTrue(result == norm)

    def testBlkDiagSolve(self):
        result = np.array([
            [ -2108.56909528,  -1599.04367287,  12983.7980645 ,   4907.54823872,  11596.60358098],
            [-13261.71782311,  19064.68118668,  -7058.51163424, -23505.65277468,  10718.98836096],
            [   509.34615374,  -6346.73823956,  12742.41838169,  26050.66900347, -11082.31307888],
            [ -3307.59390503,  -2868.45197933,  -9056.27254017, -13121.74603406,  10435.30033164],
            [  5194.61155267,   4738.83799474,   1275.99271119,   5695.36574982,    317.72274105],
            [ -7192.22592633,  -7706.51971094,  -2706.50848048,  -5226.00224303, -10609.21894342],
            [  2106.79729152,    720.663365  ,    477.29928858,   2865.35110109,   2523.12141081],
            [  3293.89400066,   8296.32959773,   6274.69897306,  -6876.89810121,  -5862.81117304],
            [ -5037.67048311,   4648.20122872,  -6478.90991549,   5611.52398572,   5231.26195727],
            [   319.85059444, -13526.13244267,   5392.6728323 ,  -5960.86618271,  -9989.22959649],
            [ -6810.8349795 ,  -5587.85203171,  -4557.56983224, -21895.30335831, -14766.02390764],
            [ -1487.82495778, -17267.75186366,   2518.13873842,  16122.34779131, -10824.59882957],
            [  1696.60328706,   7524.33425367,  -4412.35449613,  -8159.19336023,   3283.61842699],
            [ 16533.21857068,   1048.77054126,    270.18096236,   3130.66029662,   3802.78276484],
            [  3987.29419815,  14592.92355119, -10535.19114199, -11751.50898025,  10280.91948022],
            [  8221.61307636,   4963.62327863,  15482.47214868,   9215.02309094,   2026.10702896],
            [ 10605.58662119,   4939.08507375,  -6298.18788412,   2199.78159731,   6348.7733857 ],
            [  8939.66366506,   5979.70412996,   3984.91381065,   5566.93943721,  -1421.24116192],
            [-21606.51783477,   4822.39145187,   6685.88851131,  15766.49583437, -12707.40988432],
            [ -4230.44592724,   5420.21451676,   -235.85955642,  18100.20123655,  -4768.83642194],
            [  9450.93104008,   8900.03420762,   5202.48555337,   -201.77556792,   5466.57970732],
            [ 11583.03440042,     75.37078542,  19981.80654578,   -358.04535766,  -6139.4067836 ],
            [ 12333.72389213,   1438.96251241,  -8437.87301414,  17219.37822955,  11248.37259986],
            [  2193.30045686,   7010.7452714 ,   7716.40327545,  -7755.61096007,   4158.2657834 ],
            [-16260.99699839, -24157.30011252,   8957.72261107,   7178.33063461,   8681.06123862],
            [  9062.40740653,  14709.69068774,   5430.20220187,  -6558.47236417,  -7115.41480134],
            [  7468.93152378, -11727.69088497,  13044.41696129,  -1429.80060688,    615.43370603],
            [  5660.19210206,    758.33179619,    457.57835518,   8210.45409543,  -6029.85682174],
            [-11618.39974191,  -4792.87662117,   7891.4438672 , -13769.59940549,  21193.75984068],
            [-10062.76974695, -12184.86042594,   3139.30111484,   5233.94758207,   5060.12404909],
            [ 20338.94250519,  -5108.5476594 ,  -7916.199259  , -13155.55120958,  -2631.98451114],
            [ -8575.21386665,  -3075.44542941,   6705.35386167,   1366.04418311,  -3451.27892975],
            [ 11471.10856558, -18990.29443441,  -5960.30374281,  10147.12732058,   2454.46580692],
            [ 23451.62021758,   9401.91573045,  -5248.02166459,  -7872.80360867,   4596.97842653]])

        sn_matrix = [
            np.array([[ 1.29245300e-08, -6.49163277e-10,  2.45070400e-09,  1.53410891e-10],
                      [-6.49163277e-10,  1.20780198e-08,  3.75068433e-09, -2.53453097e-09],
                      [ 2.45070400e-09,  3.75068433e-09,  1.07092249e-08,  1.63163421e-09],
                      [ 1.53410891e-10, -2.53453097e-09,  1.63163421e-09,  1.57226938e-08]]),
            np.array([[1.29101793e-08, 8.87468230e-09, 3.67875235e-09],
                      [8.87468230e-09, 5.05913176e-08, 2.61651494e-08],
                      [3.67875235e-09, 2.61651494e-08, 3.12014975e-08]]),
            np.array([[1.29101793e-08, 8.87468230e-09, 3.67875235e-09],
                      [8.87468230e-09, 5.05913176e-08, 2.61651494e-08],
                      [3.67875235e-09, 2.61651494e-08, 3.12014975e-08]]),
            np.array([[ 1.09084572e-08,  6.16238273e-12, -1.67985227e-09],
                      [ 6.16238273e-12,  9.71880814e-09,  6.56599364e-09],
                      [-1.67985227e-09,  6.56599364e-09,  1.98674901e-08]]),
            np.array([[ 1.09084572e-08,  6.16238273e-12, -1.67985227e-09],
                      [ 6.16238273e-12,  9.71880814e-09,  6.56599364e-09],
                      [-1.67985227e-09,  6.56599364e-09,  1.98674901e-08]]),
            np.array([[ 1.44374266e-08, -4.43138611e-09],
                      [-4.43138611e-09,  1.13592375e-08]]),
            np.array([[ 1.44374266e-08, -4.43138611e-09],
                      [-4.43138611e-09,  1.13592375e-08]]),
            np.array([[1.01359586e-08, 1.48988673e-09],
                      [1.48988673e-09, 8.98955124e-09]]),
            np.array([[1.01359586e-08, 1.48988673e-09],
                      [1.48988673e-09, 8.98955124e-09]]),
            np.array([[1.12133339e-08, 1.87797581e-09],
                      [1.87797581e-09, 9.22078294e-09]]),
            np.array([[1.12133339e-08, 1.87797581e-09],
                      [1.87797581e-09, 9.22078294e-09]]),
            np.array([[9.17068059e-09]]), np.array([[9.17068059e-09]]),
            np.array([[8.62262996e-09]]), np.array([[8.62262996e-09]]),
            np.array([[8.80222582e-09]]), np.array([[8.80222582e-09]])
        ]

        coeff = np.array([
                 [-1.79024086e-05, -4.90370074e-05,  2.02230179e-04,  1.40516221e-04,  1.17363697e-04],
                 [-1.48512889e-04,  2.14767206e-04, -2.29352560e-05, -1.56122232e-04,  5.39212146e-05],
                 [-5.48500768e-05, -5.06209331e-06,  1.27030097e-04,  1.81437248e-04, -3.30330057e-05],
                 [-1.78844625e-05, -1.04020683e-04, -1.01716162e-04, -1.03475356e-04,  1.20600188e-04],
                 [ 1.09850319e-05, -4.56252384e-06, -5.79024234e-06,  3.76900005e-05, -8.07696512e-05],
                 [-2.62638993e-04, -3.28971040e-04, -1.13113193e-04, -1.38873438e-04, -4.67896828e-04],
                 [-1.03340746e-04, -1.61723452e-04, -5.12296850e-05, -2.63840441e-05, -1.97697809e-04],
                 [-1.00631180e-06,  9.85991203e-05,  4.33475295e-05, -6.09100454e-05, -6.60120574e-05],
                 [-2.17261186e-04, -4.51273621e-05, -1.30990539e-04,  6.68971521e-05, -4.87438362e-05],
                 [-1.09714163e-04, -2.69894566e-04,  2.18208856e-05, -6.44599929e-05, -1.96370002e-04],
                 [-7.71549133e-05, -7.37010252e-05, -4.22884340e-05, -2.25038388e-04, -1.66657239e-04],
                 [-3.36196989e-06, -1.18451671e-04, -4.52626978e-06,  1.02981866e-04, -8.37329754e-05],
                 [ 3.53793964e-05,  4.54964533e-05, -6.34722823e-05, -1.94625852e-05,  1.89677483e-05],
                 [ 1.66565383e-04,  3.19224191e-06, -2.31259304e-05,  1.85983791e-05,  3.81422875e-05],
                 [ 9.28366905e-05,  1.74423406e-04, -7.30022809e-07, -5.36855858e-05,  1.13245124e-04],
                 [ 0.00016175,      0.00019267,      0.00023797,      0.00010066,      0.00010137    ],
                 [ 1.13502277e-04,  4.48093004e-05, -1.08588317e-04,  7.08992725e-06,  9.79580181e-05],
                 [ 5.45503135e-05,  4.60378864e-05,  7.31752847e-05,  5.34881056e-05, -4.42780821e-05],
                 [-2.93195776e-04,  4.56038593e-05,  9.75722094e-05,  1.47418646e-04, -1.62329742e-04],
                 [ 4.76921830e-05,  4.01996255e-05, -3.23069382e-05,  1.35737054e-04,  2.14109414e-06],
                 [ 1.13051655e-04,  9.03226722e-05,  8.25028066e-05, -2.57863583e-06,  4.62620049e-05],
                 [ 1.18207098e-04,  1.39375924e-05,  1.87378588e-04, -3.51928983e-06, -4.70459273e-05],
                 [ 1.28281884e-04,  2.50304808e-05, -7.40293647e-05,  1.62979923e-04,  1.20208384e-04],
                 [ 3.80926384e-05,  6.51673450e-05,  5.67955276e-05, -4.40645390e-05,  5.41397444e-05],
                 [-1.65321007e-04, -2.43259429e-04,  1.10643723e-04,  6.81763658e-05,  8.39810614e-05],
                 [ 5.30247326e-05,  9.02680397e-05,  6.68931022e-05, -4.69935188e-05, -4.93068724e-05],
                 [ 9.43813269e-05, -1.30082385e-04,  1.47130724e-04, -6.13797435e-07, -4.42286161e-06],
                 [ 6.62178755e-05, -1.50319069e-05,  2.87163302e-05,  7.30216841e-05, -5.44442313e-05],
                 [-1.06548633e-04, -4.39539406e-05,  7.23699111e-05, -1.26276598e-04,  1.94361202e-04],
                 [-9.22824472e-05, -1.11743463e-04,  2.87895278e-05,  4.79988615e-05,  4.64047814e-05],
                 [ 1.75375175e-04, -4.40491161e-05, -6.82584569e-05, -1.13435450e-04, -2.26946285e-05],
                 [-7.39408960e-05, -2.65184279e-05,  5.78177851e-05,  1.17788935e-05, -2.97591011e-05],
                 [ 1.00971288e-04, -1.67156860e-04, -5.24639395e-05,  8.93173061e-05,  2.16047623e-05],
                 [ 2.06426457e-04,  8.27577854e-05, -4.61942718e-05, -6.92981952e-05,  4.04636422e-05]
                 ])

        coeff_est = blk_diag_solve(sn_matrix, coeff)
        self.assertTrue(np.allclose(result, coeff_est))

    def testBlkDiagTranspose(self):
        blk_c = blk_diag_transpose(self.blk_a)
        result = self.blk_a
        im = 0
        for mat in result:
            self.assertTrue(np.allclose(mat, blk_c[im]))
            im += 1


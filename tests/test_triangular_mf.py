from lfa_toolbox.core.mf.triangular_mf import TriangularMF


def test_fuzzification():
    mf = TriangularMF(p_min=2, p_mid=15, p_max=16, n_points=50)
    assert mf.fuzzify(-2) == 0

    # large margin because it is rounded (i.e. limited by the number of points)
    assert abs(mf.fuzzify(2.5) - 0.03846) < 0.1

    assert mf.fuzzify(15) == 1
    assert mf.fuzzify(118) == 0

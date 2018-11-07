from lfa_toolbox.fs.core.mf.free_shape_mf import FreeShapeMF


def get_mf():
    in_values = [x for x in range(5)]
    mf_values = [0, 10, 10, 5, 0]
    mf = FreeShapeMF(in_values, mf_values)
    return mf


def test_fuzzification_exact_values():
    mf = get_mf()
    assert mf.fuzzify(0) == 0
    assert mf.fuzzify(1) == 10


def test_fuzzification_interpolated_values():
    mf = get_mf()
    assert mf.fuzzify(0.5) == 5
    assert mf.fuzzify(3.5) == 2.5
    assert mf.fuzzify(-1.6) == 0
    assert mf.fuzzify(10000) == 0

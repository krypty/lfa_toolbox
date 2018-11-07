from lfa_toolbox.fs.core.mf.singleton_mf import SingletonMF


def test_fuzzification():
    mf = SingletonMF(10)

    assert mf.fuzzify(10) == 1
    assert mf.fuzzify(5) == 0
    assert mf.fuzzify(15) == 0

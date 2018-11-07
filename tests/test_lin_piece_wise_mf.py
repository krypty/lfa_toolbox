from lfa_toolbox.core.mf.lin_piece_wise_mf import LinPWMF


def test_fuzzification():
    lin1 = LinPWMF([0, 0], [2, 1], [5, 1], [6, 0.5], [10, 0])

    x = abs(lin1.fuzzify(-133) - 0)
    assert x < 1e-2, x

    x = abs(lin1.fuzzify(1) - 0.50)
    assert x < 1e-2, x

    x = abs(lin1.fuzzify(3) - 1.0)
    assert x < 1e-2, x

    x = abs(lin1.fuzzify(6) - 0.5)
    assert x < 1e-2, x

    x = abs(lin1.fuzzify(8) - 0.25)
    assert x < 1e-2, x

    x = abs(lin1.fuzzify(120) - 0)
    assert x < 1e-2, x

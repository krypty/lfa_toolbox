from lfa_toolbox.core.lv.p_points_lv import PPointsLV


def get_lv3():
    lv = PPointsLV(name="", p_points=[1.1, 4.4, 33])
    return lv


def get_lv4():
    lv = PPointsLV(name="", p_points=[1.1, 4.4, 33, 55])
    return lv


def test_labels_are_corrects():
    lv3 = get_lv3()
    sorted_labels = sorted(list(lv3.labels_name))
    assert sorted_labels == sorted(["low", "medium", "high"])

    lv4 = get_lv4()
    sorted_labels = sorted(list(lv4.labels_name))
    assert sorted_labels == sorted(["very low", "low", "medium", "high"])


def test_in_range():
    lv = get_lv4()

    assert 1.1 == lv.in_range[0], "Minimum range for lv is incorrect"
    assert 55 == lv.in_range[1], "Maximum range for lv is incorrect"


def test_fuzzification():
    lv = get_lv4()

    assert lv.ling_values["very low"].fuzzify(1.1) == 1.0
    assert lv.ling_values["low"].fuzzify(1.1) == 0.0
    assert lv.ling_values["medium"].fuzzify(44) == 0.5

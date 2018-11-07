from lfa_toolbox.fs.core.mf.lin_piece_wise_mf import gen_line


def test_n_points_set_to_zero_should_return_emty_lists():
    xs, ys = gen_line(p0=[1, 0], p1=[10, 0], n_points=0)

    assert len(xs) == 0
    assert len(ys) == 0


def equals(a, b, tolerance=1e-6):
    return abs(a - b) < tolerance


def lists_equal(list1, list2):
    return all([equals(a, b) for a, b, in zip(list1, list2)])


def test_flat_slope():
    xs, ys = gen_line(p0=[0, 0], p1=[4, 0], n_points=5)

    assert lists_equal(xs, [0, 1, 2, 3, 4])
    assert lists_equal(ys, [0, 0, 0, 0, 0])


def test_slope_45_degrees():
    xs, ys = gen_line(p0=[0, 0], p1=[4, 4], n_points=5)

    assert lists_equal(xs, [0, 1, 2, 3, 4])
    assert lists_equal(ys, [0, 1, 2, 3, 4])


def test_slope_minus_45_degrees():
    xs, ys = gen_line(p0=[0, 4], p1=[4, 0], n_points=5)

    assert lists_equal(xs, [0, 1, 2, 3, 4])
    assert lists_equal(ys, [4, 3, 2, 1, 0])

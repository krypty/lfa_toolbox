from lfa_toolbox.core.mf.lin_piece_wise_mf import LinPWMF


class TriangularMF(LinPWMF):
    """
    Assumptions:
    - mf values are bound to [0, 1]

    This class is more an example of how you can derive LinPWMF
    """

    def __init__(self, p_min, p_mid, p_max, n_points=50):
        super().__init__([p_min, 0], [p_mid, 1], [p_max, 0], n_points=n_points)

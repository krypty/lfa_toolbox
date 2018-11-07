from lfa_toolbox.core.labels.fuzzy_labels_generator import FuzzyLabelsGenerator
from lfa_toolbox.core.lv.linguistic_variable import LinguisticVariable
from lfa_toolbox.core.mf.lin_piece_wise_mf import LinPWMF


class PPointsLV(LinguisticVariable):
    """
    Syntactic sugar for simplified linguistic variable with N points (p1,
    p2, p3,...pN) and fixed labels ("very low", "low", "medium",
    "high", "very ...").


      ^
      | low      medium           high
    1 |XXXXX       X          XXXXXXXXXXXX
      |     X     X  X       XX
      |      X   X    X    XX
      |       X X      XX X
      |       XX        XXX
      |      X  X     XX   XX
      |     X    X XX       XX
      |    X       X          XX
    0 +-------------------------------------->
           p1     p2          p3


    """

    def __init__(self, name, p_points):
        if not len(p_points) > 1:
            raise ValueError("there must be at least 2 points")

        if p_points != sorted(p_points):
            raise ValueError("p_points must be increasing values")

        labels = FuzzyLabelsGenerator.generate(len(p_points))
        mfs = self._create_mfs(p_points)

        ling_values_dict = {label: lv for label, lv in zip(labels, mfs)}
        super(PPointsLV, self).__init__(name, ling_values_dict)

    @staticmethod
    def _create_mfs(p_points):
        mf_values = len(p_points) * [0]

        for i in range(len(p_points)):
            p_args = [[j, k] for j, k in zip(p_points, mf_values)]
            p_args[i][1] = 1
            yield LinPWMF(*p_args)

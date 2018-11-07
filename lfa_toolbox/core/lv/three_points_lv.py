from lfa_toolbox.core.lv.p_points_lv import PPointsLV


class ThreePointsLV(PPointsLV):
    """
    Syntactic sugar for simplified linguistic variable with only 3 points (p1,
    p2 and p3) and fixed labels ("low", "medium" and "high").


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

    def __init__(self, name, p1, p2, p3):
        assert p1 <= p2 <= p3, "points must be increasing values"
        super(ThreePointsLV, self).__init__(name, p_points=[p1, p2, p3])

def show_mf():
    from matplotlib import pyplot as plt

    from lfa_toolbox.core.mf.triangular_mf import TriangularMF
    from lfa_toolbox.view.mf_viewer import MembershipFunctionViewer

    # Create a matplotlib plot
    fig, ax = plt.subplots()

    # Create a triangular membership function
    temp_mf = TriangularMF(-20, 25, 40)

    # You can fuzzify an input value
    fuzzified_value = temp_mf.fuzzify(22.5)
    print("MF has been fuzzified to {:.3f}".format(fuzzified_value))

    # Or you can visualize the MF using matplotlib
    mfv = MembershipFunctionViewer(temp_mf, ax=ax,
                                   label="Temperature in celsius")
    mfv.fuzzify(22.5)

    plt.legend()  # optionally show the legend i.e. "Temperature"
    plt.show()


def show_mfs():
    from matplotlib import pyplot as plt

    from lfa_toolbox.core.mf.free_shape_mf import FreeShapeMF
    from lfa_toolbox.view.mf_viewer import MembershipFunctionViewer
    from lfa_toolbox.core.mf.lin_piece_wise_mf import LinPWMF
    from lfa_toolbox.core.mf.trap_mf import TrapMF

    fig, axs = plt.subplots(ncols=3, nrows=1)

    # Using FreeShapeMF you can specify each individual points to
    # to compose the craziest membership functions
    mf1 = FreeShapeMF(
        in_values=[5, 30, 100, 120, 200],
        mf_values=[1, 1, 0.7, 0.3, 0]
    )

    # Using LinPWMF (linear piecewise membership function) you only provide
    # inflection points and it generates intermediate points for you.
    # See they are points between x=10 and x=20 for this MF but not for mf1
    # (between x=5 and x=30). With LinPWMF you can specify as many points as you
    # want
    mf2 = LinPWMF((10, 0), (20, 0.5), (30, 0.5), (40, 0))

    mf3 = TrapMF(p0=-20, p1=0, p2=30, n_points=30)

    mfv = MembershipFunctionViewer(mf1, ax=axs[0])
    mfv.fuzzify(55)

    MembershipFunctionViewer(mf2, ax=axs[1])
    MembershipFunctionViewer(mf3, ax=axs[2])

    plt.show()


def show_lv():
    from matplotlib import pyplot as plt
    from lfa_toolbox.core.lv.linguistic_variable import LinguisticVariable
    from lfa_toolbox.view.lv_viewer import LinguisticVariableViewer
    from lfa_toolbox.core.mf.lin_piece_wise_mf import LinPWMF

    fig, axs = plt.subplots(3, figsize=(12, 8))

    for ax in axs:
        lv_temp = LinguisticVariable(
            name="temperature",
            ling_values_dict={
                "cold": LinPWMF([17, 1], [20, 0]),
                "warm": LinPWMF([17, 0], [20, 1], [26, 1], [29, 0]),
                "hot": LinPWMF([26, 0], [29, 1]),
            },
        )
        viewer = LinguisticVariableViewer(lv_temp, ax=ax)
        viewer.fuzzify(26.6)
        viewer.fuzzify(21.8)

    fig.tight_layout()
    plt.show()


def show_lvs():
    from matplotlib import pyplot as plt
    from lfa_toolbox.view.lv_viewer import LinguisticVariableViewer
    from lfa_toolbox.core.lv.p_points_lv import PPointsLV

    fig, ax = plt.subplots()
    # PPointsLV helps you create a linguistic variable that is human
    # interpretable and generate automatically fuzzy labels for you.
    lv = PPointsLV("Github stars", [0, 50, 300, 1000])
    LinguisticVariableViewer(lv, ax=ax)

    plt.show()


if __name__ == "__main__":
    # show_mf()
    # show_mfs()
    # show_lv()
    show_lvs()

import os

import numpy as np

from lfa_toolbox.core.fis.fis import MIN, AND_min
from lfa_toolbox.core.fis.singleton_fis import SingletonFIS
from lfa_toolbox.core.lv.linguistic_variable import LinguisticVariable
from lfa_toolbox.core.lv.three_points_lv import ThreePointsLV
from lfa_toolbox.core.mf.singleton_mf import SingletonMF
from lfa_toolbox.core.rules.default_fuzzy_rule import DefaultFuzzyRule
from lfa_toolbox.core.rules.fuzzy_rule import FuzzyRule
from lfa_toolbox.core.rules.fuzzy_rule_element import Antecedent, Consequent

SETOSA = "setosa"
VERSICOLOR = "versicolor"
VIRGINICA = "virginica"

IRIS_LABEL_PREFIX_LENGTH = len("Iris-")
LABEL_COLUMN = 4

"""
IRIS DATASET SOURCE: 
https://archive.ics.uci.edu/ml/machine-learning-databases/iris/
"""

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    # Build FIS from Fig 3.9 of Carlos Peña's book
    lv_sl = ThreePointsLV(name="SL", p1=5.68, p2=6.45, p3=7.10)
    lv_sw = ThreePointsLV(name="SW", p1=3.16, p2=3.16, p3=3.45)
    lv_pl = ThreePointsLV(name="PL", p1=1.19, p2=1.77, p3=6.03)
    lv_pw = ThreePointsLV(name="PW", p1=1.55, p2=1.65, p3=1.74)

    lv_output = LinguisticVariable(
        name="output",
        ling_values_dict={
            SETOSA: SingletonMF(1),
            VERSICOLOR: SingletonMF(2),
            VIRGINICA: SingletonMF(3),
        },
    )

    r1 = FuzzyRule(
        ants=[Antecedent(lv_pl, "high")],
        ant_act_func=AND_min,
        cons=[Consequent(lv_output, VIRGINICA)],
        impl_func=MIN,
    )

    r2 = FuzzyRule(
        ants=[Antecedent(lv_sw, "low"), Antecedent(lv_pw, "high")],
        ant_act_func=AND_min,
        cons=[Consequent(lv_output, VIRGINICA)],
        impl_func=MIN,
    )

    r3 = FuzzyRule(
        ants=[Antecedent(lv_sl, "medium"), Antecedent(lv_pw, "medium")],
        ant_act_func=AND_min,
        cons=[Consequent(lv_output, SETOSA)],
        impl_func=MIN,
    )

    rules = [r1, r2, r3]
    dr = DefaultFuzzyRule(cons=[Consequent(lv_output, SETOSA)], impl_func=MIN)

    fis = SingletonFIS(rules=rules, default_rule=dr)

    # Read Iris dataset
    iris_data_path = os.path.join(HERE, "iris.data")
    iris_data = np.loadtxt(iris_data_path, delimiter=",", dtype="f8,f8,f8,f8,|U15")

    dict_output = {SETOSA: 1, VERSICOLOR: 2, VIRGINICA: 3}

    n_correct_pred = 0
    for idx, sample in enumerate(iris_data):
        predicted_out = fis.predict(
            {"SL": sample[0], "SW": sample[1], "PL": sample[2], "PW": sample[3]}
        )

        expected_sample_label = get_sample_expected_label(sample)

        pred_out_label = predicted_out["output"]
        expected_out_label = dict_output[expected_sample_label]
        print("predicted {}, expected {}".format(pred_out_label, expected_out_label))

        if are_outputs_equal(pred_out_label, expected_out_label):
            n_correct_pred += 1

    print("Accuracy: {}".format(n_correct_pred / float(len(iris_data))))
    assert n_correct_pred == len(
        iris_data
    ), "The book says this FIS make no misclassification"


def are_outputs_equal(pred_out, expected_out, tolerance=0.5):
    out = int(pred_out - expected_out + tolerance)
    return out == 0


def get_sample_expected_label(sample):
    label = sample[LABEL_COLUMN]
    return remove_iris_dash_prefix(label)


def remove_iris_dash_prefix(label):
    return label[IRIS_LABEL_PREFIX_LENGTH:]


if __name__ == "__main__":
    main()

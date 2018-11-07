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

"""
IRIS DATASET SOURCE: 
https://archive.ics.uci.edu/ml/machine-learning-databases/iris/
"""

IRIS_LABEL_PREFIX_LENGTH = len("Iris-")
LABEL_COLUMN = 4

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    # Build FIS from Fig 3.9 of Carlos Peña's book
    lv_sl = ThreePointsLV(name="SL", p1=4.65, p2=4.65, p3=5.81)
    lv_sw = ThreePointsLV(name="SW", p1=2.68, p2=3.74, p3=4.61)
    lv_pl = ThreePointsLV(name="PL", p1=4.68, p2=5.26, p3=6.03)
    lv_pw = ThreePointsLV(name="PW", p1=0.39, p2=1.16, p3=2.03)

    yes_no = {"no": SingletonMF(0), "yes": SingletonMF(1)}
    lv_setosa = LinguisticVariable(name=SETOSA, ling_values_dict=yes_no)
    lv_virginica = LinguisticVariable(name=VIRGINICA, ling_values_dict=yes_no)
    lv_versicolor = LinguisticVariable(name=VERSICOLOR, ling_values_dict=yes_no)

    r1 = FuzzyRule(
        ants=[Antecedent(lv_pw, "low")],
        ant_act_func=AND_min,
        cons=[
            Consequent(lv_setosa, "yes"),
            Consequent(lv_versicolor, "no"),
            Consequent(lv_virginica, "no"),
        ],
        impl_func=MIN,
    )

    r2 = FuzzyRule(
        ants=[Antecedent(lv_pl, "low"), Antecedent(lv_pw, "medium")],
        ant_act_func=AND_min,
        cons=[
            Consequent(lv_setosa, "no"),
            Consequent(lv_versicolor, "yes"),
            Consequent(lv_virginica, "no"),
        ],
        impl_func=MIN,
    )

    r3 = FuzzyRule(
        ants=[
            Antecedent(lv_sl, "high"),
            Antecedent(lv_sw, "medium"),
            Antecedent(lv_pl, "low"),
            Antecedent(lv_pw, "high"),
        ],
        ant_act_func=AND_min,
        cons=[
            Consequent(lv_setosa, "no"),
            Consequent(lv_versicolor, "yes"),
            Consequent(lv_virginica, "no"),
        ],
        impl_func=MIN,
    )

    rules = [r1, r2, r3]
    dr = DefaultFuzzyRule(
        cons=[
            Consequent(lv_setosa, "no"),
            Consequent(lv_versicolor, "no"),
            Consequent(lv_virginica, "yes"),
        ],
        impl_func=MIN,
    )

    fis = SingletonFIS(rules=rules, default_rule=dr)

    iris_data = read_iris_dataset()
    # iris_data = [iris_data[-1]]

    n_correct_pred = 0
    for idx, sample in enumerate(iris_data):
        predicted_out = fis.predict(
            {"SL": sample[0], "SW": sample[1], "PL": sample[2], "PW": sample[3]}
        )

        predicted_out = [(k, v) for k, v in predicted_out.items()]
        predicted_out = sorted(predicted_out, key=lambda x: x[0])

        predicted_sample = max(predicted_out, key=lambda x: x[1])
        predicted_sample_label = predicted_sample[0]
        predicted_sample_value = predicted_sample[1]

        # the max pred must reach at least 0.5 to be considered as a the true
        # predicted output
        if predicted_sample_value < 0.5:
            continue

        expected_sample_label = get_sample_expected_label(sample)
        predicted_sample_label = predicted_sample_label

        if are_outputs_equal(predicted_sample_label, expected_sample_label):
            n_correct_pred += 1

    print("pred OK: {}, total pred: {}".format(n_correct_pred, len(iris_data)))
    # FISViewer(fis).show()
    assert n_correct_pred == 149, (
        "The book says this FIS must predict " "correctly 149 cases "
    )


def read_iris_dataset():
    iris_data_path = os.path.join(HERE, "iris.data")
    iris_data = np.loadtxt(iris_data_path, delimiter=",", dtype="f8,f8,f8,f8,|U15")
    return iris_data


def are_outputs_equal(predicted, expected):
    return predicted == expected


def get_sample_expected_label(sample):
    label = sample[LABEL_COLUMN]
    return remove_iris_dash_prefix(label)


def remove_iris_dash_prefix(label):
    return label[IRIS_LABEL_PREFIX_LENGTH:]


if __name__ == "__main__":
    main()

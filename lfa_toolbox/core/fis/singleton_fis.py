import sys
from itertools import chain
from typing import List

from lfa_toolbox.core.fis.fis import FIS
from lfa_toolbox.core.mf.free_shape_mf import FreeShapeMF
from lfa_toolbox.core.mf.singleton_mf import SingletonMF
from lfa_toolbox.core.rules.default_fuzzy_rule import DefaultFuzzyRule
from lfa_toolbox.core.rules.fuzzy_rule import FuzzyRule


class SingletonFIS(FIS):
    def __init__(self, rules: List[FuzzyRule], default_rule: DefaultFuzzyRule = None):
        """
        Create a singleton fuzzy inference system. This class is not optimized
        for speed because it is more like a wrapper around the FIS class. This
        class can be used however for learning purposes or to see the error
        compared to a Mamdani-like FIS.

        :param rules: see FIS docstring
        :param default_rule: see FIS docstring
        """

        if not self._are_all_consequents_singleton(rules):
            print("All consequents must be singleton when using a SingletonFIS")

        super(SingletonFIS, self).__init__(
            aggr_func=None, defuzz_func=None, rules=rules, default_rule=default_rule
        )

    def _aggregate(self, rules_implicated_cons):
        aggregated_consequents = {}

        for out_v_name, out_v_mf in rules_implicated_cons.items():
            numerator = 0
            denominator = 0

            for i, rule in enumerate(chain(self._rules, [self._default_rule])):
                # TODO: refactor this to better handle default rule
                if rule is None:  # happen if default rule is not set.
                    continue

                cons = self._get_consequent_from_out_var_name(rule, out_v_name)

                cons_implicated_value = out_v_mf[i].mf_values[0]
                label = cons.lv_value

                rule_act_value = cons.lv_name.ling_values[label].in_values[0]

                numerator += cons_implicated_value * rule_act_value
                denominator += cons_implicated_value

            aggregated_consequents[out_v_name] = FreeShapeMF(
                in_values=[numerator / float(denominator)], mf_values=[1]
            )

        return aggregated_consequents

    def _defuzzify(self):
        self._defuzzified_outputs = {
            k: v.in_values[0] for k, v in self._aggregated_consequents.items()
        }
        return self._defuzzified_outputs

    @staticmethod
    def _get_consequent_from_out_var_name(rule, out_v_name):
        consequents_it = enumerate(rule.consequents)
        index = [i for i, cons in consequents_it if cons.lv_name.name == out_v_name][0]
        return rule.consequents[index]

    @staticmethod
    def _are_all_consequents_singleton(rules: List[FuzzyRule]):
        def show_error(name):
            print("{} is not a SingletonMF".format(name), file=sys.stderr)

        for r in rules:
            for cons in r.consequents:
                for lv_name, lv_value in cons.lv_name.ling_values.items():
                    if not isinstance(lv_value, SingletonMF):
                        show_error(cons.lv_name.name)
                        return False
        return True

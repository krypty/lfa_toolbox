import os

from trefle_engine import TrefleFIS

from lfa_toolbox.trefle.tff_json_to_singletonfis import TffJsonToSingletonFIS


class TffConverter:
    @staticmethod
    def to_fis(tff_str: str):
        """

        :param tff_str: if tff_str is a valid file path, this latter
        will be read and parsed. Otherwise tff_str will be interpreted as
        a json str and parsed directly.
        :return: a SingletonFIS instance
        """
        return TffJsonToSingletonFIS(tff_str).convert()
        # raise NotImplementedError

    @staticmethod
    def to_trefle_fis(tff_str):
        """

        :param tff_str: if tff_str is a valid file path, this latter
        will be read and parsed. Otherwise tff_str will be interpreted as
        a json str and parsed directly.
        :return: a TrefleFIS instance
        """

        if os.path.exists(tff_str):
            return TrefleFIS.from_tff_file(tff_str)
        else:
            return TrefleFIS.from_tff(tff_str)

import re

from .parse import convert_text_to_element_list
from .stringify import to_str


class BeadsVec:
    """Beads Vector Number"""

    def __init__(self, value=0):

        # 整数かどうか判定
        try:
            int_value = int(str(value), 10)
        except ValueError:
            # 整数でなければ次へ
            pass
        else:
            # タプルとして格納する
            self._elements = int_value,
            return

        # タプル型か？
        if type(value) is tuple:
            # そのまま入れる
            self._elements = value
            return

        # それ以外は文字列として扱う
        new_element_list = convert_text_to_element_list(value)

        # タプルとして格納する
        self._elements = tuple(new_element_list)

    def __str__(self):
        """数珠玉記数法"""
        return to_str(self._elements)

    @property
    def elements(self):
        return self._elements

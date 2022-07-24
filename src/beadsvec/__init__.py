import re

from .parse import convert_text_to_element_list


class BeadsVec:
    """Beads Vector Number"""

    # 英字，アンダースコアか
    __pat_alphabet_etc = re.compile(r"^[A-Za-z_]$")

    # @staticmethod
    # def is_alphabet_etc_of_left_end(text):
    #    """左端は英字などか？"""
    #    return BeadsVec.__pat_alphabet_etc.match(text[:1])

    @staticmethod
    def is_alphabet_etc_of_right_end(text):
        """右端は英字などか？"""
        return BeadsVec.__pat_alphabet_etc.match(text[-1:])

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
        text = ""
        for token in self._elements:

            # タプル型か？
            if type(token) is tuple:
                # `q`, `p` で挟んだものを `o` で接続
                sub_text = ""
                for elem in token:
                    sub_text = f"{sub_text}o{elem}"
                # 先頭の 'o' は除去します
                sub_text = sub_text.lstrip('o')

                # `q` が間に入るので、`o` は不要
                text = f"{text}q{sub_text}p"
            else:
                # 左項の右端が英字などなら、セパレーターの `o` は不要
                if BeadsVec.is_alphabet_etc_of_right_end(text):
                    separator = ""
                else:
                    separator = "o"

                # 接続
                text = f"{text}{separator}{token}"

        # 先頭の 'o' は除去します
        return text.lstrip('o')

    @property
    def elements(self):
        return self._elements

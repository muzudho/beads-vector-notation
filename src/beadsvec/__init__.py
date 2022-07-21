import re
from dicordnum import DicOrdNum


class BeadsVec:
    """Beads Nested Number"""

    # めんどくさいので .upper() して 'O' と数字で構成されていればOkとする
    # 辞書順記数法に対応するために、めんどくさいので '_', 'A' が含まれていてもOkとする
    pattern1 = re.compile(r"^([_AO\d]*)$")

    def __init__(self, value=0):

        # 整数かどうか判定
        try:
            int_column = int(str(value), 10)
        except ValueError:
            # 整数でなければ次へ
            pass
        else:
            # タプルとして格納する
            self._columns = int_column,
            return

        # タプル型なら
        if type(value) is tuple:
            # そのまま入れる
            self._columns = value
            return

        # それ以外は文字列として扱う

        # 大文字に変換
        value = value.upper()

        # '_', 'A', 'O' と数字で構成されている必要がある
        result = BeadsVec.pattern1.match(value)
        if result:
            pass
        else:
            raise ValueError(f"not beads vector: {value}")

        # 先頭に O が付いているのは構わないものとし、
        # 先頭に付いている O は削除する
        value = value.lstrip('O')

        new_columns = []

        # 区切り文字 O で分割
        columns = value.split('O')

        for column in columns:
            if column[:1] == 'A':
                # A を除去する
                n = int(column.replace('A', ''))
                new_columns.append(n)

            elif column[:1] == '_':
                # まず '_' を除去する
                column = column.replace('_', '')

                figure = len(column)
                modulo = 1
                for i in range(0, figure):
                    modulo *= 10

                z = -1 * (modulo - int(column))
                new_columns.append(z)

            else:
                n = int(column)
                new_columns.append(n)

        # タプルとして格納する
        self._columns = tuple(new_columns)

    def __str__(self):
        """辞書順記数法"""
        text = ""
        for column in self._columns:
            # print(
            #    f"column:{column} DicOrdNum(column):{DicOrdNum(column)} text:{text}")
            text = f"{text}o{DicOrdNum(column)}"

        # 先頭だけを大文字の 'O' にする
        # print(f"text:{text}")
        text = f"O{text[1:]}"
        return text

    @property
    def columns(self):
        return self._columns

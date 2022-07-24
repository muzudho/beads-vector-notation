import re

# 英字，アンダースコアか
__pat_alphabet_etc = re.compile(r"^[A-Za-z_]$")

# @staticmethod
# def is_alphabet_etc_of_left_end(text):
#    """左端は英字などか？"""
#    return __pat_alphabet_etc.match(text[:1])


def is_alphabet_etc_of_right_end(text):
    """右端は英字などか？"""
    return __pat_alphabet_etc.match(text[-1:])


def to_str(elements):
    text = ""
    for element in elements:

        # タプル型か？
        if type(element) is tuple:
            text2 = to_str_from_tuple(element)
            text = f"{text}{text2}"

        else:
            # 左項の右端が英字などなら、セパレーターの `o` は不要
            if is_alphabet_etc_of_right_end(text):
                separator = ""
            else:
                separator = "o"

            # 接続
            text = f"{text}{separator}{element}"

    # 先頭の 'o' は除去します
    return text.lstrip('o')


def to_str_from_tuple(element_list):
    # `q`, `p` で挟んだものを `o` で接続
    sub_text = ""
    for elem in element_list:
        sub_text = f"{sub_text}o{elem}"
    # 先頭の 'o' は除去します
    sub_text = sub_text.lstrip('o')

    # `q` が間に入るので、頭の `o` は不要
    return f"q{sub_text}p"

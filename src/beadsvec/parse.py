def index_qp(text):
    # print(f"index_qp text:{text}")

    try:
        q = text.index('Q')
        # print(f"Q:{q}")

        p = text.index('P', q)
        # print(f"P:{p}")

        return q, p
    except:
        return None, None


def convert_text_to_element_list(text):
    # 大文字に変換
    text = text.upper()
    # print(f"convert_text_to_element_list text:{text}")

    q, p = index_qp(text)  # WIP

    new_element_list = []

    if not q is None and not p is None:
        # print(f"q:{q} p:{p}")

        a_str = text[:q]
        b_str = text[q+1:p]
        c_str = text[p+1:]
        # print(f"a:{a_str}")
        # print(f"b:{b_str}")
        # print(f"c:{c_str}")

        if a_str:  # 空文字列を避ける
            new_element_list.extend(convert_text_to_element_list(a_str))

        if b_str:
            new_element_list.append(
                tuple(convert_text_to_element_list(b_str)))

        if c_str:
            new_element_list.extend(convert_text_to_element_list(c_str))

    else:
        # print(f"q,p なし q:{q} p:{p} text:{text}")
        # 区切り文字 'O' で分割
        tokens = text.split('O')

        for token in tokens:
            # 整数かどうか判定
            try:
                int_element = int(str(token), 10)
                new_element_list.append(int_element)

            except ValueError:
                # 整数でなければ
                raise ValueError(f"no beads vector notation: {text}")

    return new_element_list

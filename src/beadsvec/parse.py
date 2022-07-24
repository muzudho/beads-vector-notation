def index_qp(text):

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

    q, p = index_qp(text)  # WIP

    new_element_list = []

    if q:
        # print(f"a:{text[:q]}")
        # print(f"b:{text[q+1:p]}")
        # print(f"c:{text[p+1:]}")
        new_element_list.extend(convert_text_to_element_list(text[:q]))
        new_element_list.append(
            tuple(convert_text_to_element_list(text[q+1:p])))
        new_element_list.extend(convert_text_to_element_list(text[p+1:]))

    else:
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

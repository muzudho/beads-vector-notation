def search_q():
    pass


def convert_text_to_element_list(text):
    # 大文字に変換
    text = text.upper()

    new_element_list = []

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

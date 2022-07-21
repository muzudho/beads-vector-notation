"""
python -m tests.test
"""
from src.beadsvec import BeadsVec

test_data = [
    # 正の零
    ['0', BeadsVec(0), 'O0'],
    # -   -----------   --
    # 1   2             3
    # 1. Test case text
    # 2. Actual
    # 3. Expected

    # 正の整数
    ['1', BeadsVec(1), 'O1'],
    ['10', BeadsVec(10), 'OA10'],

    # 正の整数の文字列
    ['"0"', BeadsVec('0'), 'O0'],
    ['"1"', BeadsVec('1'), 'O1'],
    ['"10"', BeadsVec('10'), 'OA10'],

    # 1o2 の形
    #['"1o2"', BeadsVec('1o2')],
    #['"1o2o3"', BeadsVec('1o2o3')],
    #['"1o2o3o4"', BeadsVec('1o2o3o4')],

    # O1o2 の形
    ['"O1o2o_9"', BeadsVec('O1o2o_9'), 'O1o2o_9'],
    ['"O1o2"', BeadsVec('O1o2'), 'O1o2'],
    ['"O1o2oA10o4"', BeadsVec('O1o2oA10o4'), 'O1o2oA10o4'],

    # o1o2 の形, snake_case への寛容
    ['"o1o2o_9"', BeadsVec('o1o2o_9'), 'O1o2o_9'],
    ['"o1o2"', BeadsVec('o1o2'), 'O1o2'],
    ['"o1o2oA10o4"', BeadsVec('o1o2oA10o4'), 'O1o2oA10o4'],

    # O1O2 の形
    ['"O1O2O_9"', BeadsVec('O1O2O_9'), 'O1o2o_9'],
    ['"O1O2"', BeadsVec('O1O2'), 'O1o2'],
    ['"O1O2OA10O4"', BeadsVec('O1O2OA10O4'), 'O1o2oA10o4'],

    # 混在
    ['"o_9O1oA10"', BeadsVec('o_9O1oA10'), 'O_9o1oA10'],

    # 拡張: 辞書順記数法への寛容
    ['A77', BeadsVec('A77'), 'OA77'],
    ['AA777', BeadsVec('AA777'), 'OAA777'],
    ['O7oA77oAA777oAAA7777', BeadsVec(
        'O7oA77oAA777oAAA7777'), 'O7oA77oAA777oAAA7777'],

    ['a77', BeadsVec('a77'), 'OA77'],
    ['aa777', BeadsVec('aa777'), 'OAA777'],
    ['o7oa77oaa777oaaa7777', BeadsVec(
        'O7oa77oaa777oaaa7777'), 'O7oa77oaa777oaaa7777'],

    # タプル
    ['"(1,2)"', BeadsVec((1, 2)), 'O1o2'],
    ['"(1,2,-3)"', BeadsVec((1, 2, 3)), 'O1o2o_7'],
    ['"(1,2,10,4)"', BeadsVec((1, 2, 3, 4)), 'O1o2oA10o4'],
]

for datum in test_data:
    if f'{datum[1]}' == datum[2]:
        print(
            f'"{datum[0]}" --> "{datum[1]}" {datum[1].columns}')
    else:
        print(
            f'[Error] "{datum[0]}" --> "{datum[1]}" {datum[1].columns} Expected: "{datum[2]}"')


# B は使えない文字だ
try:
    print(f'[Error] "OB1" --> {BeadsVec("OB1")}')
except:
    print(f'"OB1" is not BeadsVec')

# o が２連続するのはおかしい
try:
    print(f'[Error] "O2oo1" --> {BeadsVec("O2oo1")}')
except:
    print(f'"O2oo1" is not BeadsVec')

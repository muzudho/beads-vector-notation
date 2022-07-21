"""
python -m tests.test
"""
from src.beadsvec import BeadsVec

test_data = [
    # 正の零
    ['0', BeadsVec(0), '0', (0,)],
    # -   -----------   -   ----
    # 1   2             3   3
    # 1. Test case text
    # 2. Actual
    # 3. Expected

    # 負の零（正の零になります）
    ['-0', BeadsVec(-0), '0', (0,)],

    # 正の整数
    ['1', BeadsVec(1), '1', (1,)],
    ['10', BeadsVec(10), '10', (10,)],

    # 負の整数
    ['-1', BeadsVec(-1), '-1', (-1,)],

    # 整数の文字列
    ['"-1"', BeadsVec('-1'), '-1', (-1,)],
    ['"0"', BeadsVec('0'), '0', (0,)],
    ['"1"', BeadsVec('1'), '1', (1,)],
    ['"10"', BeadsVec('10'), '10', (10,)],

    # 数珠玉記数法 デフォルト（snake_case）
    ['"1o2o-1"', BeadsVec('1o2o-1'), '1o2o-1', (1, 2, -1)],
    ['"1o2"', BeadsVec('1o2'), '1o2', (1, 2)],
    ['"1o2o10o4"', BeadsVec('1o2o10o4'), '1o2o10o4', (1, 2, 10, 4)],

    # 数珠玉記数法 UPPER_SNAKE_CASE
    ['"1O2O-1"', BeadsVec('1O2O-1'), '1o2o-1', (1, 2, -1)],
    ['"1O2"', BeadsVec('1O2'), '1o2', (1, 2)],
    ['"1O2O10O4"', BeadsVec('1O2O10O4'), '1o2o10o4', (1, 2, 10, 4)],

    # 混在
    ['"-1O1o10"', BeadsVec('-1O1o10'), '-1o1o10', (-1, 1, 10)],

    # タプル
    ['(1,2)', BeadsVec((1, 2)), '1o2', (1, 2)],
    ['(1,2,-3)', BeadsVec((1, 2, -3)), '1o2o-3', (1, 2, -3)],
    ['(1,2,10,4)', BeadsVec((1, 2, 10, 4)), '1o2o10o4', (1, 2, 10, 4)],
]

for datum in test_data:
    if f'{datum[1]}' == datum[2] and datum[1].elements == datum[3]:
        print(
            f'{datum[0]} --> "{datum[1]}" {datum[1].elements}')
    else:
        print(
            f'[Error] {datum[0]} --> "{datum[1]}" {datum[1].elements} Expected: "{datum[2]}" {datum[3]}')


# B は使えない文字だ
try:
    print(f'[Error] "B1" --> {BeadsVec("B1")}')
except:
    print(f'"B1" is not BeadsVec')

# o が２連続するのはおかしい
try:
    print(f'[Error] "2oo1" --> {BeadsVec("2oo1")}')
except:
    print(f'"2oo1" is not BeadsVec')

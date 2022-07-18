"""
python -m test
"""
from src.beadsnum import BeadsNum

test_data = [
    # 正の整数
    ['0', BeadsNum(0)],
    ['1', BeadsNum(1)],
    ['10', BeadsNum(10)],

    # 正の整数の文字列
    ['"0"', BeadsNum('0')],
    ['"1"', BeadsNum('1')],
    ['"10"', BeadsNum('10')],

    # 1o2 の形
    ['"1o2"', BeadsNum('1o2')],
    ['"1o2o3"', BeadsNum('1o2o3')],
    ['"1o2o3o4"', BeadsNum('1o2o3o4')],

    # O1o2 の形
    ['"O1o2"', BeadsNum('O1o2')],
    ['"O1o2o3"', BeadsNum('O1o2o3')],
    ['"O1o2o3o4"', BeadsNum('O1o2o3o4')],

    # o1o2 の形
    ['"o1o2"', BeadsNum('o1o2')],
    ['"o1o2o3"', BeadsNum('o1o2o3')],
    ['"o1o2o3o4"', BeadsNum('o1o2o3o4')],

    # O1O2 の形
    ['"O1O2"', BeadsNum('O1O2')],
    ['"O1O2O3"', BeadsNum('O1O2O3')],
    ['"O1O2O3O4"', BeadsNum('O1O2O3O4')],

    # 混在
    ['"o12O34o56O78o910"', BeadsNum('o12O34o56O78o910')],

    # タプル
    ['"(1,2)"', BeadsNum((1, 2))],
    ['"(1,2,3)"', BeadsNum((1, 2, 3))],
    ['"(1,2,3,4)"', BeadsNum((1, 2, 3, 4))],
]

for datum in test_data:
    print(f"{datum[0]} --> {datum[1]} {datum[1].numbers}")

# B は使えない文字だ
try:
    print(f"OB1 --> {BeadsNum('OB1')} is bad")
except:
    print(f"OB1 is not BeadsNum")

# o が２連続するのはおかしい
try:
    print(f"[Error] O2oo1 --> {BeadsNum('O2oo1')}")
except:
    print(f"O2oo1 is not BeadsNum")

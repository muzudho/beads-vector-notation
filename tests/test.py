"""
python -m tests.test
"""
from src.beadsvec import BeadsVec

# Order of Ascii Code
#
# ! " # $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @
# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# [ \ ] ^ _ `
# a b c d e f g h i j k l m n o p q r s t u v w x y z
# { | } ~
#
# 記号の数 32
# 数字の数 10
# 大文字の数 26
# 小文字の数 26
#
# 日本の小学校で習う算数の記号
# ＋　ー　×　 ÷　 ＝　 ：　 ．　（　 ）　度数°
#
# 数珠玉表記でエンコードしたい記号（演算優先順）
# ;  :  (  )  *  /  +  -  .  ,  SPACE
# 対応させたいアルファベット
# j  i  q  p  x  y  t  n  o  g  u
#
# Examples
# --------
#
# [-1 0 1 2]
# n1u0u1u2
#
# 128.0.0.1
# 128o0o0o1
#
# 5-4*(1+2)/3
# 5n4xq1t2py3

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

    # タプル
    ['(1,2)', BeadsVec((1, 2)), '1o2', (1, 2)],
    ['(1,2,-3)', BeadsVec((1, 2, -3)), '1o2o-3', (1, 2, -3)],
    ['(1,2,10,4)', BeadsVec((1, 2, 10, 4)), '1o2o10o4', (1, 2, 10, 4)],

    # ネストしたタプル
    ['((1,2),3)', BeadsVec(((1, 2), 3)), 'q1o2p3', ((1, 2), 3)],
    ['(1,(2,3))', BeadsVec((1, (2, 3))), '1q2o3p', (1, (2, 3))],

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

    # 文字列：括弧
    ['q13o14p', BeadsVec('q13o14p'),
     'q13o14p', ((13, 14),)],
    ['21o22q23o24p', BeadsVec('21o22q23o24p'),
     '21o22q23o24p', (21, 22, (23, 24))],
    ['q33o34p35o36', BeadsVec('q33o34p35o36'),
     'q33o34p35o36', ((33, 34), 35, 36)],
    ['41o42q43o44p45o46', BeadsVec('41o42q43o44p45o46'),
     '41o42q43o44p45o46', (41, 42, (43, 44), 45, 46)],
    #['(1,2,-3)', BeadsVec((1, 2, -3)), '1o2o-3', (1, 2, -3)],
    #['(1,2,10,4)', BeadsVec((1, 2, 10, 4)), '1o2o10o4', (1, 2, 10, 4)],

    # ネストしたタプル
    #['((1,2),3)', BeadsVec(((1, 2), 3)), 'q1o2p3', ((1, 2), 3)],
    #['(1,(2,3))', BeadsVec((1, (2, 3))), '1q2o3p', (1, (2, 3))],
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

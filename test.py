"""
python -m test
"""
from beadsnum import BeadsNum

print(f"0 --> {str(BeadsNum(0))}")
print(f"1 --> {str(BeadsNum(1))}")
# print(f"'O2o1' --> {str(BeadsNum('O2o1'))}")

# B は使えない文字だ
try:
    print(f"OB1 --> {str(BeadsNum('OB1'))} is bad")
except:
    print(f"OB1 is not BeadsNum")

# o が２連続するのはおかしい
try:
    print(f"[Error] O2oo1 --> {str(BeadsNum('O2oo1'))}")
except:
    print(f"O2oo1 is not BeadsNum")

print(f"(2,1) --> {str(BeadsNum((2,1)))}")

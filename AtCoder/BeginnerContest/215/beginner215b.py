import math

N = int(input())

for k in reversed(range(60)):
    if N >= 2**k:
        print(k)
        break

# 整数型の問題で実数を介すると精度の問題がでる
# print(math.floor(math.log2(N)))
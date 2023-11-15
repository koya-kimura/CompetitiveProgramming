# AとBが同じ数値で倍数だと弾かれてしまう

import math

A, B, C = map(int, input().split())

a = math.floor(A/C)
b = math.floor(B/C)

if(a==b):
    print(-1)
else:
    print(b*C)
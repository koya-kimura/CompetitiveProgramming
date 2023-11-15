# import math は基本いらない. 切り捨ては //
import math

N = int(input())
A = list(map(int, input().split()))
X = int(input())

sumA = sum(A)

s = math.floor(X/sumA)*sumA
ans = math.floor(X/sumA)*N

while s <= X:
    s += A[ans%N]
    ans += 1

print(ans)
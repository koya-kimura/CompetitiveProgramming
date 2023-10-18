N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

result = [0] * N

result[0] = T[0]

for i in range(N-1):
    result[i+1] = T[i+1]
    if T[i+1] > result[i] + S[i]:
        result[i+1] =  result[i] + S[i]

# 2周目回すことで, 前のTが大きい問題も解消
# 以下がそのケース
# 4
# 1 1 1 1
# 1000 100 10 1
for i in range(N):
    result[i] = T[i]
    if T[i] > result[i-1] + S[i-1]:
        result[i] =  result[i-1] + S[i-1]

for i in range(N):
    print(result[i])
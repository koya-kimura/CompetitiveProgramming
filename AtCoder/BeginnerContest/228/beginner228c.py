N, K = map(int, input().split())
P = [sum(map(int, input().split())) for _ in range(N)]

# どうせ変わらん
n = sorted(P, reverse=True)[K-1]

for p in P:
    if n - p <= 300:
        print("Yes")
    else:
        print("No")
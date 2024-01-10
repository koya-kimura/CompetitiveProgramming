N, X = map(int, input().split())
A = list(map(int, input().split()))

ans = []

for i in range(N):
    ans.append(X)
    X = A[X-1]

print(len(set(ans)))
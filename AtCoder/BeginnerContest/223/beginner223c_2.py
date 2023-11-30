N = int(input())
AB = [map(int, input().split()) for _ in range(N)]
A, B = [list(i) for i in zip(*AB)]

T = []
t = 0
for i in range(N):
    T.append(A[i]/B[i])
    t += A[i]/B[i]

t /= 2

_t = 0
ans = 0

for i in range(N):
    if _t + T[i] < t:
        _t += T[i]
        ans += A[i]
    else:
        ans += (t-_t)*B[i]
        print(ans)
        break
N = int(input())
AB = [map(int, input().split()) for _ in range(N)]
A, B = [list(i) for i in zip(*AB)]

T = []
T_sum = 0
for i in range(N):
    T.append(A[i]/B[i])
    T_sum += A[i]/B[i]

ans = 0
t = 0
index = 0
while t < T_sum/2:
    ans += A[index]
    t += T[index]
    index += 1

if index != len(B) -1:
    ans += B[index] * (T_sum/2 - t)

print(ans)
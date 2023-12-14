N = int(input())
L = []
A = []
for i in range(N):
    A.append(list(map(int, input().split())))
    L.append(A[i][0])
    A[i].pop(0)

ans = []
ans_l = []
for i in range(N):
    if L[i] in ans_l:
        if A[i] in ans:
            continue
        else:
            ans.append(A[i])
            ans_l.append(L[i])
    else:
        ans.append(A[i])
        ans_l.append(L[i])

print(len(ans))
# ばかみたいに難しかった

N,M = map(int,input().split())
K = []
A = []

for i in range(M):
    K.append(int(input()))
    A.append(list(map(int, input().split())))

for k in range(N):
    for i in range(M):
        for j in range(M):
            if(A[i][0] == A[j][0]):
                A[i].pop(0)
                A[j].pop(0)
                break
        else:
            continue
        break


X = input()
N = int(input())
S = []
for _ in range(N):
    S.append(input())

D = {}
for i in range(len(X)):
    D[chr(i+97)] = X[i]

A = []
for s in S:
    a = ""
    for _s in s:
        a += D[_s]
    A.append(a)

A.sort()
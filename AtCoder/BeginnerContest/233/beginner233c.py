N, X = map(int, input().split())
L = []
a = []
for i in range(N):
    inputList = list(map(int, input().split()))
    L.append(inputList[0])
    a.append(inputList[1:])

pro = [1]

for i in range(N):
    pro2 = []
    for j in range(L[i]):
        for p in pro:
            pro2.append(p*a[i][j])
    pro = pro2

print(pro.count(X))
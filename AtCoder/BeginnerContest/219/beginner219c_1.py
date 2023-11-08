X = input()
N = int(input())
S = []
for _ in range(N):
    S.append(input())

SN = []
for i in range(N):
    SN.append("")
    for a in S[i]:
        b = X.find(a)
        if b < 10:
            SN[i] += "0" + str(b) # 多次元配列でも比較できたからこのあたりが不必要だった！！
        else:
            SN[i] += str(b)
    SN[i] = int(SN[i])

SN_copy = SN.copy()
I = []
for i in range(N):
    a = min(SN)
    I.append(SN_copy.index(a))
    SN.remove(a)

for i in I:
    print(S[i])
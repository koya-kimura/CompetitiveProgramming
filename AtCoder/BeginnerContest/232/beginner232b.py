S = input()
T = input()
L = len(S)

l = []
r = []

for i in range(L):
    s = ord(S[i])
    t = ord(T[i])

    a = s - t if s < t else s + 26 - t
    l.append(a)

    b = t - s if t < s else t + 26 - s
    r.append(b)

if len(set(l)) == 1 or len(set(r)) == 1:
    print("Yes")
else:
    print("No")
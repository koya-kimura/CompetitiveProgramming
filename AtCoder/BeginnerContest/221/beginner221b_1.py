S = input()
T = input()

chr = []

for i in range(len(S)):
    if S[i] != T[i]:
        chr.append(i)

if len(chr) > 2:
    print("No")
elif len(chr) == 2:
    if abs(chr[0]-chr[1]) < 2:
        print("Yes")
    else:
        print("No")
else:
    print("Yes")
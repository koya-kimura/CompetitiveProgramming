S = input()
T = input()

if S == T:
    print("Yes")
    exit()
else:
    a = 0
    for i in range(len(S)-1):
        if set([S[i], S[i+1]]) != set([T[i], T[i+1]]) and a > 1:
            print("No")
            exit()
        else:
            a += 1

if set([S[-1], S[-2]]) != set([T[-1], T[-2]]) or set([S[0], S[1]]) != set([T[0], T[1]]):
    print("No")
else:
    print("Yes")
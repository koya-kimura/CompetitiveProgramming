N = int(input())
st = [map(str, input().split()) for _ in range(N)]
S, T = [list(i) for i in zip(*st)]

fr = False

for i in range(N):
    for j in range(N):
        if(i == j):
            continue
        if(S[i] == S[j] and T[i] == T[j]):
            print("Yes")
            exit()

print("No")
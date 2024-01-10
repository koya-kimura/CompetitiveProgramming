S, T, X = map(int, input().split())

if S <= X < T or X < T < S or T < S <= X:
    print("Yes")
else:
    print("No")
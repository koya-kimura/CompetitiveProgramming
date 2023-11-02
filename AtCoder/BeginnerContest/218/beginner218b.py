P = list(map(int, input().split()))
s = ""
for p in P:
    s += chr(96+p)
print(s)
S = []
for _ in range(3):
    S.append(input())
T = input()

result = ""
for s in T:
    result += S[int(s)-1]

print(result)
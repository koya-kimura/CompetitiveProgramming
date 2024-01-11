A, B = map(lambda x: list(reversed(x)), input().split())

for i in range(min(len(A), len(B))):
    sum = int(A[i]) + int(B[i])
    if sum >= 10:
        print("Hard")
        exit()

print("Easy")
import numpy as np

N = int(input())
S = []
T = []

for i in range(N):
    S.extend(map(str, input().split()))
for i in range(N):
    T.extend(map(str, input().split()))

S = np.array(S)
T = np.array(T)

print(S)
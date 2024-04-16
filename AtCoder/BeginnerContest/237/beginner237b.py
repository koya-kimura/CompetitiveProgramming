H, W = map(int,input().split()) 
A = [list(map(int, input().split())) for _ in range(H)]

for y in range(W):
    row_data  = []
    for x in range(H):
        row_data.append(A[x][y])
    print(*row_data)
H, W = map(int, input().split())
A = [list(map(int, input().split())) for l in range(H)]

com_i = []
for i_1 in range(H):
    for i_2 in range(i_1+1, H):
        com_i.append({"i_1":i_1, "i_2":i_2})

com_j = []
for j_1 in range(W):
    for j_2 in range(j_1+1, W):
        com_j.append({"j_1":j_1, "j_2":j_2})

for i in com_i:
    for j in com_j:
        if (A[i["i_1"]][j["j_1"]] + A[i["i_2"]][j["j_2"]]) > (A[i["i_1"]][j["j_2"]] + A[i["i_2"]][j["j_1"]]):
            print("No")
            exit()

print("Yes")
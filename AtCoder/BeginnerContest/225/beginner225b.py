N = int(input())
AB = [map(int, input().split()) for _ in range(N-1)]
A, B = [list(i) for i in zip(*AB)]
tree_num = A + B

for i in range(N):
    if i+1 in tree_num:
        # ここの計算量やばい
        tree_num.remove(i+1)
    else:
        print("No")
        exit()

if len(set(tree_num)) == 1:
    print("Yes")
else:
    print("No")

# 1個ずつ調べていけば良い前から
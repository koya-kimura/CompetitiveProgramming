N, W = map(int, input().split())
l = [list(map(int, input().split())) for l in range(N)]

l = sorted(l, reverse=True, key=lambda x: x[0])

ans = 0
w = 0
for i in range(N):
    if w + l[i][1] < W:
        ans += l[i][0] * l[i][1]
        w += l[i][1]
    else:
        ans += l[i][0] * (W - w)
        break

print(ans)
S, T = map(int, input().split("."))

# 文字列の比較は辞書順になる
if S > T:
    print('Yes')
else:
    print('No')
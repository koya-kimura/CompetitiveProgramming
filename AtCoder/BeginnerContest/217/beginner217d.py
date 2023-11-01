# むずかった〜〜〜〜〜

L, Q = map(int, input().split())
cx = [map(int, input().split()) for _ in range(Q)]
C, X = [list(i) for i in zip(*cx)]

cut_list = [L] * L
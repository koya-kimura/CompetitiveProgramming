# 公式の答えが愚直だった、反省：愚直にやる時は言われた通りの操作をひたすらfor文で全パターンやってみる
# 初期値はNoでよい
S = list(input())
T = list(input())
ans = "No"
if S == T:
    ans = "Yes"
for i in range(len(S)-1):
    S[i],S[i+1] = S[i+1],S[i]
    if S == T:
        ans = "Yes"
    S[i],S[i+1] = S[i+1],S[i]
print(ans)
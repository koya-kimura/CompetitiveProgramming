ans = ["ABC","ARC","AGC","AHC"]
for i in range(3):
    ans.remove(input()) # 改行されていたら1つずつ回る
print("".join(ans)) # ans[0]でも同じ
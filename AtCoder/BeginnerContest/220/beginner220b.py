K = int(input())
A, B = map(int, input().split())

def Base_k_to_10(x,k):
    out = 0
    for i in range(1,len(str(x))+1):
        out += int(str(x)[-i])*(k**(i-1))
    return out

print(Base_k_to_10(A,K) * Base_k_to_10(B,K))
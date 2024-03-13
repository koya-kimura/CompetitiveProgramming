t = int(input())

def calc(x):
    return x**2+2*x+3

ans = calc(calc(calc(t)+t) + calc(calc(t)))
print(ans)

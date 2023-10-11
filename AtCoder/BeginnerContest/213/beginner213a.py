A, B = map(int, input().split())

a = bin(A)[2:]
b = bin(B)[2:]

a_l = [int(x) for x in list(str(a))]
b_l = [int(x) for x in list(str(b))]

if(len(a_l) < len(b_l)):
    for i in range(len(b_l)-len(a_l)):
        a_l.insert(0, 0)
elif(len(b_l) < len(a_l)):
    for i in range(len(a_l)-len(b_l)):
        b_l.insert(0, 0)

c_l = []
k = 0
for i in b_l:
    if(i==0):
        c_l.append(a_l[k])
    if(i==1):
        c_l.append(abs(a_l[k]-1))
    k += 1

c = int("".join(map(str, c_l)))

C = int(str(c), 2)

print(C)
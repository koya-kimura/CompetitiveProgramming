N = int(input())
a = list(map(int, input().split()))

max_num = 0
sec_max_num = 0

max_index = 0
sec_max_index = 0

k = 1
for i in a:
    if(max_num < i):
        sec_max_num = max_num
        sec_max_index = max_index
        max_num = i
        max_index = k
    elif(sec_max_num < i):
        sec_max_num = i
        sec_max_index = k
    k += 1

print(sec_max_index)
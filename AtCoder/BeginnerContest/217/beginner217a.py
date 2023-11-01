input_list = input().split()

S = input_list[0]
input_list.sort()

if input_list[0] == S:
    print('Yes')
else:
    print('No')
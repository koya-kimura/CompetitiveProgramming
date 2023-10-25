import itertools

input_list = input().split()
S = input_list[0]
K = int(input_list[1])

str_list = []
word_list = []

for s in S:
    str_list.append(s)

word_list_p = list(itertools.permutations(str_list, len(str_list)))

for w in word_list_p:
    word = ''.join(w)
    word_list.append(word)

word_list.sort()

n = 1
w_p = word_list[0]
for w in word_list:
    if w_p != w:
        n += 1
    if n == K:
        print(w)
        break
    w_p = w
S = input()

arr = []
for j in range(len(S)):
    word = ""
    for i in range(len(S)):
        word += S[(j+i)%len(S)]
    arr.append(word)

arr.sort()

print(arr[0])
print(arr[-1])
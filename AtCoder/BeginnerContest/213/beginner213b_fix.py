N = int(input())
list = [s for s in map(int, input().split())]
print(list.index(sorted(list)[-2])+1)
input_list = []
for _ in range(3):
    input_list.append(str(input()))

contest_list = ['ABC', 'ARC', 'AGC', 'AHC']
for i in range(4):
    if not (contest_list[i] in input_list):
        print(contest_list[i])
        break
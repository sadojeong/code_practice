num_list = []

for i in range(9):
    num_list.append(int(input()))

max_num = max(num_list)

for i, num in enumerate(num_list, start = 1):
    if num == max_num:
        max_num_idx = i

print(max_num, max_num_idx)
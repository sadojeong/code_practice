def find_num(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return find_num(n-1) + find_num(n-2) + find_num(n-3)

to = int(input())

for i in range(to):
    num = find_num(int(input()))
    print(num)
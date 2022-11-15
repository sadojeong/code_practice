x, n = input().split()

a = input().split()

num_list = []

for i in a:
    if int(i) < int(n):
        num_list.append(i)

print((' ').join(num_list))
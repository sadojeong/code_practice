else_list = []

for i in range(10):
    else_list.append(int(input()) % 42)

else_list = list(set(else_list))

print(len(else_list))
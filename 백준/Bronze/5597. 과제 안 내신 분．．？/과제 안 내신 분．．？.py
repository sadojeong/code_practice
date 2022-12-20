import sys

li = []

for i in range(1,31):
    li.append(i)

for j in range(28):
    v = int(sys.stdin.readline())
    li.remove(v)

print(min(li))
print(max(li))
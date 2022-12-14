import sys

nums = []
mul = 1

for i in range(3):
    v = int(sys.stdin.readline())
    nums.append(v)
    mul *= v

for i in range(10):
    print(str(mul).count(str(i)))
import sys

li = [1, 2, 6, 24, 120]

def find_num(n):
    sum = 0
    for i in range(len(n)):
        sum += int(n[i]) * li[len(n)-i-1]
    print(sum)

n=input()
while n != '0':
    find_num(n)
    n=sys.stdin.readline().strip()
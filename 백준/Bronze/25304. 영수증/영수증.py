total = int(input())
a = int(input()
)
sum1 = 0

for i in range(a):
    pr, qu = input().split()
    sum1 += int(pr) * int(qu)

if total == sum1:
    print('Yes')
else:
    print('No')
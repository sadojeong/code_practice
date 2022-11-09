n = int(input())

for i in range(n):
    a,b = input().split()
    sum1 = int(a) + int(b)
    print(f'Case #{i+1}: {a} + {b} = {sum1}')
def find_code(m):
    if m.isdecimal():
        return ord(m) - 48
    return ord(m)- 55

def find_num(n, s):
    sum = 0

    for i in range(len(n)):
        sum += find_code(n[i])*(int(s)**(len(n)-i-1))

    print(sum)

n, s = input().split()
find_num(n,s)
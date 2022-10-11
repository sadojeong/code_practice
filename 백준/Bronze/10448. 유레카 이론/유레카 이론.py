trinum_list = [int(n*(n+1)/2) for n in range(46)]

def check(n):
    for i in range(1,46):
        for j in range(i,46):
            for k in range(j,46):
                if trinum_list[i] + trinum_list[j] + trinum_list[k] == n:
                    return 1
    return 0 

for _ in range(int(input())):
    print(check(int(input())))
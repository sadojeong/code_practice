def solution(n):
    s = 1
    count = 0

    while True:
        if sum(range(0,s+1)) > n:
            break
        else:
            s += 1

    for i in range(1, s):
        if (n - sum(range(0, i))) % i == 0:
            count += 1
    return count
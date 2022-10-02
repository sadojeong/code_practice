def solution(n):
    count = str(bin(n)).count('1')

    while 1:
        n = n + 1
        if str(bin(n)).count('1') == count:
            break
            
    return n

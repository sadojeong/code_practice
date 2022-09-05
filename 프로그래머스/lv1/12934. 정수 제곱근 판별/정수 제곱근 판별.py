import math

def solution(n):
    sqr = math.sqrt(n)
    if sqr == int(sqr):
        return (sqr+1)**2
    return -1

print(solution(9))
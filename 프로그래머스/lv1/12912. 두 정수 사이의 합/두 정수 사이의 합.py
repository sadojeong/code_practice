def solution(a, b):
    if a > b:
        answer = sum(range(b,a+1))
    elif b > a:
        answer = sum(range(a,b+1))
    else:
        answer = a
    return answer
def solution(brown, yellow):
    answer = []
    sum_ = int((brown - 4) /2)
    mul = yellow
    
    for i in range(sum_):
        a, b = max(i, sum_ - i), min(i, sum_ - i)
        if a * b == mul:
            return [a+2, b+2]
def solution(k, m, score):
    score.sort(reverse=True)
    sum = 0 

    for i in range(1, (len(score) // m) + 1):
        sum += score[(i*m-1)] * m
        
    return sum
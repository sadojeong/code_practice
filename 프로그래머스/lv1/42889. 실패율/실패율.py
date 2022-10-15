from collections import Counter

def solution(N, stages):
    count = Counter(stages)

    cha = len(stages)
    li1 = list()

    for i in range(1, N+1):
        if count[i] > 0:
            fail_per = count[i] / cha
        else:
            fail_per = 0
        li1.append([i, fail_per])
        cha -= count[i]

    sorted_li = sorted(li1, key = lambda x:x[1], reverse = True)
    answer = [x[0] for x in sorted_li]
    
    return answer
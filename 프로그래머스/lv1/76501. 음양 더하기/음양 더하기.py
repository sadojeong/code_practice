def solution(absolutes, signs):
    li1 = []
    for i, n in enumerate(absolutes):
        if signs[i]:
            li1. append(n)
        else:
            li1. append(-n)
    return sum(li1)
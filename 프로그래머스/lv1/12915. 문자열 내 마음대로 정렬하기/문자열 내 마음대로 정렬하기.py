def solution(strings, n):
    li1 = []
    answer = []
    for string in strings:
        li1.append(string[n])

    li1.sort()

    for wo in li1:
        li2 = []
        for string in strings:
            if wo == string[n]:
                li2.append(string)
        li2.sort()
        for wo2 in li2:
            if wo2 not in answer:
                answer.append(wo2)
    return answer
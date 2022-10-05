import math

def solution(n, words):
    box = [words[0]]

    count = 1

    for word in words[1:]:
        count += 1
        if box[-1][-1] == word[0] and word not in box:
            box.append(word)
        else:
            break
            
    if len(words) == len(box):
        return [0,0]
    else:
        return [(n if count % n == 0 else count % n), math.ceil(count / n)]

    return answer
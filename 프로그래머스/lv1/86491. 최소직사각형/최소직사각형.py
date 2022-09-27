def solution(sizes):
    length1 = []
    length2 = []
    for size in sizes:
        length1.append(max(size[0],size[1]))
        length2.append(min(size[0],size[1]))

    return max(length1)*max(length2)
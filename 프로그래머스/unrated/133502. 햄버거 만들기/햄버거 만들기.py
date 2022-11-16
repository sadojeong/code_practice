def solution(ingredient):
    stack = []
    count = 0
    for i in ingredient:
        stack.append(i)
        if stack[-4:] == [1, 2, 3, 1]:
            count += 1
            for i in range(4):
                stack.pop()
    return count
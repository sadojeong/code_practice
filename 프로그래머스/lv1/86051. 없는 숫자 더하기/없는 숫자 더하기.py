def solution(numbers):
    return sum([i if i not in numbers else 0 for i in range(10)])
def solution(s):
    li = list(s)
    for i in range(len(li)):
        if i == 0 and li[i].isalpha():
            li[i] = li[i].upper()
        elif li[i].isalpha() and li[i-1] == ' ':
            li[i] = li[i].upper()
        else:
            li[i] = li[i].lower()
    return ''.join(li)
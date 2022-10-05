def balanced(ss):
    stack = 0
    for s in ss:
        if s == '(':
            stack += 1
        else:
            stack -= 1
        if stack < 0:
            return False
    return True

def reverse_(ss):
    new = ''
    for s in ss:
        if s =='(':
            new += ')'
        else:
            new += '('
    return new

def split_point(ss):
    stack = 0
    for i, s in enumerate(ss):
        if s == '(':
            stack += 1
        else:
            stack -= 1
        if stack == 0:
            return i

def solution(ss):
    answer = ''
    if ss == '':
        return ''
    else:
        u = ss[:split_point(ss)+1]
        v = ss[split_point(ss)+1:]
        if balanced(u):
            return u + solution(v)
        else:
            answer += '('
            answer += solution(v)
            answer += ')'
            return answer + reverse_(u[1:-1])
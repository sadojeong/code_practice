def solution(s):
    if s.isdigit():
        return(int(s))
    elif s.startswith('+'):
        return int(s.strip('+'))
    return int(s.strip('-')) * -1
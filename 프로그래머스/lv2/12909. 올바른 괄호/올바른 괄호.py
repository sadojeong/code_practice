def solution(s):
    opencount, closecount = (0,0)
    
    if s.startswith('(') and s.endswith(')') and (s.count('(') == s.count(')')):
        for i in range(len(s)):
            if s[i] == '(':
                opencount += 1
            else:
                closecount += 1
            if closecount > opencount:
                return False
        return True
    return False
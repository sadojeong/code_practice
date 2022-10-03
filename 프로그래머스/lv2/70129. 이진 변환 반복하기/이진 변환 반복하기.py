def solution(s):
    count = 0
    zero_count = 0
    
    while 1:
        count += 1
        zero_count += s.count('0')
        s = s.replace('0', '')
        s = str(bin(len(s)))[2:]
        if s == '1':
            break
    
    return [count,zero_count]
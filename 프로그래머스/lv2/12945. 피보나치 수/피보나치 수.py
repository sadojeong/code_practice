def solution(n):
    f_list = [0,1]
    
    for i in range(2, n+1):
        f_list.append(f_list[i-2] + f_list[i-1])
        
    return f_list[-1] % 1234567
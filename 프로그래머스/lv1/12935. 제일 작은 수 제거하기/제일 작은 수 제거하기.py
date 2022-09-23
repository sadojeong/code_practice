def solution(arr):
    if len(arr) == 1 :
        return [-1]
    arr2 = []
    
    min_num = min(arr)
    
    for num in arr:
        if num != min_num:
            arr2.append(num)     
        
    return arr2
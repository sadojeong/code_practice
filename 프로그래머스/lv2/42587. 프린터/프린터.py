def solution(priorities, location):
    answer = 0    
    while (priorities):
        if location == 0:   
            if priorities[0] < max(priorities):  
                priorities.append(priorities.pop(0)) 
                location = len(priorities) - 1  
            else:   
                return answer + 1
        else:
            if priorities[0] < max(priorities):  
                priorities.append(priorities.pop(0))   
            else:
                priorities.pop(0) 
                answer += 1 
            location -= 1       
    return answer
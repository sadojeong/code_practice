def solution(nums):
    sum_list = []
    
    for i in range(0,len(nums)-2):
        for j in range(i+1 , len(nums)-1):
            for k in range(j+1, len(nums)):
                sum_list.append(nums[i] + nums[j] + nums[k])

    answer = 0

    for num in sum_list:
        count = 0
        for i in range(2,num):
            if num % i == 0:
                count += 1
                continue  
        if count == 0:
            answer +=1
            
    return answer
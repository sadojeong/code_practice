def find_len_divisors(n, lim, alter):
    li = []
    for i in range(1, int(n**(1/2)) + 1):
        if n % i == 0:
            if i**2 != n:
                li.append(i)
                li.append(n/i)
            else:
                li.append(i)

    if len(li) > lim:
        return alter
    return len(li)

def solution(number, limit, power):
    answer = 0

    for i in range(1, number+1):
        answer += find_len_divisors(i, limit, power)
        
    return answer
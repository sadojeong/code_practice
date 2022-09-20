def bin_(a, n):
    return '0'* (n-len(bin(a).replace('0b', ''))) + str(bin(a).replace('0b', ''))

def solution(n, arr1, arr2):
    answer = []
    arr1_bin = []
    arr2_bin = []
    for i in range(n):
        arr1_bin.append(bin_(arr1[i], n))
        arr2_bin.append(bin_(arr2[i], n))
        
    for j in range(n):
        temp_string = ''
        for k in range(n):
            if arr1_bin[j][k] == '1' or arr2_bin[j][k] == '1':
                temp_string += '#'
            else:
                temp_string += ' '
        answer.append(temp_string)
    return answer
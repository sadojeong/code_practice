import sys

v = int(sys.stdin.readline())

def check_value(index, string):
    value = 1
    plus = 1
    while True:
        if index+plus < len(string):
            if string[index+plus] == "O":
                value += 1
                plus += 1
            else:
                break
        else:
            return value
    return value

for k in range(v):
    str1 = sys.stdin.readline()[::-1]
    num_sum = 0
    for i in range(len(str1)):
        if str1[i] == "O":
            num_sum += check_value(i, str1)

    print(num_sum)
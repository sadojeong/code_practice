input_numbers = list(map(int, input().split()))

a = input_numbers[0]
b = input_numbers[1]
c = input_numbers[2]

print((a+b)%c)
print(((a%c)+(b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)
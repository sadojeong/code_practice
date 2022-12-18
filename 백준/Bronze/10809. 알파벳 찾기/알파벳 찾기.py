string = input()

for i in range(26):
    alp = chr(97+i)
    print(string.find(alp), end=" ")
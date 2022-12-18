k = int(input())

for i in range(k):
    n, string = input().split()
    for j in range(len(string)):
        print(string[j]*int(n), end="")
    print("")
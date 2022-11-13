while True:
    a, b = input().split()
    a, b = int(a), int(b)

    if (a, b) ==  (0, 0):
        break
        
    print(a + b)
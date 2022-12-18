num_dict = {
    2 : "ABC",
    3 : "DEF",
    4 : "GHI",
    5 : "JKL",
    6 : "MNO",
    7 : "PQRS",
    8 : "TUV",
    9 : "WXYZ",
}

word = input()
answer = 0

for k ,v in num_dict.items():
    for w in word:
        if w in v:
            answer += k +1

print(answer)
alpha_list = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

word = input()

for alpha in alpha_list:
    word = word.replace(alpha, "*")

print(len(word))
word = input().upper()

li = []

for i in range(26):
    alp = chr(65+i)
    li.append(word.count(alp))

max_num = max(li)

if li.count(max_num) > 1:
    print("?")
else:
    print(chr(li.index(max_num)+65))
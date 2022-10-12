from sys import stdin
from collections import Counter

n = stdin.readline().rstrip()
card = list(map(int,stdin.readline().split()))
m = stdin.readline().rstrip()
test = list(map(int,stdin.readline().split()))

counter = Counter(card)

for num in test:
    if num in counter:
        print(counter[num], end = ' ')
    else:
        print(0, end = ' ')

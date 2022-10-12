n , k = map(int, input().split())
li = list(range(1,n+1))

p = 0
ans = []

for i in range(n):
    p += k-1
    p %= len(li)
    ans.append(li.pop(p))

ans = f"<{', '.join(map(str, ans))}>"
print(ans)
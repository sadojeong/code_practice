h,m = map(int, input().split())

if m >= 45:
  print(str(h)+" "+str(m-45))
elif h == 0:
  print("23 "+str(m+15))
else:
  print(str(h-1)+" "+str(m+15))
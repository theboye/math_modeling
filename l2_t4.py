a = int(input())
b = 1
c = 2
if a == 1:
  print(1)
elif a == 2:
  print(b , b)
else:
  print(b , b , c ,end=' ')
  for i in range(3 , a+1):
    print(b+c , end=' ')
    e = b
    b = c
    c = e + b
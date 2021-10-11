a = int(input())
b = int(input())
if b == 0:
  print('Нельзя делить на ноль')
  exit()
c = a % b
d = a // b
if a % b == 0:
  print (f'a делится на b нацело, частное={d}')
else:
  print(f'a делится на b не нацело, остаток = {c}, частное={d}')

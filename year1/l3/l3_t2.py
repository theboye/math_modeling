a,b,c = int(input()), int(input()), int(input())
d = max(a,b,c)
z = float()
if d == a and d < b + c:
    z ='YES'
else:
    if d == b and d < a+c:
        z = 'YES'
    else:
        if d == c and d < a+b:
            z = 'YES'
        else:
            z = 'NO'
if z in ('YES') :
  if a == b:
      if b == c:
          print('Равносторонний')
      else:
          print('Равнобедренный')
  elif b == c:
      print('Равнобедренный')
  elif a == c:
    print('Равнобедренный')
  else:
    print('Разносторонний')
else:
  print('NO')
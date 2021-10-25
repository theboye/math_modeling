print('Введите первое число, множитель, кол-во чисел')
b1 = int(input())
q = int(input())
n = int(input())
print('')
print('Пасиба, вот числа')
z = 0
while z < n:
  print (b1 * q**z ,end=' ') 
  z = z + 1

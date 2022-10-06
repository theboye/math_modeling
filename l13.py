'''
a = range(0,10,2)
print(a)
print(type(a))
print(a[3])
a = 'Good'
for i in range(1,10,1):
  if len(a) > i:
    print(a[i] + '  - bad')
  else:
    print(f'{i}'  + ' - good')
''''''
def func(*args,**kwargs):
  x = 6* args[1] - kwargs['obj3']
  return x

print(func(1,100,3,4,5,6,obj3=6,obj7=69420))
''''''
import random
import time
#print(random.random())
a = time.time()
print(a)
print(a/60/60/24/30.5/12)
#help(time)
#print(time.asctime(a))
'''
from datetime import datetime as dt
import time

#a = dt.now()

def decorator(func):
    def wrapped(*args, **kwargs):
        a = dt.now()
        result = func(*args, **kwargs)
        b = dt.now()
        print(b-a)
        return result
    return wrapped
  	
@decorator
def boba(num):
  l = []
  for i in range(1,num):
    l.append(i)
  return l
 
boba(10000)



	
@decorator
def biba(num):
  l =[x for x in range(1,num)]
  return l
  


biba(10000)
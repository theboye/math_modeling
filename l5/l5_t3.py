#(mv**2)/2
x = 0
from l4_t1 import g
m,h,v = float(input()),float(input()),float(input())
EK = ((m*v)**2)/2
EP = m*g*h
def energy(x):
  x = 0
  x = EK + EP
  return x
print (energy(x))
from math import sqrt, tan , cos, pi
#import math
from l4_t1 import G, k, e, g, h
b = 30
a = pi / 3
H = 100
V = sqrt((g*H*(tan(b)**2))/(2*(cos(a)**2)*(1-tan(b)*tan(a))))
#v = math.sqrt((g * h * (math.tan(b)** 2)) / (2 * (math.cos(a)** 2) * (1 - math.tan(b) * math.tan(a))))
print (V)

t = 200
E = 300
N = (2/(sqrt(pi))) * (h/((k*t)**3/2)) * (e**(-E/(k*t))) *  E**(t/2)
print(N)
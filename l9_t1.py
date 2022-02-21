#Метеорит, находящийся под влиянием земного притяжения, из состояния покоя начинает прямолинейно падать на Землю с высоты h. Определите закон изменения скорости метеорита по мере его приближения к поверхности Земли и определите скорость его столкновения с нашей планетой.

import math
import numpy
from scipy import odeint
import matplotlib as plt

R = 6371
m1 = int(input())
M = 5.972 * 10**24
h0 = int(input())
h = numpy.arrange(0,25,0.1)
g  = 9,80665
G = (m1 * g * (h0 + R) **2) / m1 *M
def meteorite(v,h):
    v = (2 * (m1 * g * (h0+R) **2)/  m1 * M )*h
    dvdh = 
    return dvdh
solve = odeint(meteor,G,h)

plt.plot(t,solve[:,0])
plt.show()
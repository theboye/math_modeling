#Ускорение локомотива , начальная скорость которого равна v0, прямо пропорционально силе тяги F и обратно пропорционально массе поезда m. Сила тяги локомотива F(t) = b — k v(t), где v(t) — скорость локомотива в момент t, а b и k — постоянные величины. Определить зависимость силы тяги локомотива от времени t.
# V_0 = F
# F(t) = b - k * V(t)
# Fтяги = ma
#  b , k = const
# ma = b-k*V 
# a = (b - k *V) / m
# a это зависимость v От t
# dv / dt = (b - k *V) / m

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

b = 100000
k = 10005
m = 15 * 10 ** 3
V_0 = 0

t = np.arange(0,10,0.02)
def radio_function(V_0,t):
  dndt = (b - k*V_0) / m
  return dndt 

solve_Bi = odeint(radio_function , V_0,t)
plt.plot(t,solve_Bi[:,0],label='amogus')
plt.xlabel('Я, СКОРОСТЬ')
plt.show()

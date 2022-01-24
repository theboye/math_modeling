# На материальную точку массы m действует постоянная сила, сообщающая точке ускорение a0. Окружающая среда оказывает движущейся точке сопротивление, пропорциональное квадрату скорости движения со временем, коэффициент сопротивления равен γ. Определите закон изменения скорости со временем, если в начальный момент времени точка находилась в покое.
#dv / dt = (V^2 * Y + F) / m
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

m = 5

F =200

Y = - 1.8

V_0 = 10

t = np.arange(0,100,0.4)
def radio_function(V_0,t):
  dvdt = (V_0**2 * Y + F) / m
  return dvdt 

solve_Bi = odeint(radio_function , V_0,t)
plt.plot(t,solve_Bi[:,0],label='amogus')
plt.xlabel('Я, СКОРОСТЬ')
plt.show()

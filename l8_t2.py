#Предприятие инвестирует в новое производство денежные средства, причем инвестиции уменьшаются со скоростью, прямо пропорциональной инвестируемым в данный момент времени средствам с коэффициентом пропорциональности 0,08. Найти закон изменения инвестиций со временем и объем инвестиций за 4 года, если в начальный момент времени инвестиции составили 1000 денежных единиц.
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#ds/dt = -0.08*s*t

s_0 = 1000

k = -0.08


t = np.arange(0,10,1)
def radio_function(s_0,t):
  dndt = k*t*s_0
  return dndt 


solve_Bi = odeint(radio_function, s_0,t)
plt.plot(t,solve_Bi[:,0],label='amogus')
plt.xlabel('время')
plt.show()



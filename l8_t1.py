#Из эксперимента известно, что скорость размножения бактерий при достаточном запасе пищи пропорциональна их количеству. Определите закон увеличения бактерий и время, спустя которое их станет в 10 раз больше, относительно начального количества.
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
#  dn
# ———— = kn(t)
#  dt
k = 2
n = 1
t = np.arange(0,10,0.3)
def radio_function(n,t):
  dndt = k * n
  return dndt 

solve_Bi = odeint(radio_function, n,t)
plt.plot(t,solve_Bi[:,0],label='amogus')
plt.xlabel('время')
plt.show()
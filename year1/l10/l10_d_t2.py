import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0.001,5,0.001)

def diff_func(fff,arg):
  t = arg
  y,a = fff
  dydt = a
  dadt = (a**2 - ((3* y**2)/np.sqrt(t)))/ y

  
  return dydt, dadt



y0 = 1
dy0dt = 0
m0 = y0,dy0dt


sol = odeint(diff_func,m0,t)

plt.plot(t, sol[:,0])
plt.plot(t, sol[:,1])
plt.show()
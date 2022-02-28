import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(-1,1,0.001)

def diff_func(fff,arg):
  t = arg
  y,p = fff
  
  dydx = p
  dpdx = (4 * t**2 + 0.5) * (y/t**2) - p/t

  
  return dydx, dpdx



y0 = 3
dy0dt = 0
m0 = y0,dy0dt


sol = odeint(diff_func,m0,t)

plt.plot(t, sol[:,0])
plt.plot(t, sol[:,1])
plt.show()
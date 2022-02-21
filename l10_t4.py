import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(-5,5,0.001)

def diff_func(m,t):
  y,x = m
  dy_dt = x - 4*y
  dx_dt = -5 * y

  
  return dy_dt, dx_dt


dy_dt0 = -1
y0 = 4
m0 = y0,dy_dt0


sol = odeint(diff_func,m0,t)

plt.plot(t, sol[:,0])
plt.plot(t, sol[:,1])
plt.show()
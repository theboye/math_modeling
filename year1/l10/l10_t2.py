import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(-1,1,0.0001)


def diff_func(m,t):
  e= np.exp(3*t)
  e1 = np.exp(t)
  x,y = m
  dx_dt = 3*x -2*y +(e/(e1+1))
  dy_dt = x-(e/(e1+1))
  
  return dx_dt,dy_dt
y0 = -7
x0 = 5
m0 = x0,y0

sol = odeint(diff_func,m0,t)
plt.plot(t, sol[:,0])

plt.plot(t, sol[:,1])
plt.show()
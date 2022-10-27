import numpy as np
import l4_t1 as lol

g = lol.g
time_start = 0
time_stop = 5
x0 = 10
y0 = 5
v0x = 2
v0y = 15
steps = 10

step_rn = 0

coords = np.zeros((steps,3))
for t in np.linspace(time_start,time_stop,steps):
  x = x0 + v0x*t
  y = y0 + v0y * t - (g * t**2)/2
  coords[step_rn,0] = t
  coords[step_rn,1] = x
  coords[step_rn,2] = y
  step_rn = step_rn + 1 
print(coords)
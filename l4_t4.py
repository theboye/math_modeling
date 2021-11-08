import numpy as np
import math
n  = 4
m = 5

arr = np.zeros((n,m))
#  print(f"element:[{i},{j}] = {value}")
for (i,j), value in np.ndenumerate(arr):

  result = math.sin(n*(i+1) + m*(j+1))
  if (result < 0):
    result = 0
  arr[i,j] = result
print(arr)

arr[:,[2,0]] = arr[: , [0,2]]
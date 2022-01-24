n = int(input())
def fibb(n):
  n1 = 1
  n2 = 1
  for i in range(n):
    n2 += n1
    n1,n2 = n2,n1
    x = n2
  return x  
print(fibb(n))
a = int(input())
factorednumbers = []
for i in range(1, a):
  factors = []
  for t in range(1, i):
    if i % t == 0:
      factors.append(t)
  if sum(factors) == i:
    factorednumbers.append(i)
print(factorednumbers)



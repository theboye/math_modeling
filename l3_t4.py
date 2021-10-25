x = int(input())
factors = []
for t in range(1, x + 1):
  if x % t == 0:
    factors.append(t)
print(factors)
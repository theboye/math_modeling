from itertools import product
"""
print("x y z w")
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if not((x and not(y)) or (y == z) or w):
                    print(f"Ответ: {x}, {y}, {z}, {w}")
"""
"""
for i in range(1,1000):
    b = bin(i)[2:]
    b += b[-1]
    a = sum([int(x) for x in b])
    ost = a%2
    b+= str(ost)
    if int(b,2) > 105:
        print(int(b,2))
        break
"""
"""
for i,x in enumerate(product('АИОУЭ',repeat = 4)):
    print(i+1,x)
"""
# 01 > 210
# 02 > 3101 > 31210
# 03 > 2012 > 22102 > 2213101 > 22131210
# единицы x + 2y + 3z = 70
# двойки  x + y + 3z = 56
# тройки  y + z = 23
# т.е. z = 9    y = 14    x = 15
# 9+14+15+2 = 40
"""
x = 9**8+ 3**5 -2
s = ''
while x != 0: 
    s += str(x % 3)
    x //= 3
s = s[::-1]
print(s.count("2"))
"""
"""
for A in range(10**3):
    for x in (10**2):
        for y in range(10**2):
            if (x * y < 121) or (y > A) or (x >= A):
"""
"""
def f(n):
    if n ==1:
        return 1
    if n == 2:
        return 1
    if n > 2:
        return f(n-2)*n
print(f(7))
""" """
with open('17.txt','r') as file:
    w = [int(x)for x in file]

k = 0
mx = 0
for i in range(0,len(w)-1):
    for j in range(i+1,len(w)):
        d = abc(w[i]-w[j])
        if d%45 == 0 and(w[i]%18 == 0 or w[j]%18==0):
            k+=1
            if d > mx:
                mx = d
print(k,mx)
"""
#ID процесса B	Время выполнения процесса B (мс)	ID процесса (ов) A	time
#1	4	0	4
#2	5	0	5
#3	8	1;2	13
#4	2	3	15
#5	12	2	17
#6	4	0	4
#7	7	3;4	22
#8	3	2;3	16
#9	8	0	8
#10	3	5;6	20
#11	2	3;6	15
#12	7	2;7	29
#13	2	0	2
#14	4	6;9	12
#15	11	3	11
"""
разбирал на листочке
""" """
with open('zadanie24_2','r') as f:
    w = f.readline().strip()
mx = 0
k = 0
for i in range(len(w),3):
    if w[i] + w[i+1] + w[i+2] == 'LDR':
        k+=1
    else:
        if mx< k:
            mx = k*3
        k = 0
print(mx)
"""

#Создать функцию, строящую графики кривых второго порядка, заданных явно:
#Парабола
#Гипербола
import matplotlib.pyplot as plt
import numpy

Xa = int(input("Отрицательное пжпжпжпжп:"))
Xb = int(input())
N = int(input())
a = int(input())
b = int(input())
c = int(input())
k = int(input('Неравное нулю:'))

def parabola(a, b, c, k, Xa, Xb, N, title = 'Парабола и Гипербола'):
  x = numpy.linspace(Xa, Xb, N)
  y = a * x ** 2 + b * x + c

  plt.plot(x, y, label = 'Парабола, Finally!')
  plt.xlabel('X')
  plt.ylabel('Y')
  plt.title(title)
  plt.legend()
  plt.show()

#parabola(a, b, c, k, Xa, Xb, N)

def hyperbola(k, Xa, Xb, title = 'Гипербола'):
  x1 = numpy.linspace(Xa,Xb, N)
  y1 = k / x1

  y1  = y1[y1 == 0]
  x1 = x1[y1 == 0]

  plt.plot(x1, y1, label = 'Гипербола, Ура!')
  plt.xlabel('O(X)')
  plt.ylabel('O(Y)')
  plt.title(title)
  plt.legend()
  plt.show()
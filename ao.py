import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Определяем переменную величину
frames = 365
seconds_in_year = 365 * 24 * 60 * 60
years = 2
t = np.linspace(0, years*seconds_in_year, frames)

# Определяем функцию для системы диф. уравнений

def move_func(s, t):
    (x1, v_x1, y1, v_y1) = s
  
    dxdt1 = v_x1
    dv_xdt1 = - G * m * x1 / (x1**2 + y1**2)**1.5
    dydt1 = v_y1
    dv_ydt1 = - G * m * y1 / (x1**2 + y1**2)**1.5

    return (dxdt1, dv_xdt1, dydt1, dv_ydt1)
    
# Определяем начальные значения и параметры
    
G = 6.67 * 10**(-11)
m = (5.9722 + 0.0006) * 10**24



#Шпутник
x10 = 0
v_x10 = 11300
y10 = -35786
v_y10 = 0

s0 = (x10, v_x10, y10, v_y10)

# Решаем систему диф. уравнений
def solve_func(i, key):
    sol = odeint(move_func, s0, t)
    if key == 'point':
        x1 = sol[i, 0]
        y1 = sol[i, 2]

    else:
        x1 = sol[:i, 0]
        y1 = sol[:i, 2]

    return ((x1, y1))

# Строим решение в виде графика и анимируем
fig, ax = plt.subplots()

ball1, = plt.plot([], [], 'o', color='brown')
ball_line1, = plt.plot([], [], '-', color='brown')



plt.plot([0], [0], 'o', color='orange', ms=20)

def animate(i):
    ball1.set_data(solve_func(i, 'point')[0])
    ball_line1.set_data(solve_func(i, 'line')[0])

    
ani = FuncAnimation(fig,
                    animate,
                    frames=frames,
                    interval=30)

plt.axis('equal')
edge = 6 * x10
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

plt.show()
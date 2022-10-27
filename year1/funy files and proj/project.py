import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('default')

b = int(input('укажи массу(в кг):  '))

figure = plt.figure()
axis = plt.axes(xlim=(0, 4), ylim=(-2, 2))
line, = axis.plot([], [], lw=3)

def init():
    line.set_data([], [])
    return line,
def animate(i):
    x = np.linspace(0, 4, 1500)
    y = np.sin(b * np.pi * (x - 0.001 * i))
    line.set_data(x, y)
    return line,

anim = FuncAnimation(figure, animate, init_func=init,
                               frames=520, interval=20, blit=True)


anim.save('test 1.gif', writer='imagemagick')
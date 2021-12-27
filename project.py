import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.use('default')


figure = plt.figure()
axis = plt.axes(xlim=(0, 3), ylim=(-2, 2))
line, = axis.plot([], [], lw=3)

def init():
    line.set_data([], [])
    return line,
def animate(i):
    x = np.linspace(0, 4, 1500)
    y = np.sin(7 * np.pi * (x - 0.005 * i))
    line.set_data(x, y)
    return line,

anim = FuncAnimation(figure, animate, init_func=init,
                               frames=520, interval=20, blit=True)


anim.save('wave.gif', writer='imagemagick')
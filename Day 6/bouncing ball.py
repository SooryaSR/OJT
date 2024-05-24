import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


g = 9.81 
e = 0.8 
dt = 0.01 
initial_height = 10 
y = initial_height
v = 0

y_positions = [y]

while len(y_positions) < 1000:

    v -= g * dt
    y += v * dt

    if y <= 0: 
        y = 0
        v = -e * v 

    y_positions.append(y)

fig, ax = plt.subplots()
ax.set_xlim(0, 2)
ax.set_ylim(0, initial_height + 2)
ball, = ax.plot([], [], 'bo', markersize=20)

def init():
    ball.set_data([], [])
    return ball,

def animate(i):
    ball.set_data(1, y_positions[i])
    return ball,

ani = animation.FuncAnimation(fig, animate, init_func=init, frames=len(y_positions), interval=dt*1000, blit=True)

plt.show()
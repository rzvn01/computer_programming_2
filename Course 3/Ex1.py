import cmath

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm


def rb(x1, x2):
    return 100 * (x2 - x1 ** 2) ** 2 + (1 - x1) ** 2


n = 1000
x1 = np.linspace(start=-1.5, stop=2, num=n)
x2 = np.linspace(start=-0.5, stop=3, num=n)

F = np.zeros((n, n))

for i in range(n):
    for k in range(n):
        F[i][k] = rb(x1[i], x2[k])

fig = plt.figure()
ax = plt.axes(projection='3d')
surface = ax.plot_surface(x1, x2, F, cmap=cm.inferno)
ax.set_title('Rosenbrock Function')
plt.show()

x = np.zeros(4)
y = np.zeros(4)

tau = 2 / (1 + cmath.sqrt(5))

if y[2] > y[1]:
    x[2:4] = x[1:3]
    y[2:4] = y[1:3]
    x[1] = (1 - tau) * (x[3] - x[0]) + x[0]
    y[1] = rb(1, x[1])
else:
    x[1:3] = x[0:2]
    y[1:3] = x[0:2]
    x[2] = tau * (x[3] - x[0]) + x[0]
    y[2] = rb(1, x[2])

import matplotlib.pyplot as plt
import numpy as np
import math


def rb(x1, x2):
    return 100 * (x2 - x1 ** 2) ** 2 + (1 - x1) ** 2


n = 40
x1 = np.linspace(start=-1.5, stop=2, num=n)
x2 = np.linspace(start=-0.5, stop=3, num=n)
X1, X2 = np.meshgrid(x1, x2)
F = rb(X1, X2)
print(F)


# GOLDEN CUT
tau = 2 / (1 + math.sqrt(5))

x = [0, 1 - tau, tau, 1]
y = np.zeros(4)

xmin = -1
xmax = 2

for i in range(4):
    x[i] = x[i] * (xmax - xmin) + xmin
    y[i] = rb(1, x[i])

print(x)
print(y)

while (x[2] - x[1]) >= 0.01:
    if y[2] > y[1]:
        x[2:4] = x[1:3]
        x[1] = (1 - tau) * (x[3] - x[0]) + x[0]
        y[2:4] = y[1:3]
        y[1] = rb(1, x[1])
    else:
        x[1:3] = x[0:2]
        x[2] = tau * (x[3] - x[0]) + x[0]
        y[1:3] = x[0:2]
        y[2] = rb(1, x[2])
#
fig = plt.figure()
wf = fig.add_subplot(111, projection="3d")
wf.plot_wireframe(x1, x2, F, rstride=1, cstride=1,color="purple")
wf.set_title("Rosenbrock function")

print("\nGolden Cut Algorithm\n")
print("Minimum x_min = %f" % x[1])
print("f(x_min)= %f" % y[1])

M = 10000
x = [-1, +1]

alpha = 1e-3
h = 1e-3

g = np.zeros(2)
out = np.zeros((M, 2))

for n in range(M):
    g[0] = (rb(x[0] + h / 2, x[1]) - rb(x[0] - h / 2, x[1])) / h
    g[1] = (rb(x[0], x[1] + h / 2) - rb(x[0], x[1] - h / 2)) / h
    x = x - alpha * g
    out[n][:] = x

print("\n*** Steepest Descent Algorithm ***\n")
plt.figure(3, figsize=(6, 4))
plt.plot(np.linspace(0, M, M), out)

plt.show()

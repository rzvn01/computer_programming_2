import numpy as np
import matplotlib.pyplot as plt


def egg_holder(x, y):
    return -(y + 47) * np.sin(np.sqrt(np.abs(x / 2 + (y + 47)))) - x * np.sin(np.sqrt(np.abs(x - (y + 47))))


x = np.linspace(-512, 512, 100)
y = np.linspace(-512, 512, 100)
X, Y = np.meshgrid(x, y)
Z = egg_holder(X, Y)

# Create a 3D plot using plot_surface
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_title('Egg Holder Function - plot_surface')

# Create a 3D plot using plot_wireframe
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(X, Y, Z, cmap='viridis')
ax.set_title('Egg Holder Function - plot_wireframe')

# Create a contour plot using contourf
plt.figure(figsize=(8, 6))
contour = plt.contourf(X, Y, Z, cmap='viridis', levels=50)
plt.colorbar(contour)
plt.title('Egg Holder Function - contourf')
plt.xlabel('x')
plt.ylabel('y')

plt.show()

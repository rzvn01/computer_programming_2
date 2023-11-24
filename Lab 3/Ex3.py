import numpy as np
import matplotlib.pyplot as plt


# Define the Three-Hump Camel Function
def three_hump_camel(x, y):
    return 2 * x ** 2 - 1.05 * x ** 4 + (x ** 6) / 6 + x * y + y ** 2


# Calculate the Gradient and Hessian Matrix
def gradient(x, y):
    df_dx = 4 * x ** 3 - 4.2 * x ** 3 + x ** 5 + y
    df_dy = x + 2 * y
    return np.array([df_dx, df_dy])


def hessian(x, y):
    d2f_dx2 = 12 * x ** 2 - 12.6 * x ** 2 + 5 * x ** 4
    d2f_dy2 = 2
    d2f_dx_dy = 1
    return np.array([[d2f_dx2, d2f_dx_dy], [d2f_dx_dy, d2f_dy2]])


# Newton's Method with Convergence Tracking
def newtons_method(initial_guess, tolerance=1e-6, max_iterations=100000):
    x, y = initial_guess
    x_history, y_history = [x], [y]

    for iteration in range(max_iterations):
        grad = gradient(x, y)
        hess = hessian(x, y)
        delta = np.linalg.solve(hess, -grad)
        x += delta[0]
        y += delta[1]

        x_history.append(x)
        y_history.append(y)

        # Check convergence
        if np.linalg.norm(delta) < tolerance:
            break

    return x, y, x_history, y_history


# Different initial guess
initial_guess = [1.5, -1.5]

# Find the minimum and track convergence
result_x, result_y, x_history, y_history = newtons_method(initial_guess)

# Create a grid of x and y values for surface plotting
x_range = np.linspace(-2, 2, 400)
y_range = np.linspace(-2, 2, 400)
X, Y = np.meshgrid(x_range, y_range)
Z = three_hump_camel(X, Y)

# Plot the convergence in 3D
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
ax.plot(x_history, y_history, [three_hump_camel(x, y) for x, y in zip(x_history, y_history)], marker='o', color='red')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x, y)')
ax.set_title('Convergence of Newton\'s Method for Three-Hump Camel Function')
plt.show()

print("Minimum point (x, y):", (result_x, result_y))
print("Minimum value of the Three-Hump Camel Function:", three_hump_camel(result_x, result_y))

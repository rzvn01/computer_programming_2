import numpy as np
import matplotlib.pyplot as plt


# Function to generate a random rectangle
def generate_random_rectangle():
    x = np.random.randint(0, 51)  # Random x-coordinate in [0, 20]
    y = np.random.randint(0, 51)  # Random y-coordinate in [0, 20]
    width = np.random.randint(1, 51)  # Random width in [1, 20]
    height = np.random.randint(1, 51)  # Random height in [1, 20]
    return [x, y, width, height]


# Generate two random rectangles R1 and R2
R1 = generate_random_rectangle()
R2 = generate_random_rectangle()


while R1[2] == 0 or R1[3] == 0:
    R1 = generate_random_rectangle()

while R2[2] == 0 or R2[3] == 0:
    R2 = generate_random_rectangle()

# Create a figure and axis
fig, ax = plt.subplots()

# Plot rectangles R1 and R2 with different colors
ax.add_patch(plt.Rectangle((R1[0], R1[1]), R1[2], R1[3], color='orange', alpha=0.5, label='Rectangle 1'))
ax.add_patch(plt.Rectangle((R2[0], R2[1]), R2[2], R2[3], color='blue', alpha=0.5, label='Rectangle 2'))


ax.set_xlim(0, 50)
ax.set_ylim(0, 50)


ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Random Rectangles')
ax.legend()

plt.show()

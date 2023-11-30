import numpy as np
import matplotlib.pyplot as plt


def generate_random_rectangle():
    x = np.random.randint(0, 21)  # Random x-coordinate in [0, 20]
    y = np.random.randint(0, 21)  # Random y-coordinate in [0, 20]
    width = np.random.randint(1, 21)
    height = np.random.randint(1, 21)
    return [x, y, width, height]


def compute_central_point(rectangle):
    x = rectangle[0] + rectangle[2] / 2
    y = rectangle[1] + rectangle[3] / 2
    return [x, y]


def check_intersection(rect1, rect2):
    x1, y1, w1, h1 = rect1
    x2, y2, w2, h2 = rect2

    center1 = compute_central_point(rect1)
    center2 = compute_central_point(rect2)

    intersect = (abs(center1[0] - center2[0]) * 2 < (w1 + w2)) and (abs(center1[1] - center2[1]) * 2 < (h1 + h2))

    return intersect, center1, center2


R1 = generate_random_rectangle()
R2 = generate_random_rectangle()

while R1[2] == 0 or R1[3] == 0:
    R1 = generate_random_rectangle()

while R2[2] == 0 or R2[3] == 0:
    R2 = generate_random_rectangle()

intersection, center1, center2 = check_intersection(R1, R2)

print(f"Central point of R1: {center1}")
print(f"Central point of R2: {center2}")
print(f"Rectangles intersect: {intersection}")

fig, ax = plt.subplots()

ax.add_patch(plt.Rectangle((R1[0], R1[1]), R1[2], R1[3], color='red', alpha=0.5, label='Rectangle 1'))
ax.add_patch(plt.Rectangle((R2[0], R2[1]), R2[2], R2[3], color='blue', alpha=0.5, label='Rectangle 2'))

ax.set_xlim(0, 20)
ax.set_ylim(0, 20)

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Random Rectangles')
ax.legend()

plt.show()

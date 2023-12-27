import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Function to perform Newton-Raphson iteration
def f(z):
    return z**5 + 4*z**3 + 2*z + 7

# Constants
GRID_SIZE = 100
ITERATIONS = 1

# Create a 2D grid to store initial complex numbers
grid = np.array([[complex(x, y) for x in np.linspace(-2, 2, GRID_SIZE)] for y in np.linspace(-2, 2, GRID_SIZE)])

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

# Create an empty scatter plot
sc = ax.scatter([], [], s=1)

# Function to update the plot for each frame of the animation
def update(frame):
    global grid
    new_grid = np.copy(grid)
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            z = grid[i][j]
            for _ in range(ITERATIONS):
                z = z - f(z) / (5 * z**4 + 12 * z**2 + 2)
                new_grid[i][j] = z
    grid = new_grid
    x = np.real(grid).flatten()
    y = np.imag(grid).flatten()
    sc.set_offsets(np.column_stack((x, y)))
    return sc,

# Create the animation
ani = FuncAnimation(fig, update, frames=1, interval=2000)
plt.show()

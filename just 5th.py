import numpy as np
import matplotlib.pyplot as plt
import mplcyberpunk
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns

# Apply cyberpunk style
plt.style.use('cyberpunk')

# Constants
m = 1  # mass
F = 8  # force magnitude

# Simulation parameters
dt = 0.05  # time step
t_final = 1.75  # final time
t = np.arange(0, t_final + dt, dt)  # time array

# Initial conditions
x0, y0 = 0, 0

# Case 1: Initial velocities
v_x0_case1, v_y0_case1 = 0, 0

# Case 2: Initial velocities
v_x0_case2, v_y0_case2 = 0, 5

# Arrays to store results
x_case1 = np.zeros(len(t) + 1)
v_x_case1 = np.zeros(len(t) + 1)
y_case1 = np.zeros(len(t) + 1)
v_y_case1 = np.zeros(len(t) + 1)

x_case2 = np.zeros(len(t) + 1)
v_x_case2 = np.zeros(len(t) + 1)
y_case2 = np.zeros(len(t) + 1)
v_y_case2 = np.zeros(len(t) + 1)

# Set initial conditions
x_case1[0], v_x_case1[0] = x0, v_x0_case1
y_case1[0], v_y_case1[0] = y0, v_y0_case1

x_case2[0], v_x_case2[0] = x0, v_x0_case2
y_case2[0], v_y_case2[0] = y0, v_y0_case2

# Create figure
fig = plt.figure(figsize=(19, 11))
flare_colors = sns.color_palette("flare")
crest_colors = sns.color_palette("crest")

# Darker color variants for the dots
flare_darker = [sns.dark_palette(flare_colors[0], n_colors=1)[0]]
crest_darker = [sns.dark_palette(crest_colors[0], n_colors=1)[0]]

# Variable for dot step
dot_step = 3  # Change this to adjust how often to plot small dots

# Store small dots for plotting
small_dots_case1_y = []
small_dots_case2_y = []
small_dots_case1_x = []
small_dots_case2_x = []

# Subplot 1: xy Movement of Balls
ax1 = fig.add_axes([0.00, 0.35, 0.3, 0.3])  # [left, bottom, width, height]
ax1.grid(True)
ax1.set_aspect('equal')
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('Ball Movement - Cases 1 and 2')

# Subplots for Lagrangians
ax5 = fig.add_axes([0.25, .03, 0.7, 0.7], projection='3d')  # [left, bottom, width, height]

# Set up mesh grid for Lagrangian surfaces
Y, Ydot = np.meshgrid(np.linspace(-10, 10, 21), np.linspace(-10, 10, 21))
X, Xdot = np.meshgrid(np.linspace(-10, 10, 21), np.linspace(-10, 10, 21))

# Update positions and velocities for both cases
for frame in range(len(t)):
    # Case 1
    x_case1[frame + 1] = x_case1[frame] + v_x_case1[frame] * dt
    v_x_case1[frame + 1] = v_x_case1[frame] + (F/m - v_x_case1[frame]) * dt
    y_case1[frame + 1] = y_case1[frame] + v_y_case1[frame] * dt
    v_y_case1[frame + 1] = v_y_case1[frame]

    # Case 2
    x_case2[frame + 1] = x_case2[frame] + v_x_case2[frame] * dt
    v_x_case2[frame + 1] = v_x_case2[frame] + (F/m - v_x_case2[frame]) * dt
    y_case2[frame + 1] = y_case2[frame] + v_y_case2[frame] * dt
    v_y_case2[frame + 1] = v_y_case2[frame]

    # Clear previous plots
    ax1.cla()  # Clear only the content of the axis, not the limits
    ax5.cla()

    # Re-plot xy movement
    ax1.plot(x_case1[:frame+2], y_case1[:frame+2], color=flare_colors[0], linewidth=2, label='Case 1')
    ax1.plot(x_case2[:frame+2], y_case2[:frame+2], color=crest_colors[0], linewidth=2, label='Case 2')
    
    # Plot the current positions of the big dots
    ax1.scatter(x_case1[frame + 1], y_case1[frame + 1], color=flare_colors[2], s=100)  # Big dot for Case 1
    ax1.scatter(x_case2[frame + 1], y_case2[frame + 1], color=crest_colors[2], s=100)  # Big dot for Case 2
    
    ax1.set_xlim(-1, 10)
    ax1.set_ylim(-1, 10)
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.set_title('Ball Movement - Cases 1 and 2')
    ax1.legend(loc='upper left')

    # Case 2 - x vs xdot
    Lagrangian_case2_x = -1 * F/m * X + 0.5 * m * (Xdot - 5)**2
    ax5.plot_surface(X, Xdot, Lagrangian_case2_x, cmap='crest', alpha=0.6)

    # Update the big dot for Case 2
    ax5.scatter3D(x_case2[frame + 1], v_x_case2[frame + 1],
                   -1 * F/m * x_case2[frame + 1] + 0.5 * (v_x_case2[frame + 1] - 5)**2,
                   color=crest_colors[4], s=100, edgecolor='black', linewidth=1.5)

    # Store small dot for Case 2 if conditions are met
    if frame % dot_step == 0:
        small_dots_case2_x.append((x_case2[frame], v_x_case2[frame], 
                                 -1 * F/m * x_case2[frame] + 0.5 * (v_x_case2[frame] - 5)**2))
    
    # Plot all stored small dots for Case 2 and draw lines down to z=0
    for dot in small_dots_case2_x:
        ax5.scatter3D(dot[0], dot[1], dot[2], color=crest_darker[0], s=20)
        ax5.plot([dot[0], dot[0]], [dot[1], dot[1]], [dot[2], 0], color='white', linestyle='--', linewidth=2)

    ax5.set_title('Lagrangian - Case 2 (x vs xdot)')
    ax5.set_xlabel('x')
    ax5.set_ylabel('xdot')
    ax5.set_zlabel('Lagrangian')
    ax5.view_init(-161, -36)

    # Pause to create animation effect
    plt.pause(0.01)

plt.show()

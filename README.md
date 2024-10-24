# Lagrangian/Path of Least Action Visualization
## Introduction:
As I was teaching myself about Lagrangian Mechanics, I noticed a lack of resources providing clear visualizations for the "path of least action," instead of rough hand-drawn diagrams. This project aims to fill that gap by offering a visual simulation of two point masses subjected to forces, highlighting how Lagrangian mechanics can describe their motion.

## Problem Setup:
In this simulation, we model two 1 kg point masses starting from the same position at (0,0), each subject to a force of 8N along the x-axis. In Case 1, the particle starts at rest, and in Case 2, the particle begins with an initial upward velocity of 5 m/s. This scenario simplifies the problem of a particle on a frictionless slope: one starting from rest, and the other with an initial velocity along the slope.
The Lagrangian is defined as:
$L = T - V$
where $T$ is the kinetic energy, and $V$ is the potential energy. For our simplified setup (with no gravity), the kinetic energy is given by:
$T = \frac{1}{2}m\dot{x}^2 + \frac{1}{2}m\dot{y}^2$
and the potential energy:
$V = -\frac{F}{m}x$
where $F$ is the applied force. This resembles the potential energy for a particle moving along a frictionless slope where the potential decreases linearly with displacement in the x-direction. In the real world, the potential energy of a ball on a slope would be equal to $mgh$, but this is functionally identical to our example here, as in our case, as we move in the positive x direction, our potential energy decreases linearly.
## Visualization Breakdown:
First, on the left, we animate the positions of the two particles along the x and y axis, with the final result shown below.

<p align="center">
  <img src="https://github.com/user-attachments/assets/5946b226-7e4d-437d-a616-3c784b5ff7b2" alt="Simul" width="350"/>
</p>

For both cases, we also present two sets of animated 3D plots:

- Lagrangian vs. x-position and x-velocity
- Lagrangian vs. y-position and y-velocity

<p align="center">
  <img src="https://github.com/user-attachments/assets/e70b51ab-e5c8-4df4-9bb1-2a64ff3d2ce6" alt="fourplots" width="1000"/>
</p>

In order to gain a more intuitive understand of what is going on, let us focus our attention on the x-position and x-velocity plot for Case 2:
<p align="center">
  <img src="https://github.com/user-attachments/assets/8e913c19-02bf-4f28-8021-47425c6c08e4" alt="case_2_x" width="600"/>
</p>


The "action" is represented by the area of the surface traced out by the dashed white lines. To gain an intuition for the "path of least action," let us assume that the equation for the Lagrangian of our system is both fixed and known (In other words, the plotted surface does not change) and that we have known starting and ending x positions. We will aim to find a "path" by varying the values of velocity in order to minimize the area traced out by the dashed white lines. 


Perhaps the simplest case to imagine is velocity values that result in a straight line from our starting to ending point. However, it should be clear that this is not optimal, as, although the "length" of the path is minimized in the xy-plane, the area underneath the path is not. In the optimal case, we have a slightly longer path, but we spend a majority of the length in areas where the value of the Lagrangian is low and only a small amount of the length near areas where the value of the Lagrangian is high. 

As an additional note, our animations are actually four-dimensional, with the fourth dimension represented by the animation timestep. In reality, we are not concerned with the "length" of the path, but more explicitly, with the time our system remains in different regions of the Lagrangian. For this specific example and animation, our velocities have been intentionally chosen not to vary greatly, so analyzing the area swept out by the path length is an acceptable approximation.


The Lagrangian is independent of the y-position because the potential energy is only a function of the x-position. For each plot, the white dashed lines and small markers visualize the path of least action. This path minimizes the area under the curve, showing how the particle moves from the starting to the final position in the most efficient way, according to the Lagrangian principle.

## Code Overview:
This Python script uses matplotlib, mplcyberpunk, and seaborn to generate a dynamic visualization of the particle motion and their respective Lagrangians. It creates an animated 3D plot showing the path of least action for both cases.
### How to Run:

Install dependencies:

`pip install numpy matplotlib mplcyberpunk seaborn`

Run the script in a Python environment. The animation will display the movement of both particles over time, along with the Lagrangian surface plots.

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as mpatches

# Create new Figure with black background
f = plt.figure(facecolor='black', figsize=(9,9))

# Add a subplot with no frame
ax = plt.subplot(111, frameon=False)

# Set plot limits
ax.set_ylim(-1e9, 1e9)
ax.set_xlim(-1e9, 1e9)

# Remove tick marks on the axes
ax.set_xticks([])
ax.set_yticks([])

# Set constannt simulation parameters
dt = float(18000)      # Time step in loop
rast = 6e6    #radius of asteriod
rearth = 6e7  # Radius of the Earth

# Set asteroid's startposition, and velocity
vx = 10e2
vy = 0
x = float(0)
y = float(4e8)

# Draw Earth and asteroid using the add_patch function
earth = ax.add_patch(mpatches.Circle([0,0],radius=rearth, fill=True, color='b', ls='solid'))
ast = ax.add_patch(mpatches.Circle([x,y],radius=rast, fill=True, color='w', ls='solid'))

def step(args):
    """This function advances the animation one time step"""
    global vx, vy, x, y

# Define gravitational acceleration
    g = -6.673e-11*5.97e24/(x**2 + y**2)

# Define angle from y-axis
    if y == 0:
        theta = np.pi/2
    else:
        theta = np.arctan(abs(x/y))

# Define new vx and vy
    if y >= 0:
        vy = vy + g*np.cos(theta)*dt
    elif y < 0:
        vy = vy - g*np.cos(theta)*dt
    if x >= 0:
        vx = vx + g*np.sin(theta)*dt
    elif x < 0:
        vx = vx - g*np.sin(theta)*dt

# Define new position of asteroid
    x = x + vx*dt
    y = y + vy*dt
    ast.center = [x,y]
    return

# Create the animation
anim = animation.FuncAnimation(f, step, interval=1)
# Show the animation
plt.show()

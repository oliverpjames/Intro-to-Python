import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as mpatches

# Create new Figure with black background
f = plt.figure(facecolor='black', figsize=(16,16))

# Add a subplot with no frame
ax = plt.subplot(111, frameon=False)

# Set plot limits
ax.set_ylim(-1e9, 1e9)
ax.set_xlim(-1e9, 1e9)

# Remove tick marks on the axes
ax.set_xticks([])
ax.set_yticks([])

# Set constannt simulation parameters
sf = 2                 # Radius of bodies scale factor
dt = 18000      # Time step in loop
G = 6.673e-11          # Gravitational constant
rast = 5e5 *sf         # Radius of asteriod
rearth = 6.37e6 *sf    # Radius of Earth
mearth = 5.97e24       # Mass of Earth
rmoon = 1.737e6 *sf    # Radius of Moon
mmoon = 7.342e22       # Mass of Moon
rmoonorb = 3.84467e8   # Radius of Moon's orbit

# Set Moon start position and velocity

#angvmoon = 2.6639e-6
mx = float(0)
my = float(rmoonorb)
mvx = 1024.143
mvy = 0

# Set asteroid's startposition, and velocity
vx = -7
vy = 0
x = float(0)
y = float(8e8)
#good orbits 
#unstable
#vx=-11e2, y=-7e8 
#vx= -60, y = 8e8
#vx = -1,-0.2,-0.3e2, y = -8e8
#vx = -1000, y = 8e8
#stable
#vx = -70, y = 8e8
#vx = 10e2, y = -2e8 

# Draw Earth and asteroid using the add_patch function
earth = ax.add_patch(mpatches.Circle([0,0], radius=rearth, fill=True, color='b', ls='solid'))
ast = ax.add_patch(mpatches.Circle([x,y], radius=rast, fill=True, color='w', ls='solid'))
moon = ax.add_patch(mpatches.Circle([mx,my], radius=rmoon, fill=True, color='w', ls='solid'))


def step(args):
    """This function advances the animation one time step"""
    global vx, vy, x, y, mvx, mvy, mx, my

# Define angle from y-axis and calculate new mvx and mvy
    mg = -G*mearth/(mx**2 + my**2)

    if my == 0:
        phi = np.pi/2
    else:
        phi = np.arctan(abs(mx/my))

    if my >= 0:
        mvy = mvy + mg*np.cos(phi)*dt
    elif my < 0:
        mvy = mvy - mg*np.cos(phi)*dt
    if mx >= 0:
        mvx = mvx + mg*np.sin(phi)*dt
    elif mx < 0:
        mvx = mvx - mg*np.sin(phi)*dt

    mx = mx + mvx*dt
    my = my + mvy*dt
    moon.center = [mx,my]

# Define angle from y-axis and calculate new vx and vy

    aeg = -G*mearth/(x**2 + y**2)
    amg = -G*mearth/((x - mx)**2 + (y - my)**2)

    if y == 0:
        aetheta= np.pi/2
    else:
        aetheta = np.arctan(abs(x/y))

    if y >= 0:
        vy = vy + aeg*np.cos(aetheta)*dt
    elif y < 0:
        vy = vy - aeg*np.cos(aetheta)*dt
    if x >= 0:
        vx = vx + aeg*np.sin(aetheta)*dt
    elif x < 0:
        vx = vx - aeg*np.sin(aetheta)*dt

    if (y - my) == 0:
        amtheta= np.pi/2
    else:
        amtheta = np.arctan(abs((x - mx)/(y - my)))

    if (y - my) >= 0:
        vy = vy + amg*np.cos(amtheta)*dt
    elif (y - my) < 0:
        vy = vy - amg*np.cos(amtheta)*dt
    if (x - mx) >= 0:
        vx = vx + amg*np.sin(amtheta)*dt
    elif (x - mx) < 0:
        vx = vx - amg*np.sin(amtheta)*dt

    x = x + vx*dt
    y = y + vy*dt
    ast.center = [x,y]
    return

# Create the animation
anim = animation.FuncAnimation(f, step, interval=1)
# Show the animation
plt.show()

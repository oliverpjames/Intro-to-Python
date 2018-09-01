import numpy as np
from scipy.signal import hann
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.animation as animation
import time

# Create new Figure with black background
f = plt.figure(facecolor='blue', figsize=(12,9))
plt.subplots_adjust(bottom=0, right=1, top=1, left=0)

#Add a subplot with no frame
ax = plt.subplot(111, frameon=False)

# Set plot limits
ax.set_xlim(0, 1200)
ax.set_ylim(-300, 600)

# Remove tick marks on the axes
ax.set_xticks([])
ax.set_yticks([])

#define smooth and resize curve
def smooth(y):
    return np.convolve(y, hann(50), mode='same')
    
def size(y):
    d = max(y) - min(y)
    return y/d*200
    

# Create random series of numbers (rnum=random numbers)
ns = 1200
x = np.linspace(0.,1200.,ns)
cumsum = np.cumsum(np.random.uniform(-10,10, ns))
y = size(smooth(cumsum))

ax.plot(x, y, "g")
plt.fill_between(x, -300, y, facecolor='g')


#Player start positions (make, teleport in future?)
p1x = np.random.randint(10,800)
p2x = np.random.randint(p1x+200,1190)

p1 = ax.add_patch(mpatches.Ellipse([p1x,y[p1x]+10], width=10, height=20, fill=True, color='R', ls='solid'))
p2 = ax.add_patch(mpatches.Ellipse([p2x,y[p2x]+10], width=10, height=20, fill=True, color='Y', ls='solid'))
    
# Compute gradient angle
phi = np.arctan(np.gradient(y))
#define time incriment
dt = 0.1
#define angle, and initial velocity (angle is direction from horizontal from right) 
a = 0.1*np.pi/2
vi = 50

#define gravity, start positions, and vx, vy
gx = p1x
gy = y[gx]+20
gvx = vi*np.cos(a)
gvy = vi*np.sin(a)
g = -9.81

#draw grenade
grenade = ax.add_patch(mpatches.Circle([gx,gy], radius=2.5, fill=True, color='k', ls='solid'))

def step(*args):
    global gx, gy, gvx, gvy
    if gy > y[gx]+5:
        gvx = gvx
        gx = gx + gvx*dt
        
        gvy = gvy + g*dt
        gy = gy + gvy*dt
    
        grenade.center = [gx, gy]
    
    elif gy <= y[gx] + 5:
        
        gv = (gvx**2 + gvy**2)**0.5
        theta = np.tan(gvx/gvy)
        ang = abs(theta) + phi[gx]

        if phi[gx] == 0:
            gvy = -gvy
        else:
            gvy = gv*np.cos(ang)
            gvx = -gv*np.sin(ang)
        gx = gx + gvx*dt
        gy = gy + gvy*dt
    return 
    

anim = animation.FuncAnimation(f, step, np.arange(1,100), interval=1)#, np.arange(1,1000)


#ax.text(0.04,0.9,'Time taken to execute: {:.2f} s'.format(time - start),transform=ax.transAxes, size='large')
plt.show()














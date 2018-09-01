import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import time
from mpl_toolkits.mplot3d import Axes3D

def derivs(u, t, p):

# Unpack the state of motion and the system parameters
    x,  y,  z = u
    sigma, beta, rho = p
    
    vx = sigma*(y - x)
    vy = rho*x - y - x*z
    vz = x*y - beta*z
    res = (vx, vy, vz)
    return res

# Set constants, and starting position
sigma = 10
beta = 8./3
rho = 28

x0 = 1#19.
y0 = 1#26.
z0 = 1#18.

params = [sigma, beta, rho]
init = [x0, y0, z0]

# Set values to be calculated over
n = 2e4
t0 = 0.
tend = 50.
t = np.linspace(t0, tend, n)

# compute solutions
u = odeint(derivs, init, t, args=(params, ))
x, y, z = u[:, 0], u[:, 1], u[:, 2]

f = plt.figure(figsize=(12,10))
ax = f.add_subplot(111, projection='3d')
ax.plot(x, y, z)#,'b', alpha=0.5)
plt.show()

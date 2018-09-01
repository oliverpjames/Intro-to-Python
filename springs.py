import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import time
#%matplotlib inline

def derivs(u, t, p):

# Unpack the state of motion and the system parameters
    x0, vx0, x1, vx1 = u
    k, m = p

# Compute the derivatives of the position and velocity; 
# Compute the acceleration due to a spring
# on a test particle. Its velocity is already known from the input. 
    
    a = np.array([(-k[0]*x0 + k[1]*(x1 - x0))/m[0], (- k[1]*(x1 - x0)- k[2]*x1)/m[1]])
    res = (vx0, a[0],vx1, a[1])
    return res

# Start clock
start = time.time()

k = np.array([1, 1, 1])
m = np.array([1, 1])

x0i = 0.5
x1i = -0.5
vx0i = 0.
vx1i = 0.

params = [k, m]
init = [x0i, vx0i, x1i, vx1i]

# Define solution domain and timestep
n = 1e4
t0 = 0.
tend = 500. 
t = np.linspace(t0,tend,n)

u = odeint(derivs, init, t, args=(params, ))
x0, vx0, x1, vx1 = u[:, 0], u[:, 1], u[:, 2], u[:, 3]

# Get the system clock time at the end of execution of solver.
end = time.time()

# Draw graphs
f = plt.figure(figsize=(30,12))
ax = plt.subplot(211)
ax.plot(t, x0, 'k')
ax.set_ylabel(r'$x1$', size='x-large')
ax.set_title('Springs', size='x-large')
ax.set_ylim([-0.6,0.6])
ax.set_xlim([0,500])
ax.axhline(0,ls=':')
ax.text(0.005,0.95,'Time taken to execute: {:.2f} s'.format(end - start),transform=ax.transAxes, size='large')

ax1 = plt.subplot(212)
ax1.plot(t, x1, 'k')
ax1.set_xlabel(r'$t$', size='x-large')
ax1.set_ylabel(r'$x2$', size='x-large')
ax1.set_ylim([-0.6,0.6])
ax1.set_xlim([0,500])
ax1.axhline(0,ls=':')
ax1.text(0.005,0.95,'Time taken to execute: {:.2f} s'.format(end - start),transform=ax.transAxes, size='large')

plt.draw()
plt.show()

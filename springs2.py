import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft, fftfreq
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

k = np.array([5, 1, 5])
m = np.array([1, 1])

x0i = 0.1
x1i = -3.
vx0i = 0.
vx1i = 0.

params = [k, m]
init = [x0i, vx0i, x1i, vx1i]

# Define solution domain and timestep
n = int(1e4)
t0 = 0.
tend = 500.
dels = (tend - t0)/n
t = np.linspace(t0,tend,n)

u = odeint(derivs, init, t, args=(params, ))
x0, vx0, x1, vx1 = u[:, 0], u[:, 1], u[:, 2], u[:, 3]

#compute fft etc.
G0 = fft(x0)
rcvsig0 = ifft(G0).real

f0 = fftfreq(n,dels)
sortinx = np.argsort(f0)
f0 = f0[sortinx]
G0 = G0[sortinx]

# Get the system clock time at the end of execution of solver.
end = time.time()

# Create a new Figure
fig = plt.figure(figsize=(30,12))

# Plot the signal
ax = plt.subplot(311)
ax.plot(t,x0)
ax.axhline(0,ls=':')
ax.set_ylim([-0.6,0.6])
ax.set_xlim([0,500])
ax.set_title(r'$g(t)=\sin(\omega t)$', size='x-large')

# Plot the normalised magnitude of the FFT (abs gives the magnitude of a complex number)
# The FFT is normalised by the number of samples taken and
# the factor of 2 ensures the peak is the same height as the amplitude of the wave (see below)
ax = plt.subplot(312)
ax.plot(f0,np.abs(G0)/(n/2.))
plt.xlim([0,10])
plt.ylim([-0.1,1.2])

# Plot the recovered signal
ax = plt.subplot(313)
ax.plot(t,rcvsig0)
ax.axhline(0,ls=':')
ax.set_ylim([-0.6,0.6])
ax.set_xlim([0,500])

plt.draw()
plt.show()

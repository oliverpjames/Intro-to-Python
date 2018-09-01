import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq
from scipy import interpolate
import matplotlib.gridspec as gridspec

data = "rev26_27.dat"
recdat = np.recfromtxt(data, names = ["time", "r", "theta", "phi"])
r = recdat.r
t = recdat.time

not_nan = np.logical_not(np.isnan(r))
i = np.arange(len(r))
rinterp = np.interp(i, i[not_nan], r[not_nan])

period = 1/fftfreq(34504, (t[-1]-t[0])/34504)
fftamp = fft(rinterp)

sort = np.argsort(fftamp)
fftamp = fftamp[sort]
period = period[sort]

gs = gridspec.GridSpec(8, 1)

plt.figure(figsize=[12,12])

ax1 = plt.subplot(gs[:2, :])
ax1.plot(t, rinterp, "r")
ax1.plot(t, r, "b")
ax1.set_xlim([934.9, 959])
ax1.set_xlabel("time since 2004(days)")
ax1.set_ylabel("radial component of magnetic field")

ax2 = plt.subplot(gs[3:, :])
ax2.plot(period, fftamp)#, "x")
ax2.set_xlim([0,20])
ax2.set_ylabel("fft(radial component of magnetic field)")
ax2.set_xlabel("time period(hours)")

plt.show()

# I notice that there is a couple of high amplitude radial components, with long oscilation
# periods, and many small amplitude short oscilation period components.
# There also appears to be 2 different dependancies, ie at different, both from the main cluster 


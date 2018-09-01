import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal
import matplotlib.gridspec as gridspec
data = "rev26_27.dat"
recdat = np.recfromtxt(data, names = ["time", "r", "theta", "phi"])

r = recdat.r
t = recdat.time
r = r[np.logical_not(np.isnan(r))]
t = t[np.logical_not(np.isnan(r))]
r = r[len(r)/2:]
t = t[len(t)/2:]

f = np.linspace(0.1, 100, 10000)
pgram = signal.lombscargle(t, r, f)
npgram = np.sqrt(pgram*4./len(r))

plt.figure(figsize=[10,10])
plt.plot(f,npgram)
plt.draw()
plt.show()



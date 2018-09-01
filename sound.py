import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft, fftfreq
import scipy.io.wavfile as wavfile


wav = np.load("fft.npy")
recvsig = ifft(wav).real
t = np.linspace(0.,11.,489584)
f = np.linspace(0.,44.1e3, 489584)
 
#fig = plt.figure(figsize = (30,12))
#ax = plt.subplot(211)
#ax.plot(f, wav)
#ax.set_xlim([0, 44.1e3])
#ax.set_title(r"Sound File", size="x-large")
#ax.set_xlabel("$Frequency$", size="x-large")
#ax.set_ylabel("$Amplitude$", size="x-large")


#ax1 = plt.subplot(212)
#ax1.plot(t, recvsig)
#ax1.set_xlim([0,11])
#ax1.set_title("Recovered Sound Wave", size="x-large")
#ax1.set_xlabel("$Time$", size="x-large")
#ax1.set_ylabel("$Amplitude$", size="x-large")

plt.show()
##the frequencies, that dictate the overal shape, and amplitude of the sound waves

wavfile.write('wavesound.wav', 44.1e3, recvsig.astype('int16')) 
#fu(umlout)r Elise! +maybe an accent somewhere I duon't know I'm not a Deutcshlander



wave = np.reshape(recvsig[0:489500:10], (10,-1))
#wave = np.swapaxes(wave, 1, 0)


fwave = abs(fft(wave))#, 0, 1000)



plt.imshow(fwave, aspect=100)
plt.show()


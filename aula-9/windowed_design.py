import numpy as np
from numpy import pi, cos, sin
import matplotlib.pyplot as plt
import scipy.fftpack


sample_rate = 5000

# definindo a frequencia de corte

fc = 0.014

# definindo o roll-off
BW = 0.5
# M = 4 / BW
M = 8
K = 1

i = np.arange(0, M, 0.001)

# 16-4
h = K * (sin(2*pi*fc*(i-M/2))/(i-M/2)) * (0.42 - 0.5*cos(2*pi*i/M) + 0.08*cos(4*pi*i/M))


###############
#   plot
plt.subplot(2, 1, 1)
plt.plot(i, h, label="Windowed")
plt.legend()
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")

#retorna a transformada de fourier
yf = scipy.fftpack.fft(h)

plt.subplot(2, 1, 2)
plt.plot(i, yf, 'b')
plt.xlabel("Freq")
plt.ylabel("Magnitude")

plt.grid()
plt.show()
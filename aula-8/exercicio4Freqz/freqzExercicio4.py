from scipy.signal import freqz
import numpy as np
import matplotlib.pyplot as plt


# A
num = [3, -3.2]
den = [1, -1.4, 0.45]
w, h = freqz(num, den)
plt.subplot(3, 1, 1)
plt.plot(w, 20 * np.log10(abs(h)), 'b')
plt.grid()

# B
num = [1, 0]
den = [1, -2.1, 1.08]
w, h = freqz(num, den)
plt.subplot(3, 1, 2)
plt.plot(w, 20 * np.log10(abs(h)), 'g')
plt.grid()

# C
num = [1, 0.9]
den = [1, 1, 0.41]
w, h = freqz(num, den)
plt.subplot(3, 1, 3)
plt.plot(w, 20 * np.log10(abs(h)), 'r')
plt.grid()

# modo manual
plt.figure(2)

# A
w = np.arange(0, np.pi, np.pi/1000)
num_m = (3*np.exp(-1j*w) - 3.2)
den_m = (np.exp(-1j*w) - 0.5) * (np.exp(-1j*w) - 0.9)
plt.subplot(3, 1, 1)
plt.plot(w*1000/(2*np.pi), 20 * np.log10(abs(num_m/den_m)), 'b')
plt.grid()

# B
num_m = np.exp(-1j*w)
den_m = (np.exp(-1j*w) - 0.9) * (np.exp(-1j*w) - 1.2)
plt.subplot(3, 1, 2)
plt.plot(w*1000/(2*np.pi), 20 * np.log10(abs(num_m/den_m)), 'g')
plt.grid()

# C
num_m = (np.exp(-1j*w) + 0.9)
den_m = np.exp(-2j*w) + np.exp(-1j*w) + 0.41
plt.subplot(3, 1, 3)
plt.plot(w*1000/(2*np.pi), 20 * np.log10(abs(num_m/den_m)), 'r')
plt.grid()


plt.show()
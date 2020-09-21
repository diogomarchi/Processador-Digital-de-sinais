import numpy as np
import matplotlib.pyplot as plt

w = np.arange(-1*np.pi, 1*np.pi, np.pi/100)
# formula walter
a = 2*np.cos(w) + 1
#a = np.exp(1j*w) + 1 + np.exp(-1j*w)

mod_x = abs(a)
fase_x = np.angle(a)

plt.subplot(2, 1, 1)
plt.plot(w, mod_x)
plt.title("Modulo de X")
plt.xlabel("W")
plt.grid

plt.subplot(3, 1, 3)
plt.plot(w, fase_x)
plt.title("Fase de X")
plt.xlabel("W")
plt.grid

plt.show()

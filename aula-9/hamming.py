import numpy as np
import matplotlib.pyplot as plt

fc = 400
M = 50

# para calcular os valores
i = np.arange(0, M, 0.00001)

# função passa baixa
w_i = 0.54 - 0.46 * np.cos(2*np.pi*i/M)


plt.subplot(1, 1, 1)
plt.plot(i, w_i, label="Output")
plt.legend()
plt.xlabel("i")
plt.ylabel("Amplitude")
plt.grid()
plt.show()
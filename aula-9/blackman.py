import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

fc = 400
M = 50

# para calcular os valores
i = np.arange(0, M, 0.00001)
i2 = np.arange(-M/2, M/2, 0.00001)

# função passa baixa
w_i = 0.42 - 0.5 * np.cos(2*np.pi*i/M) - 0.08 * np.cos(4*np.pi*i/M)
w_i_2 = np.sinc(i2)


plt.subplot(2, 1, 1)
plt.plot(i, w_i, label="formula do artigo")
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(i2, w_i_2, label="sinc do python")
plt.legend()

plt.grid()
plt.show()
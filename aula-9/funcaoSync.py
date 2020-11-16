import numpy as np
import matplotlib.pyplot as plt

i = np.arange(-0.2, 0.2, 0.00001)
Fc = 100

#funcao passa baixa
h = (np.sin(2*np.pi*Fc*i)) / i*np.pi

###############
#   plot
plt.plot(i, h, "k-", "ko", "k-")
plt.legend()

plt.show()


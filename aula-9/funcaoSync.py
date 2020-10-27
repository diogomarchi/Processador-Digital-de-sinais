import numpy as np
import matplotlib.pyplot as plt

i = np.arange(-2, 2, 0.01)
Fc = 100

#funcao passa baixa
h = (np.sin(2*np.pi*Fc*i)) / i*np.pi

###############
#   plot
plt.stem(i, h, "k-", "ko", "k-")
plt.legend()

plt.show()


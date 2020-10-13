# Exemplo de um filtro passa baixa
# H(s) = a/(s + a)
# s ----> z via Tustin
# H[z] = Y[z]/X[z] =

from scipy.signal import freqz, TransferFunction, bode, cont2discrete
import scipy.signal as signal
import numpy as np
import matplotlib.pyplot as plt

# Definindo a especificação do filtro

# R = 10;
# C = 10*10^-6;
# W0 = 1/(R*C)
W0 = 2*np.pi*1000

f0 = W0/(2*np.pi)  # frequencia de sintonia em Hz

# w0 = 2*pi*f0;

# Definindo os coeficientes em s

num = [W0, 0]
den = [W0, 1]

H = TransferFunction(num, den)
print(type(H))
bode(H)

# Aplicando a transf Biliner S->Z

Fs = 8000   # Frequência de amostragem
Ts = 1/Fs

# https://github.com/scipy/scipy/issues/11312
Hd = cont2discrete(H, Ts, 'bilinear')     # Convertendo para discreto

# Plotar em frequencia
[H, w] = freqz(Hd.Numerator[0, 0], Hd.Denominator[0, 0], fs=Fs/(2*np.pi))

plt.figure(2)
plt.plot(w, 20*np.log10(abs(H)))
plt.grid()
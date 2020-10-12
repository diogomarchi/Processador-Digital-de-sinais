# Resposta  de frequência da média móvel
import numpy as np
import matplotlib.pyplot as plt
import scipy as signal

# Variaveis
passo = np.pi / 1000
w = np.arange(0, np.pi, passo)
L = 8
Fs = 8000

# Numerador e Denominador
num = np.sin(w * L / 2)
den = np.sin(w / 2)

# Equação Base
temp = num / den

# Rad
X = (1 / L) * (abs(temp))
plt.subplot(3, 1, 1)
plt.plot(w, X)
plt.xlabel('Frquência')
plt.title('Frequêncua Rad')
plt.grid


# Hz
F_Hz = (w / np.pi) * (Fs / 2)
plt.subplot(3, 1, 2)
plt.plot(F_Hz, X)
plt.xlabel('Frequência')
plt.title('Frequência em Hz')
plt.grid

# Db
X_Db = 20 * np.log10(X)
plt.subplot(3, 1, 3)
plt.plot(F_Hz, X_Db)
plt.ylabel('Atenuação DB')
plt.xlabel('Frequência')
plt.title('Frequência em Hz')
plt.grid

plt.axis([0, 4000, - 70, 0])

plt.figure(2)
# Usando freqz para obter a resposta em frequencia
# num = [.25 .25 .25 .25];
num2 = np.full(L, 1 / L)
den = 1
H, Freq = signal.freqz(num2, den, Fs)
plt.plot(Freq * Fs / (2 * np.pi), 20 * np.log10(abs(H)))
plt.title('Magnitude da resposta em frequencia')
plt.grid


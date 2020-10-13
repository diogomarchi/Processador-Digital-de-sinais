import numpy as np
import matplotlib.pyplot as plt

tam = 8000
entrada = np.zeros(2)
saida = 0

Fc = 1000
Fs = 8000

# calcula FC
wc = 2*np.pi*Fc

# F'
F1 = 2 * Fs

# coeficientes
a = wc/(F1+wc)
b = (wc-F1)/(F1+wc)

with open('sweep_20_3600.pcm', 'rb') as f:
    buf = f.read()
    data_i = np.frombuffer(buf, dtype='int16')
    data_len = len(data_i)

    # replica do arquivo lido para salvar o resultado
    data_o = np.zeros_like(data_i)

    for i in range(data_len):
        entrada[0] = data_i[i]

        saida = a*entrada[0] + a*entrada[1] - b*saida
        data_o[i] = saida
        entrada[1:2] = entrada[0:1]

# amostra de 100 ms
t = np.arange(0, data_len/tam, 1 / tam)

###############
#   plot
plt.stem(t, data_i[: len(t)], "k-", "ko", "k-", label="Input")
plt.plot(t, data_o[: len(t)], label="Output")
plt.legend()
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()


file_name = "../passaBaixaSaida.pcm"
with open(file_name, 'wb') as f:
    for d in data_o:
        f.write(d)
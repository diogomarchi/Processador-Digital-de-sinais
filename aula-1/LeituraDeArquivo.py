# Diogo Marchi #

import numpy as np
import matplotlib.pyplot as plt


ganho = 0.5
taxa_amostragem = 8000


with open('teste_audio.pcm', 'rb') as f:
    buf = f.read()
    data_i = np.frombuffer(buf, dtype='int16')
    data_len = len(data_i)

    # replica do arquivo lido para salvar o resultado
    data_o = np.zeros_like(data_i)

    for i in range(data_len):
        data_o[i] = data_i[i] * ganho

    with open(r'result.pcm', 'wb') as f:
        for d in data_o:
            f.write(d)

    t = np.arange(0, data_len/taxa_amostragem, 1 / taxa_amostragem)

    plt.plot(t, data_i[: len(t)], label="Input")
    plt.plot(t, data_o[: len(t)], label="Output")
    plt.legend()
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.show()





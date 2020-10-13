import numpy as np
import matplotlib.pyplot as plt

sample_rate = 8000
input_buf = np.zeros(3)
out_buf = np.zeros(2)

Fc = 1000
Fs = sample_rate

# calcula FC
wc = 2*np.pi*Fc

# F'
F1 = 2 * Fs

# coeficientes
a = F1/(F1+wc)
b = (2*wc)/(F1+wc)
c = (F1-wc) / (F1+wc)

print(a)
print(b)

with open('sweep_20_3600', 'rb') as f:
    buf = f.read()
    data_i = np.frombuffer(buf, dtype='int16')
    data_len = len(data_i)

    # replica do arquivo lido para salvar o resultado
    data_o = np.zeros_like(data_i)

    for i in range(data_len):
        input_buf[0] = data_i[i]

        m = a*input_buf[0] - a*input_buf[2] - b*out_buf[0] + c*out_buf[1]

        out_buf[1:len(out_buf)] = out_buf[0:len(out_buf)-1]
        out_buf[0] = m     # y-1

        data_o[i] = m
        input_buf[1:len(input_buf)] = input_buf[0:len(input_buf) - 1]

# amostra de 100 ms
t = np.arange(0, data_len/sample_rate, 1 / sample_rate)

###############
#   plot
plt.stem(t, data_i[: len(t)], "k-", "ko", "k-", label="Input")
plt.plot(t, data_o[: len(t)], label="Output")
plt.legend()
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()


file_name = "../media_manual_result.pcm"
with open(file_name, 'wb') as f:
    for d in data_o:
        f.write(d)
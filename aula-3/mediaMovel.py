import numpy as np
import matplotlib.pyplot as plt

sample_rate = 8000
media_len = 9
media_buf = np.zeros(media_len)

with open("wn_.pcm", 'rb') as f:
    buf = f.read()
    data_i = np.frombuffer(buf, dtype='int16')
    data_len = len(data_i)

    # replica do arquivo lido para salvar o resultado
    data_o = np.zeros_like(data_i)

    for i in range(data_len):
        media_buf[0] = data_i[i]
        m = np.sum(media_buf)/media_len
        data_o[i] = m
        buf = media_buf[0:media_len-1]
        media_buf[1:media_len] = buf

# amostra de 100 ms
t = np.arange(0, 0.1, 1 / sample_rate)

###############
#   plot
plt.stem(t, data_i[: len(t)], "k-", "ko", "k-", label="Input")
plt.plot(t, data_o[: len(t)], label="Output")
plt.legend()
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()


file_name = "media_"+str(media_len)+"_result.pcm"
with open(file_name, 'wb') as f:
    for d in data_o:
        f.write(d)
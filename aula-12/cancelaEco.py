import numpy as np
import matplotlib.pyplot as plt

n = 160

#carregando sistema desconhecido
with open("near_apcm.pcm", 'rb') as f:
    buf = f.read()
    data_i2 = np.frombuffer(buf, dtype='int16')
    data_lenNear = len(data_i2)
    near = data_i2[:n]

#carregando ruido branco
with open("far_apcm.pcm", 'rb') as f:
    buf = f.read()
    data_i = np.frombuffer(buf, dtype='int16')
    data_lenFar = len(data_i)
    far = data_i[:n]


#mi
numero = 0.0000001

# Vetores utilizados
wn = np.zeros(n, dtype=np.float64)			# Coeficientes de W(z)

erro = []

for i in range(data_lenFar//n):

    # filtragem
    yn = wn.T * far

    # calculo do erro
    ee = near - yn

    # atualizando coeficientes
    wn = wn + 2 * numero * ee * far

    erro.append(ee)



# Plotando os sinais de erro e de controle
plt.figure(1)
plt.plot(erro)
plt.grid
plt.title('Sinal de Erro');
plt.xlabel('Amostras');
plt.ylabel('Erro');

plt.figure(2)
plt.plot(wn)
plt.grid
plt.title('Comportamento dos Coefs');
plt.xlabel('Amostras');
plt.show()

# salva resultado do filtro
file_name = "resultado_coefs_eco.pcm"
with open(file_name, 'wb') as f:
    erro = np.asarray(erro)
    for d in erro:
        f.write(d.astype(np.int16))

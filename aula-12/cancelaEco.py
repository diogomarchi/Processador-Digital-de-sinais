import numpy as np
import matplotlib.pyplot as plt

n = 160

#carregando sistema desconhecido
with open("near_apcm.pcm", 'rb') as f:
    buf = f.read()
    data_i2 = np.frombuffer(buf, dtype='int16')
    data_lenNear = len(data_i2)
    dn = data_i2[0:n]

#carregando ruido branco
with open("far_apcm.pcm", 'rb') as f:
    buf = f.read()
    data_i = np.frombuffer(buf, dtype='int16')
    data_lenFar = len(data_i)
    xn = data_i[0:n]


#mi
numero = 0.00000005

#tamanho do filtro adaptativo
tam_filtro = len(dn)

#numero de interação pelo tamanho do ruido branco
n_inter = 200000

# Vetores utilizados
wn = np.zeros(tam_filtro, dtype=np.float64)			# Coeficientes de W(z)

erro = []

for i in range(n_inter):

    # filtragem
    yn = wn.T * xn

    # calculo do erro
    ee = dn - yn

    erro.append(sum(abs(ee)))
    print(erro[i])

    #atualizando coeficientes
    wn = wn + 2 * numero * ee * xn

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
    yn = np.convolve(wn, data_i, mode="same")
    for d in yn:
        f.write(d.astype(np.float16))

# salva coeficientes
coefs_name = "coef_adptativo_eco.dat"
with open(coefs_name, 'w') as f:
    for d in wn:
        f.write(str(d.astype(np.float16))+",\n")
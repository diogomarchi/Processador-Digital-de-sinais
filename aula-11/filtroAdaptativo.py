import numpy as np
import matplotlib.pyplot as plt

n = 160

#carregando sistema desconhecido
with open("passaBaixaCoef.dat", 'r') as f:
    cof = f.read().replace("\n", "").split(",")
    cof.remove('')
    desconhecido = np.asarray(cof, dtype=np.float16)

#carregando ruido branco
with open("wn.pcm", 'rb') as f:
    buf = f.read()
    data_i = np.frombuffer(buf, dtype='int16')
    data_lenWn = len(data_i)
    xn = data_i[0:n]

    dn = desconhecido.T * xn

#mi
numero = 0.000000000005

#tamanho do filtro adaptativo
tam_filtro = len(desconhecido)

#numero de interação pelo tamanho do ruido branco
n_inter = 200000

# Vetores utilizados
wn = np.zeros(tam_filtro, dtype=np.float64)			# Coeficientes de W(z)

# aplica coefs sistema desconhecido
dn = desconhecido.T * xn
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
file_name = "resultado_coefs.pcm"
with open(file_name, 'wb') as f:
    yn = np.convolve(wn, data_i, mode="same")
    for d in yn:
        f.write(d.astype(np.float16))

# salva coeficientes
coefs_name = "coef_adptativo.dat"
with open(coefs_name, 'w') as f:
    for d in wn:
        f.write(str(d.astype(np.float16))+",\n")

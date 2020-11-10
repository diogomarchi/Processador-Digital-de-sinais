import numpy as np
import matplotlib.pyplot as plt

#carregando ruido branco
with open("wn.pcm", 'rb') as f:
    buf = f.read()
    x = np.frombuffer(buf, dtype='int16')
    data_lenWn = len(x)

print(data_lenWn)
#carregando sistema desconhecido
with open("passaBaixa.pcm", 'rb') as f:
    buf = f.read()
    w0 = np.frombuffer(buf, dtype='int16')
    data_lenPb = len(w0)

#mi
numero = 0.000000000005

#tamanho do filtro adaptativo
tam_filtro = data_lenPb

#numero de interação pelo tamanho do ruido branco
n_inter = data_lenWn

# Vetores utilizados
wn = np.zeros(tam_filtro);			# Coeficientes de W(z)
x_linhan = np.zeros(tam_filtro);	# Vetor de entrada filtrado por F^(z)


#vetor de erro
erro_salva = np.zeros(n_inter)
#vetor para sinal de controle
y_salva = np.zeros(n_inter)
#plotar sinal dos coeficientes
w_salva = np.zeros(n_inter)




for i in range(n_inter):

    x_new = x[i]

    x_linhan[0] = x_new

    y = 0
    # filtragem
    for j in range(tam_filtro):
        y = y + x_linhan[j] * wn[j]
    y_salva[i] = y


    d = 0
    #saida desejada
    for j in range(tam_filtro):
        d = d + x_linhan[j] * w0[j]



    #calculo do erro
    erro = d - y
    #salvando o erro no vetor
    erro_salva[i] = erro

    #atualizando coeficientes
    for j in range(tam_filtro):
        wn[j] = wn[j] + numero * erro * x_linhan[j]

    #w_salva[i] = wn
    #atualiza vetor x_linha
    for j in range(tam_filtro-1):
        x_linhan[tam_filtro-1-j] = x_linhan[tam_filtro-1-j-1]



# Plotando os sinais de erro e de controle
plt.figure(1)
plt.plot(erro_salva)
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

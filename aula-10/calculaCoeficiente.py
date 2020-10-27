 # 'LOW-PASS WINDOWED-SINC FILTER
 #'This program filters 5000 samples with a 101 point windowed-sinc filter,
 #resulting in 4900 samples of filtered data.
 #
import numpy as np

fs = 8000
fc = 400
bw = 200
bwn = bw / fs
fcn = fc / fs

M = 4 / bwn
#create vector
h = [M]

#Calculate the low-pass filter kernel via Eq. 16-4
for i in M:
    if (i - M/2) == 0:
         h[i] = 2*np.pi*fcn

    else:
         h[i] = np.sin(2*np.pi*fcn * (i-M/2)) / (i-M/2)

    h[i] = h[i] * (0.54 - 0.46*np.cos(2*np.pi*i/M))

#Normalize the low-pass filter kernel for
soma = 0
for i in 100: #'unity gain at DC
    soma = soma + h[i]

#garantindo que os valores estao entre 0 e 1
for i in 100:
    h[i] = h[1] / soma


#fazer para salvar esses coeficientes
#obter resposta em frequencia


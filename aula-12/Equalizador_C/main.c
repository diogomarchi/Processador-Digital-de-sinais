/* Implementação de um filtro
Lê um arquivo binário com amostras em 16bits
Salva arquivo filtrado também em 16 bits
George
 */
#include <stdio.h>
#include <fcntl.h>
//#include <io.h>

#define NSAMPLES 160

int main() {
  FILE * in_file, * out_file;
  int n_amost;

  short entrada, saida;
  short sample[NSAMPLES] = {
    0x0
  };

  float yA = 0, yB = 0, yF = 0, y = 0;

  // ganhos dos filtros
  float g_pb = 0.7;
  float g_pf = 0.6;
  float g_pa = 0.5;

  //Carregando os coeficientes do filtro pb
  float coef_pb[NSAMPLES] = {
        #include "coefPassaBaixaEq.dat" // NSAMPLES
  };

  //Carregando os coeficientes do filtro pb
  float coef_pf[NSAMPLES] = {
        #include "coefPassaFaixaEq.dat" // NSAMPLES
  };

  //Carregando os coeficientes do filtro pb
  float coef_pa[NSAMPLES] = {
        #include "coefPassaAltaEq.dat" // NSAMPLES
  };

  /* abre os arquivos de entrada e saida */
  if ((in_file = fopen("sweep_20_3600.pcm", "rb")) == NULL) {
    printf("\nErro: Nao abriu o arquivo de entrada\n");
    return 0;
  }
  if ((out_file = fopen("resultado_filtro_c.pcm", "wb")) == NULL) {
    printf("\nErro: Nao abriu o arquivo de saida\n");
    return 0;
  }

  // zera vetor de amostras
  for (int i = 0; i < NSAMPLES; i++) {
    sample[i] = 0;
  }

  // execução do filtro
  do {

    //zera saída do filtro
    yA = 0, yB = 0, yF = 0, y = 0;

    //lê dado do arquivo
    n_amost = fread( & entrada, sizeof(short), 1, in_file);
    sample[0] = entrada;

    //Convolução e acumulação PB
    for (int n = 0; n < NSAMPLES; n++) {
      yB += g_pb * coef_pb[n] * sample[n];
    }

    //Convolução e acumulação PF
    for (int n = 0; n < NSAMPLES; n++) {
      yF += g_pf* coef_pf[n] * sample[n];
    }

    //Convolução e acumulação PA
    for (int n = 0; n < NSAMPLES; n++) {
      yA += g_pa * coef_pa[n] * sample[n];
    }

    //desloca amostra
    for (int n = NSAMPLES - 1; n > 0; n--) {
      sample[n] = sample[n - 1];
    }

    y = yA + yB + yF;

    saida = (short) y;

    //escreve no arquivo de saída
    fwrite( & saida, sizeof(short), 1, out_file);

  } while (n_amost);

  //fecha os arquivos de entrada de saída
  fclose(out_file);
  fclose(in_file);
  return 0;
}

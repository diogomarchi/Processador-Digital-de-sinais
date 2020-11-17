#include <stdio.h>
#include <fcntl.h>

#define NSAMPLES 160 // quantidade de coef

int main() {
  FILE * in_file, * out_file;
  int i, n, n_amost;
  float mi = 0.00000000001;
  double y = 0.0, dn = 0.0, erro = 0.0;


  short entrada, saida;
  short sample[NSAMPLES];

  double wn[NSAMPLES];

  //Carregando os coeficientes do filtro média móvel
  float coef[NSAMPLES] = {
        #include "passaAlta.dat" // NSAMPLES
  };

  /* abre os arquivos de entrada e saida */
  if ((in_file = fopen("wn.pcm", "rb")) == NULL) {
    printf("\nErro: Nao abriu o arquivo de entrada\n");
    return 0;
  }
  if ((out_file = fopen("resultado_filtro_adaptativo_c.pcm", "wb")) == NULL) {
    printf("\nErro: Nao abriu o arquivo de saida\n");
    return 0;
  }

  // zera vetor de amostras
  for (i = 0; i < NSAMPLES; i++) {
    sample[i] = 0;
    wn[i] = 0.0;
  }

  // execução do filtro
  do{

    //zera saída do filtro
    y = 0;
    dn = 0;
    //lê dado do arquivo
    n_amost = fread( & entrada, sizeof(short), 1, in_file);
    sample[0] = entrada;

    //Convolução da saida esperada
    for (n = 0; n < NSAMPLES; n++) {
      dn += coef[n] * sample[n];
    }

    // convolução da saida esperada
    for (int j = 0; j < NSAMPLES; j++) {
        y += wn[j] * sample[j];
    }


    erro = dn - y;

    //desloca amostra
    for (n = 0; n < NSAMPLES; n++) {
        wn[n] = wn[n] + 2.0 * mi * erro * sample[n];
    }

    //desloca amostra
    for (n = NSAMPLES - 1; n > 0; n--) {
        sample[n] = sample[n - 1];
    }

    saida = (short) erro;

    //escreve no arquivo de saída
    fwrite( & saida, sizeof(short), 1, out_file);

  }while(n_amost);

  //fecha os arquivos de entrada de saída
  fclose(out_file);
  fclose(in_file);
  return 0;
}

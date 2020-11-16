/* Implementação de um eco
Lê um arquivo binário com amostras em 16bits
Salva arquivo com eco também em 16 bits
 */
#include <stdio.h>

#include <fcntl.h>

#include <io.h>

int main() {
  float Fs, Ts, t1, t2, L, a0, a1, a2, y = 0;
  int n1, n2;
  Fs = 8000;
  Ts = 1 / Fs;
  t1 = 1.0 / 10;
  t2 = 1.5 / 10;
  L = 1 * Fs;
  n1 = t1 * Fs;
  n2 = t2 * Fs;

  //Definição dos ganhos
  a0 = 0.5;
  a1 = 0.3;
  a2 = 0.2;

  FILE * in_file, * out_file;
  int n_amost;

  short entrada, saida;

  /* abre os arquivos de entrada e saida */
  if ((in_file = fopen("teste_audio.pcm", "rb")) == NULL) {
    printf("\nErro: Nao abriu o arquivo de entrada\n");
    return 0;
  }
  if ((out_file = fopen("sai_teste_audio.pcm", "wb")) == NULL) {
    printf("\nErro: Nao abriu o arquivo de saida\n");
    return 0;
  }

  float sample[n2];
  // zera vetor de amostras
  for (int i = 0; i < n2; i++) {
    sample[i] = 0;
  }

  do {
    //zera saída do filtro
    y = 0;
    //lê dado do arquivo
    n_amost = fread( & entrada, sizeof(short), 1, in_file);
    sample[0] = entrada;
    y = a0 * sample[0] + a1 * sample[n1 - 1] + a2 * sample[n2 - 1];
    saida = (short) y;

    //deslocamento
    for (int i = n2 - 1; i > 0; i--) {
      sample[i] = sample[i - 1];
    }

    fwrite( & saida, sizeof(short), 1, out_file);
  } while (n_amost);

  //fecha os arquivos de entrada de saída
  fclose(out_file);
  fclose(in_file);
  return 0;
}

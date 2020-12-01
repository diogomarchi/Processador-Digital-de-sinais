#include <stdio.h>
#include <cycles.h>


#define NSAMPLES 160 // quantidade de coef




extern short calculaPassaBaixa( short *, float *, int);




int main(int argc,char *argv[]) {
	
  FILE * in_file, * out_file;
  int i, n, n_amost;
  
  cycle_stats_t stats;

  short entrada, saida;
  
  short sample[NSAMPLES] = {0x0};

  float y = 0.0;

  //Carregando os coeficientes 
  float coefPB[NSAMPLES] = {
        #include "passaBaixaCoef.dat" // NSAMPLES
  };
  
  printf("***************************************************************\n");
  printf("* TESTE COM ARQUIVOS					           		      *\n");
  printf("*                                                             *\n");
  printf("***************************************************************\n");
  printf("\n");

  /* abre os arquivos de entrada e saida */
  if ((in_file = fopen("..\\sweep_20_3600.pcm", "rb")) == NULL) {
    printf("\nErro: Nao abriu o arquivo de entrada\n");
    return 0;
  }
  if ((out_file = fopen("..\\resultado_filtro_PB_c.pcm", "wb")) == NULL) {
    printf("\nErro: Nao abriu o arquivo de saida\n");
    return 0;
  }

  // execucao do filtro
  while(fread( & entrada, sizeof(short), 1, in_file)==1) {
  	
	sample[0] = entrada;

    saida = calculaPassaBaixa (sample, coefPB, NSAMPLES) ;

    //escreve no arquivo de saída
    fwrite( & saida, sizeof(short), 1, out_file);

  }

  //fecha os arquivos de entrada de saída
  fclose(in_file);
  fclose(out_file);
  printf("terminou de fazer o passa baixa com o sweep");
  
  return 0;
  
}

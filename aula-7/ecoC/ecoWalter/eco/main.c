/* Implementa��o de um filtro M�dia M�vel
L� um arquivo bin�rio com amostras em 16bits
Salva arquivo filtrado tamb�m em 16 bits
Walter vers�o 1.0
 */
#include <stdio.h>
#include <fcntl.h>
#include <io.h>


#define NSAMPLES       8	// Tamanho da m�dia

int main()
{
    float Fs, Ts, t1, t2, L , n1, n2, a0, a1, a2;
    Fs = 8000;
    Ts = 1 / Fs;
    t1 = 1.0*10^-1;
    t2 = 1.5*10^-1;
    L = 1 * Fs;
    n1 = t1*Fs;
    n2 = t2*Fs;

    #Defini��o dos ganhos
    a0 = 0.5;
    a1 = 0.3;
    a2 = 0.2;

   FILE *in_file, *out_file;
   int i, n, n_amost;

   short entrada, saida;
   short sample[NSAMPLES] = {0x0};

   float y=0;

   //Carregando os coeficientes do filtro m�dia m�vel

   float coef[NSAMPLES]={
   				#include "coefs_mm_8.txt"
   };


   /* abre os arquivos de entrada e saida */
  if ((in_file = fopen("teste_audio.pcm","rb"))==NULL)
  {
    printf("\nErro: Nao abriu o arquivo de entrada\n");
    return 0;
  }
  if ((out_file = fopen("sai_teste_audio.pcm","wb"))==NULL)
  {
    printf("\nErro: Nao abriu o arquivo de saida\n");
    return 0;
  }

   // zera vetor de amostras
   for (i=0; i<NSAMPLES; i++)
        {
        sample[i]=0;
        }
    float y = 0;
   // execu��o do filtro
 do {
    //zera sa�da do filtro
    y=0;
    //l� dado do arquivo
    n_amost = fread(&entrada,sizeof(short),1,in_file);
    sample[0] = entrada;
    y = a0 * sample[0] + a1 * sample[n1-1] + a2 * sample[n2-1]
    saida[j] = y
    for(int i = n_amost; i > 0; i ++){
        sample[i] = sample[i-1];
    }
    fwrite(&saida,sizeof(short),1,out_file);
 } while (n_amost);


   //fecha os arquivos de entrada de sa�da
   fclose(out_file);
   fclose(in_file);
   return 0;
}

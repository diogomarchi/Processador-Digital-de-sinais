#include <stdio.h>
#include <stdlib.h>

void zeraVetor(int *vet, int tam){
    for(int i=0; i < tam; i++){
        vet[i] = 0;
    }
}

int somaTudo(int *vet, int tam){
    int resultado = 0;
    for(int i = 0; i < tam; i ++){
        resultado += vet[i];
    }
    return resultado;
}

void deslocamento(int *vet, int tam){
    for(int i = tam-1; i > 0; i--){
        vet[i] = vet[i-1];
    }
}

int main()
{
    int sample_rate = 8000;
    int media_len = 9;
    int media_buf[media_len];
    zeraVetor(media_buf, media_len);

    FILE *arq;
    arq = fopen("wn1.pcm","rb");

    if(arq == NULL){
        printf("deu erro ao abrir arquivo");
        return 0;
    }

    FILE * output;
    printf ( " Criando arquivo de gravacao \ n " );
    output = fopen ( " media_resultado_c.pcm " , " wb " );
    if (output == NULL ) {
        printf ( " Erro ao criar arquivo de saída! " );
        return  0 ;
    }

    // buffer para leitura
    short buff = 0;

    // tamanho do arquivo de entrada
    int TAM = 0;

    // le de dois em 2 bytes colocando valor em buff. quando acabar o inputuivo retorna 0
    while(fread(&buff, 2, 1, arq) != 0){
        TAM++;
        media_buf[0] = buff;
        short m = somaTudo(media_buf, media_len)/media_len;
        fwrite(&m, 2, 1, output);
        deslocamento(media_buf, media_len);
    }

    printf("Tamanho do arquivo de entrada %d bytes\n", 2*TAM);

    fclose(arq);
    fclose(output);
    return 0;
}

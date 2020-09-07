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
    fseek(arq, 0, SEEK_SET);
    if(arq == NULL){
        printf("deu cagada");
        return 0;
    }

    int *ptr, cont = 0;
    while(fread(ptr, sizeof(short),1,arq)){
          printf("entrou no while \n");
        cont ++;
    }
    printf("cont: %d", cont);
    int data_i[cont];
/*
    fseek(arq, 0, SEEK_SET);
    printf("chegou aqui 2");
    int data_i[cont];
    int j = 0;

    while(fread(ptr, sizeof(short),1,arq)){
        data_i[j] = ptr;
        j++;
    }
    */
    // replica do arquivo lido para salvar o resultado
    float data_o[cont];
    zeraVetor(data_o,cont);

    for(int i = 0; i < cont; i ++){
        media_buf[0] = data_i[i];
        float m = somaTudo(media_buf, media_len)/media_len;
        data_o[i] = m;
        deslocamento(media_buf, media_len);
    }

    fclose(arq);

    //gravar em arquivo


    return 0;
}

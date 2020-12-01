short calculaPassaBaixa( short *sample, float *coefPB, int NSAMPLES )
{
    //zera saída do filtro
    int n = 0;
    float y = 0.0;
	short saida_filtro;
	

    //Convolução e acumulação
    for (n = 0; n < NSAMPLES; n++) {
      y += coefPB[n] * sample[n];
    }

    //desloca amostra
    for (n = NSAMPLES - 1; n > 0; n--) {
      sample[n] = sample[n - 1];
    }
    
    
 	saida_filtro = (short)y;

    return saida_filtro;
}

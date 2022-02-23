
#include "cuda_runtime.h"
#include "device_launch_parameters.h"

#include <stdio.h>

__global__ void addArraysGPU(int* a, int* b, int* c)
{
	int i = threadIdx.x;
	c[i] = a[i] + b[i];
}

void main()
{
	// Constante
	const int count = 5;
	const int size = count * sizeof(int);

	// Arrays - Mem�ria RAM
	int ha[] = { 1, 2, 3, 4, 5 };
	int hb[] = { 100, 200, 300, 400, 500 };

	// Array para gravar o resultado - Mem�ria RAM
	int hc[count];

	// Vari�veis para execu��o na GPU
	int *da, *db, *dc;

	// Aloca��o de mem�ria na GPU
	cudaMalloc(&da, size);
	cudaMalloc(&db, size);
	cudaMalloc(&dc, size);

	// C�pia das vari�veis a e b da Mem�ria RAM para a Mem�ria na GPU
	cudaMemcpy(da, ha, size, cudaMemcpyHostToDevice);
	cudaMemcpy(db, hb, size, cudaMemcpyHostToDevice);

	// Definindo um bloco de threads
	addArraysGPU <<<1, count >>>(da, db, dc);

	// C�pia do resultado da Mem�ria da GPU de volta para a Mem�ria da CPU
	cudaMemcpy(hc, dc, size, cudaMemcpyDeviceToHost);

	// Imprime os resultados
	printf("%d %d %d %d %d",
		hc[0],
		hc[1],
		hc[2],
		hc[3],
		hc[4]);

	// Libera as �reas de mem�ria
	cudaFree(da);
	cudaFree(db);
	cudaFree(dc);

	// Para visualizar o resultado na tela at� pressionar uma tecla
	getchar();

}

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

	// Arrays - Memória RAM
	int ha[] = { 1, 2, 3, 4, 5 };
	int hb[] = { 100, 200, 300, 400, 500 };

	// Array para gravar o resultado - Memória RAM
	int hc[count];

	// Variáveis para execução na GPU
	int *da, *db, *dc;

	// Alocação de memória na GPU
	cudaMalloc(&da, size);
	cudaMalloc(&db, size);
	cudaMalloc(&dc, size);

	// Cópia das variáveis a e b da Memória RAM para a Memória na GPU
	cudaMemcpy(da, ha, size, cudaMemcpyHostToDevice);
	cudaMemcpy(db, hb, size, cudaMemcpyHostToDevice);

	// Definindo um bloco de threads
	addArraysGPU <<<1, count >>>(da, db, dc);

	// Cópia do resultado da Memória da GPU de volta para a Memória da CPU
	cudaMemcpy(hc, dc, size, cudaMemcpyDeviceToHost);

	// Imprime os resultados
	printf("%d %d %d %d %d",
		hc[0],
		hc[1],
		hc[2],
		hc[3],
		hc[4]);

	// Libera as áreas de memória
	cudaFree(da);
	cudaFree(db);
	cudaFree(dc);

	// Para visualizar o resultado na tela até pressionar uma tecla
	getchar();

}
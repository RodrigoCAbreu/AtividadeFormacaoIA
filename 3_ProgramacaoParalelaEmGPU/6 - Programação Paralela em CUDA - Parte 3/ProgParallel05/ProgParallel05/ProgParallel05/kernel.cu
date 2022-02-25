#include "cuda_runtime.h"
#include "device_launch_parameters.h"

#include <iostream>
#include <numeric>
using namespace std;

__global__ void sumSingleBlock(int* d)
{
	int tid = threadIdx.x;

	// Número de threads participando em cada iteração 
	for (int tc = blockDim.x, stepSize = 1; tc > 0; tc >>= 1, stepSize <<= 1)
	{
		// Thread deve ter permissão para escrever. Thread ID deve ser menor que Thread Count
		if (tid < tc)
		{
			// Definindo como será a operação de Reduce
			// Precisamos especificar que a thread obteve o resultado e então somar com o próximo elemento do array
			int pa = tid * stepSize * 2;

			// Obtemos o que foi escrito (gravado) pela thread e somamos com o próximo elemento do array
			int pb = pa + stepSize;
			d[pa] += d[pb];
		}
	}
}


int main()
{
	// Status de erro
	cudaError_t status;

	// Constantes
	const int count = 256;
	const int size = count * sizeof(int);

	// Definindo um array de valores inteiros 
	// Array no host
	int* h = new int[count];

	// Preenchendo o array com elementos
	for (int i = 0; i < count; ++i)
		h[i] = i + 1;

	// Array no device
	int* d;

	// Alocando device memory
	status = cudaMalloc(&d, size);

	// Copiando da memória RAM para a memória do device
	status = cudaMemcpy(d, h, size, cudaMemcpyHostToDevice);

	// Um bloco de thread e o máximo de threads possível em nosso caso, count/2
	sumSingleBlock << <1, count / 2, size >> >(d);

	int result;

	// Devolvendo os elementos do device para a memória RAM
	status = cudaMemcpy(&result, d, sizeof(int), cudaMemcpyDeviceToHost);

	cout << "Soma dos Elementos do array igual a " << result << endl;

	getchar();

	cudaFree(d);
	delete[] h;

	return 0;
}


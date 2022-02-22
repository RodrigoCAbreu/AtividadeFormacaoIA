
#include "cuda_runtime.h"
#include "device_launch_parameters.h"

#include <stdio.h>

void addArrays(int* a, int* b, int* c, int count)
{
	for (int i = 0; i < count; ++i)
		c[i] = a[i] + b[i];
}


void main()
{
	// Constante
	const int count = 5;

	// Arrays
	int a[] = { 1, 2, 3, 4, 5 };
	int b[] = { 100, 200, 300, 400, 500 };

	// Arrays para o resultado
	int c[count];

	// Somar os arrays
	addArrays(a, b, c, count);

	// Imprime os itens do array c
	for (int i = 0; i < count; ++i)
		printf("%d ", c[i]);

	getchar();

}


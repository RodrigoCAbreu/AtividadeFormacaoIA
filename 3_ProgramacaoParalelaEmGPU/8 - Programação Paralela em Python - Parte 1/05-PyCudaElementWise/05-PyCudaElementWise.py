# Avaliando Expressões Element-wise
# Avaliando a combinação linear entre 2 vetores

import pycuda.gpuarray as gpuarray
import pycuda.autoinit
import numpy
from pycuda.curandom import rand as curand
from pycuda.elementwise import ElementwiseKernel
import numpy.linalg as la

# Matrizes
input_vector_a = curand((50,))
input_vector_b = curand((50,))

# Coeficientes
mult_coefficient_a = 2
mult_coefficient_b = 5

# Kernel
# Combinação Linear = 2a + 5b
linear_combination = ElementwiseKernel(
        "float a, float *x, float b, float *y, float *c",
        "c[i] = a*x[i] + b*y[i]",
        "linear_combination")

# Variável para receber o resultado da operação
linear_combination_result = gpuarray.empty_like(input_vector_a)

# Execução do kernel
linear_combination(mult_coefficient_a, input_vector_a, mult_coefficient_b, input_vector_b, linear_combination_result)

# Imprime os resultados
print ("Vetor A =")
print (input_vector_a)

print ("Vetor B = ")
print (input_vector_b)

print ("Vetor Resultante C = ")
print (linear_combination_result)

print ("Verificando o resultado, checando a diferença entre o vetor C e a combinação linear de A e B")
print ("C - (%sA + %sB) = "%(mult_coefficient_a,mult_coefficient_b))
print (linear_combination_result - (mult_coefficient_a*input_vector_a + mult_coefficient_b*input_vector_b))
assert la.norm((linear_combination_result - (mult_coefficient_a*input_vector_a + mult_coefficient_b*input_vector_b)).get()) < 1e-5

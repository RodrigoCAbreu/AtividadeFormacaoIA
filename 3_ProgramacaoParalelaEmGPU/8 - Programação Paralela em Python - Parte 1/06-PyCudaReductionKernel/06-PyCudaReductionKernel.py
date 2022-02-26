# Operações de MapReduce em Paralelo na GPU

# Pacotes
import pycuda.gpuarray as gpuarray
import pycuda.autoinit
import numpy
from pycuda.reduction import ReductionKernel

# Comprimento do vetor
vector_length = 400

# Vetores A e B
input_vector_a = gpuarray.arange(vector_length, dtype = numpy.int)
input_vector_b = gpuarray.arange(vector_length, dtype = numpy.int)

# Operação de redução em paralelo
dot_product = ReductionKernel(numpy.int,
                       arguments = "int *x, int *y",
                       map_expr = "x[i]*y[i]",
                       reduce_expr = "a+b", 
                       neutral = "0")

# Execução do kernel
dot_product = dot_product(input_vector_a, input_vector_b).get()

# Imprime os resultados
print("Matriz A")
print(input_vector_a)

print("Matriz B")
print(input_vector_b)

print("Resultado do Produto A * B")
print(dot_product)


# GPU Array
# Funciona de forma similar ao np.ndarray do Numpy
# GPU Array suporta diversas operações aritméticas e pode ser usado em conjunto com pycuda.cumath e pycuda.curandom

import pycuda.gpuarray as gpuarray
import pycuda.driver as cuda
import pycuda.autoinit
import numpy

# Definindo a matriz em tempo de execução
a_gpu = gpuarray.to_gpu(numpy.random.randn(5,5).astype(numpy.float32))

# Multiplicando a matriz na GOU
a_doubled = (2 * a_gpu).get()

# Imprimindo so resultados
print ("Matriz Original")
print (a_gpu)
print ("Matriz multiplicada por 2 após a execução com GPUARRAY")
print (a_doubled)

# Gerenciamento de Memória na GPU através da muliplicação de 2 matrizes

# Pacotes
import numpy as np
from pycuda import driver, compiler, gpuarray, tools

# Inicializando o device
import pycuda.autoinit

# Kernel
kernel_code_template = """
__global__ void MatrixMulKernel(float *a, float *b, float *c)
{
    int tx = threadIdx.x;
    int ty = threadIdx.y;
    float Pvalue = 0;
    for (int k = 0; k < %(MATRIX_SIZE)s; ++k) {
        float Aelement = a[ty * %(MATRIX_SIZE)s + k];
        float Belement = b[k * %(MATRIX_SIZE)s + tx];
        Pvalue += Aelement * Belement;
    }

    c[ty * %(MATRIX_SIZE)s + tx] = Pvalue;
}
"""

# Define o tamanho da Matriz
MATRIX_SIZE = 5

# Variáveis para armazenar as matrizes na memória do host
a_cpu = np.random.randn(MATRIX_SIZE, MATRIX_SIZE).astype(np.float32)
b_cpu = np.random.randn(MATRIX_SIZE, MATRIX_SIZE).astype(np.float32)
c_cpu = np.dot(a_cpu, b_cpu)

# Variáveis para armazenar as matrizes na memória do device
a_gpu = gpuarray.to_gpu(a_cpu) 
b_gpu = gpuarray.to_gpu(b_cpu)
c_gpu = gpuarray.empty((MATRIX_SIZE, MATRIX_SIZE), np.float32)

# Define o kernel
kernel_code = kernel_code_template % {
    'MATRIX_SIZE': MATRIX_SIZE 
    }

# Compila o kernel
mod = compiler.SourceModule(kernel_code)

# Obtém o kernel
matrixmul = mod.get_function("MatrixMulKernel")

# Executa o kernel
matrixmul(
    a_gpu, b_gpu, 
    c_gpu, 
    block = (MATRIX_SIZE, MATRIX_SIZE, 1),
    )

# Imprime is resultados
print ("-" * 80)
print ("Matriz A (GPU):")
print (a_gpu.get())

print ("-" * 80)
print ("Matriz B (GPU):")
print (b_gpu.get())

print ("-" * 80)
print ("Matriz C (GPU):")
print (c_gpu.get())

print ("-" * 80)
print ("Diferença CPU-GPU:")
print (c_cpu - c_gpu.get())

np.allclose(c_cpu, c_gpu.get())


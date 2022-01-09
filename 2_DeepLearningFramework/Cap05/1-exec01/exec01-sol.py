# TensorFlow - Matrizes e Operações com Matrizes

# Importando os pacotes
import numpy as np
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# Criando uma matriz identidade 2x3
identity_matrix = tf.eye(2, num_columns = 3)
print("\nMatriz Identidade 2x3")
print(identity_matrix)

# Criando uma matriz 2x3 randomicamente normalizada
A = tf.random.truncated_normal([2,3])
print("\nMatriz A - 2x3")
print(A)

# Criando uma matriz 2x3 com valores constantes
B = tf.fill([2,3], 5.0)
print("\nMatriz B - 2x3")
print(B)

# Criando uma matriz 3x2 randomicamente uniforme
C = tf.random.uniform([3,2])
print("\nMatriz C - 3x2")
print(C)

# Convertendo um array numpy 3x3 para um tensor
array1 = np.array([[1., 2., 3.], [-3., -7., -1.], [0., 5., -2.]])
D = tf.convert_to_tensor(array1)
print("\nMatriz D")
print(D)

# Adicione a matriz A com a matriz B
print("\nSoma A + B")
print(A+B)

# Subtraia a matriz B da mesma matriz B
print("\nSubtrai B de B")
print(B-B)

# Multiplicação da Matriz A e C
print("\nMultiplicação de Matriz")
print(tf.matmul(A, C))

# Transposta da matriz C
print("\nTransposta Matriz C")
print(tf.transpose(C)) 

# Determinante da matriz D
print("\nDeterminante D")
print(tf.linalg.det(D))

# Matrix Inversa da matriz D
print("\nInversa da Matriz D")
print(tf.linalg.inv(D))

print('\n')


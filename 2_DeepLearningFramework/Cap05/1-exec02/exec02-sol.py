# Tensores

# Tensores são a estrutura de dados primária que o TensorFlow usa para operar no grafo computacional. 
# Podemos declarar esses tensores como variáveis. 
# Quando criamos um tensor e declaramos que ele é uma variável, o TensorFlow cria várias estruturas de grafo em nosso grafo computacional. 

# Importando os pacotes
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# Cria um tensor preenchido por 20 zeros, dimensão 1x20
my_tensor = tf.zeros([1,20])
print('\nTensor com 20 zeros')
print(my_tensor)

# Declara a variável que recebe um tensor preenchido por 20 zeros
my_var = tf.Variable(tf.zeros([1,20]))
print('\nmy_var')
print(my_var)

# Variáveis Python que podem ser usadas como parâmetro
row_dim = 2
col_dim = 3 

# Tensor inicializado com zeros usando como dimensões as variáveis criadas anteriormente
zero_var = tf.Variable(tf.zeros([row_dim, col_dim]))
print('\nzero_var')
print(zero_var)

# Tensor inicializado com 1's
ones_var = tf.Variable(tf.ones([row_dim, col_dim]))
print('\nones_var')
print(ones_var)

# Tensor preenchido com valores constantes (variáveis Python criadas anteriormente)
fill_var = tf.Variable(tf.fill([row_dim, col_dim], -1))
print('\nfill_var')
print(fill_var)

# Cria um tensor a partir de uma lista de valores constantes
const_var = tf.Variable(tf.constant([8, 6, 7, 5, 3, 0, 9]))
print('\nconst_var')
print(const_var)

# Similar ao anterior, mas usando variáveis Python defindas anteriormente:
const_fill_var = tf.Variable(tf.constant(-1, shape = [row_dim, col_dim]))
print('\nconst_fill_var')
print(const_fill_var)

# Gerando uma sequência de valores lineares com a função tf.linspace, começando por 0.0, terminando em 1.0, com 3 elementos
linear_var = tf.Variable(tf.linspace(start = 0.0, stop = 1.0, num = 3)) 
print('\nlinear_var')
print(linear_var)

# Gerando uma sequência de valores com a função tf.range, começando por 6, limite de 15 e saltando de 3 em 3
sequence_var = tf.Variable(tf.range(start = 6, limit = 15, delta = 3)) 
print('\nsequence_var')
print(sequence_var)

print('\n')





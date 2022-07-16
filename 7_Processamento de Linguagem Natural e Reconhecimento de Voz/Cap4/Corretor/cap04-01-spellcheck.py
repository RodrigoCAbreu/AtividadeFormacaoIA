# Corretor Ortográfico

# Para executar, digite: python cap04-01-spellcheck.py palavras_digitadas.txt dicionario_en.txt

# Imports
import csv
import sys
import time
import random
import numpy as np

# Global Constants
deletion_cost = 1
insertion_cost = 1
substitution_cost = 1

# Encontra a palavra mais próxima
# s = palavra
# dictionary = dicionário de palavras
def find_closest_word(s, dictionary):
  distances = []
  for i in range(0, len(dictionary)):
    # Usando a distância de levenshtein 
    distance = levenshtein_distance(s, dictionary[i], deletion_cost, insertion_cost, substitution_cost)

    if distance == 0:
      return dictionary[i]
    distances.append(distance)
  #print (distances.index(min(distances)))
  return dictionary[distances.index(min(distances))]


# Levenshtein Distance
# s = palavra 1; 
# t = palavra 2
# m = comprimento de s; 
# n = comprimento de t
# deletion_cost, insertion_cost, substitution_cost são fixos

# Função para cálculo da distência de Levenshtein
def levenshtein_distance(s, t, deletion_cost, insertion_cost, substitution_cost):
  first_len, second_len = len(s), len(t)
  if s == t:
    return 0

  if first_len > second_len:
    s, t = t, s
    first_len, second_len = second_len, first_len

  if second_len == 0:
    return first_len

  # Inicializando a matriz com zeros
  d = [[0] * second_len for x in range(first_len)]

  # Definindo valores para a primeira linha e primeira coluna
  for i in range(0, first_len):
    d[i][0] = i * deletion_cost
  for j in range(0, second_len):
    d[0][j] = j * insertion_cost

  for j in range(1, second_len):
    for i in range(1, first_len):
      if s[i] == t[j]:
        d[i][j] = d[i - 1][j - 1]
      else:
        d[i][j] = min(d[i - 1][j] + deletion_cost, d[i][j - 1] + insertion_cost, d[i - 1][j - 1] + substitution_cost) + 1

  return d[first_len - 1][second_len - 1]

# Media de Erro
# Comparação entre o erro de digitação e a palavra verdadeira
def measure_error(typos, true_words, dictionary):
  error_count = 0
  start = time.time()
  for i in range(0, len(typos)):
    closest_word = find_closest_word(typos[i], dictionary)
    true_word = true_words[i]
    if ',' in true_word:
      true_word_arr = true_word.split(',')
      has_match = False
      for x in range(0, len(true_word_arr)):
        word = true_word_arr[x].strip()
        if closest_word == word:
          has_match = True 
          break
      if has_match:
        print ('Palavra sem erro de digitação: ' + closest_word)
      else:
        print ('Erro de digitação detectado: ' + typos[i] + '. Palavra correta: ' + true_word)
        error_count = error_count + 1
    elif ' ' in true_word:
      true_word_arr = true_word.split(' ')
      has_match = False
      for x in range(0, len(true_word_arr)):
        word = true_word_arr[x].strip()
        if closest_word == word:
          has_match = True 
          break
      if has_match:
        print ('Palavra sem erro de digitação: ' + closest_word)
      else:
        print ('Erro de digitação detectado: ' + typos[i] + '. Palavra correta: ' + true_word)
        error_count = error_count + 1

    else:
      if closest_word == true_word:
        print ('Palavra sem erro de digitação: ' + closest_word)
      else:
        print ('Erro de digitação detectado: ' + typos[i] + '. Palavra correta: ' + true_word)
        error_count = error_count + 1
  print ('Taxa de erro de ' + str(float(error_count) / len(typos)))
  print ('Tempo de cálculo foi de ' + str(time.time() - start) + ' segundos')


def main():
  args = sys.argv[1:]

  if len(args) != 2:
    print ('Por favor digite: python cap04-01-spellcheck.py <arquivo a ser corrigido> <dicionário de palavras>')
    sys.exit(1)

  filename = args[0]
  dict_word_list = args[1]

  words = [] 
  typos = []
  true_words = []
  
  with open(dict_word_list, 'r') as word_dict_file:
    words = [line.strip() for line in word_dict_file]

  with open(filename, 'r') as target_file:
    for line in target_file:
      typos.append(line.split('\t')[0].strip())
      true_words.append(line.split('\t')[1].strip())

  random_indices = random.sample(range(1, len(typos)), 100)
  random_typos = [ typos[i] for i in random_indices ]
  random_true_words = [ true_words[i] for i in random_indices ]

  # Por default, a taxa de erros é calculada em uma amostra de 100 palavras.
  # Caso queira calcular a taxa de erros em todo o dataset, comente esta linha abaixo e descomente a próxima
  measure_error(random_typos, random_true_words, words)
  #measure_error(typos, true_words, words)


if __name__ == '__main__':
  main()


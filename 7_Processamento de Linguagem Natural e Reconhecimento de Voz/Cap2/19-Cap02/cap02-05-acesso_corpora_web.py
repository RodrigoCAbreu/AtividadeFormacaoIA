# Acessando um Corpora a Partir da Web
# Download do dataset: http://www.cs.cornell.edu/people/pabo/movie-review-data/mix20_rand700_tokens_cleaned.zip

# Import
# Como este Corpous já está categorizado, carregar e ler o Corpus diretamente com a função CategorizedPlaintextCorpusReader
from nltk.corpus import CategorizedPlaintextCorpusReader
from random import randint

# Carregando o arquivo e imprimindo catefgorias e ids dos arquivos
# Usamos expressões regulares para buscar padrões nos nomes dos arquivos
reader = CategorizedPlaintextCorpusReader(r'/home/dmpm/FIA/PLN/Cap02/movie_reviews_tokens/tokens', r'.*\.txt', cat_pattern=r'(\w+)/*')
print(reader.categories())
print(reader.fileids())

# Separa os arquivos das duas categorias
posFiles = reader.fileids(categories='pos')
negFiles = reader.fileids(categories='neg')

# Selecionamos randomicamente arquivos de cada categoria
fileP = posFiles[randint(0,len(posFiles)-1)]
fileN = negFiles[randint(0, len(posFiles) - 1)]
print(fileP)
print(fileN)

# Imprimimos as palavras do arquivo escolhido
for w in reader.words(fileP):
    print(w + ' ', end='')
    if (w is '.'):
        print()


for w in reader.words(fileN):
    print(w + ' ', end='')
    if (w is '.'):
        print()
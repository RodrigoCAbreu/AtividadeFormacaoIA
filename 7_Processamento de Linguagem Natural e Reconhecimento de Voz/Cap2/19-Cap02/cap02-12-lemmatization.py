# Lemmatization

# Lemmatização na linguística, é o processo de agrupar as diferentes formas flexionadas de uma palavra para que possam ser analisadas como um único item.
# Na linguística computacional, a Lemmatização é o processo algorítmico de determinação do lema para uma determinada palavra. 
# Uma vez que o processo pode envolver tarefas complexas, como entender o contexto e determinar a parte da fala de uma palavra em uma frase 
# (requerendo, por exemplo, conhecimento da gramática de uma linguagem), pode ser uma tarefa difícil implementar um lematizador para uma nova língua.

# Em muitas línguas, as palavras aparecem em várias formas inflexíveis. 
# Por exemplo, em inglês, o verbo 'to walk' pode aparecer como 'walk', 'walk', 'walkks', 'walking'. 
# A forma base, 'walk', que se poderia procurar em um dicionário, é chamado de lema para a palavra. 
# A combinação da forma base com a parte da fala geralmente é chamada de lexema da palavra.

# A Lemmatização está intimamente relacionada com o Stemming. 
# A diferença é que um stemmer opera em uma única palavra sem conhecimento do contexto e, portanto, não pode discriminar entre palavras 
# que têm diferentes significados, dependendo da parte da fala. No entanto, os stemmers são geralmente mais fáceis de implementar e executar mais 
# rapidamente, e a precisão reduzida pode não ser importante para algumas aplicações.

# Stemming e Lemmatization são operações parecidas. A principal diferença entre eles é que o Stemmning pode gerar palavras geralmente inexistentes, 
# enquanto as lemas são palavras reais.

# Assim, sua root stem pode não ser algo que você pode procurar em um dicionário, mas você pode procurar um lema. 
# Algumas vezes você terminará com uma palavra muito semelhante, mas as vezes, você terminará com uma palavra completamente diferente. Vamos ver alguns exemplos.

# Imports
from nltk.stem import WordNetLemmatizer

# Lemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

# Com argumentos default
wordnet_lemmatizer.lemmatize('cooking')
wordnet_lemmatizer.lemmatize('dogs')
wordnet_lemmatizer.lemmatize('churches')
wordnet_lemmatizer.lemmatize('are')
wordnet_lemmatizer.lemmatize('is')

# pos = v
wordnet_lemmatizer.lemmatize('is', pos='v')
wordnet_lemmatizer.lemmatize('are', pos='v')
wordnet_lemmatizer.lemmatize('cooking', pos='v')

# Treinando Um Chunker

# Imports
import nltk
from nltk.corpus import conll2000

# Função para testar o chunker RegexpParser do NLTK
def test_regexp():
    # grammar = r"NP: {<[CDJNP].*>+}"
    grammar = '\n'.join([
    'NP: {<DT>*<NNP>}',
    'NP: {<JJ>*<NN>}',
    'NP: {<NNP>+}',
    ])
    cp = nltk.RegexpParser(grammar)
    test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])
    print("Resultado do RegexpParser Chunker:")
    print(cp.evaluate(test_sents))

# Função para treinar um chunker em um corpus
class BigramChunker(nltk.ChunkParserI):
    def __init__(self, train_sents):
        train_data = [[(t,c) for w,t,c in nltk.chunk.tree2conlltags(sent)] for sent in train_sents]
        self.tagger = nltk.BigramTagger(train_data)

    def parse(self, sentence):
        pos_tags = [pos for (word,pos) in sentence]
        tagged_pos_tags = self.tagger.tag(pos_tags)
        chunktags = [chunktag for (pos, chunktag) in tagged_pos_tags]
        conlltags = [(word, pos, chunktag) for ((word,pos),chunktag)
                in zip(sentence, chunktags)]
        return nltk.chunk.conlltags2tree(conlltags)

# Testa o chunker personalizado
def test_mychunker():
    test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])
    train_sents = conll2000.chunked_sents('train.txt', chunk_types=['NP'])
    my_chunker = BigramChunker(train_sents)
    print("\nResultado do Chunker Personalizado:")
    print(my_chunker.evaluate(test_sents))

test_regexp()
test_mychunker()
print("\n")

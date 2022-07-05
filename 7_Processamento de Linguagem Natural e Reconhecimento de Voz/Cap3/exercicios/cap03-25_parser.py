# Parser

# Imports
import nltk

# Parser
def RDParserExample(grammar, textlist):
    parser = nltk.parse.RecursiveDescentParser(grammar)
    for text in textlist:
        sentence = nltk.word_tokenize(text)
        for tree in parser.parse(sentence):
            print(tree)
            tree.draw()

# CFG
grammar = nltk.CFG.fromstring("""
S -> NP VP
NP -> NNP VBZ
VP -> IN NNP | DT NN IN NNP
NNP -> 'Tajmahal' | 'Índia' | 'Havana' | 'Cuba'
VBZ -> 'é'
IN -> 'na' | 'de'
DT -> 'a'
NN -> 'capital'
""")

text = [
    "Tajmahal é na Índia",
    "Havana é a capital de Cuba",
]

RDParserExample(grammar, text)

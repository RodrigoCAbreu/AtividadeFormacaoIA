# Parser Chart

from nltk.grammar import CFG
from nltk.parse.chart import ChartParser, BU_LC_STRATEGY

grammar = CFG.fromstring("""
S -> T1 T4
T1 -> NNP VBZ
T2 -> DT NN
T3 -> IN NNP
T4 -> T3 | T2 T3
NNP -> 'Tajmahal' | 'Índia' | 'Havana' | 'Cuba'
VBZ -> 'é'
IN -> 'na' | 'de'
DT -> 'a'
NN -> 'capital'
""")

cp = ChartParser(grammar, BU_LC_STRATEGY, trace=True)

sentence = "Havana é a capital de Cuba"
tokens = sentence.split()
chart = cp.chart_parse(tokens)
parses = list(chart.parses(grammar.start()))
print("Total Edges :", len(chart.edges()))
for tree in parses: print(tree)
tree.draw()

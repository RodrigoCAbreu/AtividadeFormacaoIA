# Extraindo Vocabulário Comum Entre 2 Textos

story1 = """Em um reino distante, havia um rio. Este rio era o lar de muitos cisnes dourados. Os cisnes passavam a maior parte do tempo nas margens do rio. A cada seis meses, os cisnes deixavam uma pena dourada como taxa de uso do lago. Os soldados do reino recolhiam as penas e as depositavam no tesouro real.
Um dia, um pássaro desabrigado viu o rio. "A água neste rio parece tão legal e calmante. Vou fazer minha casa aqui", pensou o pássaro.
Assim que o pássaro se estabeleceu perto do rio, os cisnes dourados o notaram. Eles vieram gritando. "Este rio pertence a nós. Nós pagamos uma pena dourada ao rei para usar este rio. Você não pode viver aqui".
"Eu sou sem-teto, irmãos. Eu também pagarei o aluguel. Por favor me dê um abrigo", implorou o pássaro. "Como você pagará o aluguel? Você não tem penas douradas", disseram os cisnes rindo. Eles adicionaram, "Pare de sonhar e saia uma vez". O humilde pássaro pediu muitas vezes. Mas os cisnes arrogantes expulsaram o pássaro.
"Eu vou ensinar-lhes uma lição!" decidiu o pássaro humilhado.
Ela foi ao rei e disse: "Ó Rei! Os cisnes em seu rio são descorteses e indecentes. Eu pedi abrigo, mas eles disseram que compraram o rio com penas douradas".
O rei estava bravo com os cisnes arrogantes por ter insultado o pássaro desabrigado. Ele ordenou que seus soldados levassem os cisnes arrogantes para o tribunal. Em pouco tempo, todos os cisnes dourados foram trazidos para a corte do rei.
"Vocês acham que o tesouro real depende das suas penas douradas? Vocês não podem decidir quem mora junto ao rio. Deixem o rio imediatamente ou todos vocês serão decapitados!" gritou o rei.
Os cisnes tremiam de medo ao ouvir o rei. Eles se afastaram para nunca mais voltar. O pássaro construiu sua casa perto do rio e morou lá feliz para sempre. O pássaro deu abrigo a todas as outras aves do rio. """

story2 = """Há muito tempo, vivia um rei. Ele era preguiçoso e gostava de todos os confortos da vida. Ele nunca executou seus deveres como Rei. "Nosso Rei não cuida das nossas necessidades. Ele também ignora os assuntos de seu reino. "O povo se queixou.
Um dia, o rei entrou na floresta para caçar. Depois de ter vagado por algum tempo, ele ficou com sede. Para seu alívio, ele viu um lago. Enquanto ele estava bebendo água, de repente viu um cisne dourado sair do lago e pousar em uma pedra. "Oh! Um cisne dourado. Devo capturá-lo ", pensou o Rei.
Mas assim que ele segurou seu arco, o cisne desapareceu. E o rei ouviu uma voz: "Eu sou o Cisne dourado. Se você quiser me capturar, você deve ir ao céu ".
Surpreendido, o rei disse: "Por favor, mostre-me o caminho para o céu." "Faça boas ações, sirva seu povo e o mensageiro do céu viria buscá-lo para o céu", respondeu a voz.
O rei egoísta, ansioso para capturar o Cisne, tentou fazer algumas boas ações em seu Reino. "Agora, suponho que um mensageiro venha me levar para o céu", pensou ele. Mas, não veio nenhum mensageiro.
O rei então se disfarçou e saiu para a rua. Lá ele tentou ajudar um velho. Mas o velho ficou bravo e disse: "Você não precisa tentar ajudar. Eu estou neste estado miserável por causa do rei egoísta. Ele não fez nada por seu povo ".
De repente, o rei ouviu a voz do cisne dourado: "Faça boas ações e você virá para o céu". Ele percebeu que, fazendo atos egoístas, não irá para o céu.
Ele percebeu que seu povo precisava dele e cumprir seus deveres era o único caminho para o céu. Depois desse dia ele se tornou um rei responsável.
"""

# Removendo caracteres e convertendo para lowercase
story1 = story1.replace(",", "").replace("\n", "").replace('.', '').replace('"', '').replace("!","").replace("?","").casefold()
story2 = story2.replace(",", "").replace("\n", "").replace('.', '').replace('"', '').replace("!","").replace("?","").casefold()

# Divivindo os textos em palavras
story1_words = story1.split(" ")
print("\n")
print("Palavras da Primeira História :", story1_words)
print("\n")
story2_words = story2.split(" ")
print("Palavras da Segunda História :", story2_words)
print("\n")

# Criando um vocabulário (conjunto de palavras sem repetição)
story1_vocab = set(story1_words)
print("Vocabulário da Primeira História :", story1_vocab)
print("\n")
story2_vocab = set(story2_words)
print("Vocabulário da Segunda História", story2_vocab)
print("\n")

# Vocabulário comum
common_vocab = story1_vocab & story2_vocab
print("Vocabulário Comum :", common_vocab)
print("\n")




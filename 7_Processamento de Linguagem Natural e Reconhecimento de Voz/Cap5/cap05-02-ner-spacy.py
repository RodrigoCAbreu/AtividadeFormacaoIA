# Named Entity Recognition com SpaCy

# Import
# pip install spacy
import spacy

# Carrega o idioma
# python -m spacy download pt_core_news_sm
# python -m spacy download pt
nlp = spacy.load('pt')

# Frase
doc = nlp(u'Rio de Janeiro é a capital turística do Brasil.')

# Print das Entidades e suas classes
print ("\n-------Exemplo 1 ------\n")
for ent in doc.ents:
    print(ent.label_, ent.text)

# Frase
doc1 = nlp(u'Enquanto isso na França, Christine Lagarde discutiu os esforços de estímulo de curto prazo em uma '
           u'entrevista recente às 17:00 com o Wall Street Journal')

# Print das Entidades e suas classes
print ("\n-------Exemplo 2 ------\n")
for ent1 in doc1.ents:
    print(ent1.label_, ent1.text)


print ("\n")
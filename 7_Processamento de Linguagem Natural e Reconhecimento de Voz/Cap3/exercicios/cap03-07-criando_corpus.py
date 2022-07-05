# Criando um Corpus

# Imports
import os
import docx
from PyPDF2 import PdfFileReader
from nltk.corpus.reader.plaintext import PlaintextCorpusReader

# Função para obter texto de arquivos DOCX
def getTextWord(wordFileName):
    doc = docx.Document(wordFileName)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

# Função para coletar texto do arquivo pdf
def getTextPDF(pdfFileName, password = ''):
    pdf_file = open(pdfFileName, 'rb')
    read_pdf = PdfFileReader(pdf_file)
    if password != '':
        read_pdf.decrypt(password)
    text = []
    for i in range(0,read_pdf.getNumPages()):
        text.append(read_pdf.getPage(i).extractText())
    return '\n'.join(text)

# Coletar texto de arquivos txt
def getText(txtFileName):
    file = open(txtFileName, 'r')
    return file.read()

# Cria um diretório para o Corpus
newCorpusDir = 'mycorpus/'
if not os.path.isdir(newCorpusDir):
    os.mkdir(newCorpusDir)

# Pega o nome dos arquivos
txt1 = getText('arquivo1.txt')
txt2 = getTextPDF('arquivo1.pdf')
txt3 = getTextWord('arquivo1.docx')

# Nome dos arquivos do Corpus
files = [txt1,txt2,txt3]

# Abre os arquivos do Corpus para escrita
for idx, f in enumerate(files):
    with open(newCorpusDir+str(idx)+'.txt', 'w') as fout:
        fout.write(f)

# Grava o Corpus
newCorpus = PlaintextCorpusReader(newCorpusDir, '.*')

# Print do conteúdo do Corpus
print(newCorpus.words())
print("\n")
print(newCorpus.sents(newCorpus.fileids()[1]))
print("\n")
print(newCorpus.paras(newCorpus.fileids()[0]))
print("\n")

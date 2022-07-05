# Leitura de Arquivos PDF 

# Import
# pip install pypdf2
from PyPDF2 import PdfFileReader

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

# Nome do arquivo
pdfFile = 'arquivo1.pdf'
pdfFileEncrypted = 'arquivo1.protected.pdf'

# Obtendo texto dos arquivos pdf
print('PDF 1: \n', getTextPDF(pdfFile))
print('PDF 2: \n', getTextPDF(pdfFileEncrypted,'tuffy'))
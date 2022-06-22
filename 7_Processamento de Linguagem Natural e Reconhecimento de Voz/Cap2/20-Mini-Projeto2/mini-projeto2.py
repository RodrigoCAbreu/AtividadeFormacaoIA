# App

# Imports
import re
import nltk
from tqdm import tqdm
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

# Função main
def main(email_df, dec_sent):

    # Criamos uma regra para filtar os dados usando expressões regulares
    splitter = re.compile('[^.!?]*[\w]\s*[.!?]')
    
    # Estruturas de controle
    bow = {}
    sentences = []
    total_count = 0
    actionable_sentences = 0

    # Vamos definir um limite de 1000 mensagens para evitar estouro da memória
    LIMIT = 1000 

    # Função para checar se o texto contém palavras acionáveis
    def is_actionable(query):
        
        # Converte para minúsculo
        query = query.lower()
        
        # Lista de palavras que indicam ações
        words = ["?","can you ","would ","should ","please ","will ","could ","what ","what ","who "," how ","where ","when ",
                "do ","list ","document ","send ","forward ","fix ","write ","open ","wait",
                "move ","visit ","make ","listen ","come ","spend ","submit ","build ","bring ","ask ","grab",
                "read ","give ","act ","visit ","think ","drop ","call ","schedule ","accept ","reply ","respond",
                "create ","open ","close ","show ","make ","execute ","perform ","cause ","exercise ","practice",
                "answer ","serve ","manage ","arrange ","set ","name ","count ","get ","direct ","mail ","post",
                "transport ","ship ","commit ","charge ","institutionalize ","institutionalise ","air",
                "broadcast ","transmit ","repair ","restore ","secure ","determine ","define ","specify ","limit",
                "prepare ","ready ","deposit ","situate ","locate ","compose ","indite ","publish ","save",
                "spell ","spread ","unfold ","expect ","look ","await ","scan ","take ","study ","learn",
                "register ","show ","record ","translate ","understand "]
        
        for word in words:
            if word in query:
                if query.count(' ') > 2:
                    return True
        return False

    # Função para separar as sentenças
    def get_message(colln,idx):
        _msg = colln.iloc[idx]['message']
        msgs = _msg.split(':')[-1].split('/n')
        msgs_join = ' '.join(msgs)
        msg_sents = splitter.findall(msgs_join)
        return msg_sents

    # Lista de sentenças
    sentences = []

    # Contadores
    tp = 0
    fp = 0
    fn = 0
    
    # Dicionário e padrões
    pos_dict = {'MD':'1','VB':'2','VBG':'2','VBN':'2','VBP':'2','VBZ':'2','WP':'3'}
    patterns = ['142','12','32','342','242']

    # Função para avaliação
    def evaluate(idf):
        
        if idf[0] == '2':
            return True

        for p in patterns:
            if p in idf:
                return True
        return False

    # Loop para a barra de progressão
    # Aqui definimos nossa heurística (regra)
    for k in tqdm(range(len(email_df))):
        try:

            # Obtém a mensagem de texto do e-mail e verifica o comprimento
            sents_k = get_message(email_df,k)
            total_count += len(sents_k)
            
            # Para cada sentença aplicamos o pós-tag
            for s in sents_k:
                tags = nltk.pos_tag(s.strip().split())
                pos = [item[1] for item in tags]
                key_idf = ''
                
                for p in pos:
                    if p in pos_dict.keys():
                        key_idf += pos_dict[p]
                    else:
                        key_idf += '4'

                gt_sent = evaluate(key_idf)
                
                if is_actionable(s.strip()):
                    sentences.append(s.strip())
                    
                    if gt_sent:
                        tp+=1
                    else:
                        fp+=1
                else:
                    if gt_sent:
                        fn+=1

            if len(sentences) > LIMIT:
                save_results = open('dados/resultados.txt','a+')
                actionable_sentences+=len(sentences)
                
                print('Resultados salvos para ' + str(len(sentences)) + ' linhas.')
                
                results = '\n'.join(sentences)
                save_results.write(results)
                save_results.close()
                sentences = []
        except:
            print('Mensagem não pode ser aberta!')

    # Função para detectar se o e-mail é ou não acionável
    def detect(sen):
        for y in sentences:
            if y in sen:
                return "Acionável"

        return "Não Acionável"

    # Salva o estado do e-mail
    email_df['State'] = email_df['message'].apply(lambda x : detect(x))   

    # Salva os e-mails classificados                                     
    email_df.to_csv('dados/emails_classificados.csv')
    
    # Sumário
    print('\n\n\n============== Sumário ====================\n')
    
    # Calcula as métricas
    precission = (tp) / (tp + fp)
    recall = (tp) / (tp + fn)
    F1 = 2 * precission * recall / (precission+recall)
    
    print('Precision :', precission)
    print('Recall :', recall)
    print('F1 score : ',F1)
    
    save_results = open('dados/resultados.txt','a+')
    
    # Contador de sentenças acionáveis
    actionable_sentences += len(sentences)
    
    print('Resultados salvos para ' + str(len(sentences)) + ' linhas.')
    
    results = '\n'.join(sentences)
    save_results.write(results)
    save_results.close()

    print('Número de Sentenças Acionáveis: ', actionable_sentences)
    print('Total de Sentenças: ', total_count)
    
    return detect(dec_sent)

print("\n--------------------")
print('Digite o total de e-mails que usaremos para treinar nossa heurística (Valor de 1 a 517401).')
print('Obs: com base no total de e-mails, o tempo de processamento pode ser alto!')
print("--------------------\n")

# Recebe o valor do input do usuário
rows = input('Insira o total de e-mails desejados: ')
print("\n")

# Checa o valor digitado e busca no dataset de e-mails da Enron
if rows.isdigit() and int(rows) <= 517401 and int(rows) >= 0:
    
    # Carrega o dataset da Enron    
    email_df = pd.read_csv('dados/emails.csv', nrows = int(rows))
    
    dec_sent = input('Por favor, digite o número do e-mail para detectar se é Acionável ou Não Acionável (Valor de 1 a 517401): ')
    print("\n")
    
    print("Estado do E-mail: ", main(email_df, dec_sent))    
else:
    print('Número Inválido!')
    
print("\nObrigado!\n")
#Imports
import csv
import os

#Listas, Dicionários
contasADM={}
cadastro = []
dadosCadastro = []

#Variáveis Globais
global proceed
global wInicial
global wVolunt
global wMain
global wDonate
global d
global e
global f
global g
global logged

#Valores das Globais
wInicial = True
b = True
wMain = True
d = True
e = True
f = True
g = True
logged = False

#Variáveis de Escolha
escolha_main = 0
escolha_login = 0
escolha_menu = 0
escolha_back = 10

#Limpar Terminal
def limpa():
    os.system('cls')
    
#Cadastro
def escreverDados(nomeArquivo, nomeLista):
    with open(nomeArquivo, 'a') as adm:
        esc = ','.join(nomeLista)
        adm.writelines(esc+'\n')
        
#Tela de Login
def Login(nomeArquivo, nomeDic):
        user = input('Digite o email de login: ')
        senha = input('Digite sua senha: ')
        with open(nomeArquivo,'r') as adm:
            leitor = csv.reader(adm)
            nomeDic = {l[0]:l[1] for l in leitor}
            if user not in nomeDic or nomeDic[user] != senha:
                return False                
            else:
                return True 
#Tela de Cadastro

def Cadastro(nomeArquivo, nomeDic):
    global proceed
    global e
    global f
    global g
    e = True
    user = input('Insira o email para login: ')
    with open(nomeArquivo,'r') as adm:
        leitor = csv.reader(adm)
        nomeDic = {l[0]:l[1] for l in leitor}
    if user not in nomeDic:
        nome = input('Digite seu nome: ')
        cpf = input('Digite seu CPF: ')
        cadastro.append(user)
        dadosCadastro.append(user)
        dadosCadastro.append(nome)
        dadosCadastro.append(cpf)
        while e==True:
            senha = input('Digite sua senha:')
            conf = input('Confirme a senha: ')
            if senha == conf:
                cadastro.insert(1, senha)
                dadosCadastro.insert(1, senha)
                e = False
            else:
                limpa()
                proceed = int(input('''As senhas não coincidem.
[1] - Tentar novamente \t [2] - Voltar \n'''))
                if proceed == 2:
                    limpa()
                    e = False
                    f = False
                    g = False
                    break
# O BOTAO DE VOLTAR NÃO FUNCIONA
# REVER // TENTAR NOVAMENTE FUNCIONA NORMAL
                else:
                    limpa()
                    pass   
        limpa()
        escreverDados('DadosADM.csv', cadastro)
        escreverDados('DadosCadastro.csv',dadosCadastro)
        return True
    else: return False
#def voluntRonda():
 #   if logged == True:

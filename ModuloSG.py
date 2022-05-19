#Imports
import csv
import os

from regex import P

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
def Login():
        user = input('Digite o email de login: ')
        senha = input('Digite sua senha: ')
        with open('DadosADM.csv','r') as adm:
            leitor = csv.reader(adm)
            contasADM = {l[0]:l[1] for l in leitor}
        if user not in contasADM:
            return 'cadastro'
        elif user in contasADM and contasADM[user]!= senha:
            return 'senhaIncorreta'               
        elif user in contasADM and contasADM[user] == senha:
            return True 
        else:
            print('Não foi possível fazer o login') 
            pass
#Tela de Cadastro

def Cadastro():
    global e
    global user
    e = True
    user = input('Insira o email para login: ')
    if user in contasADM:
        return 'jaCadastrado'
    else:
        nome = input('Digite seu nome: ')
        cpf = input('Digite seu CPF: ')
        cadastro.append(user)
        dadosCadastro.append(user)
        dadosCadastro.append(nome)
        dadosCadastro.append(cpf)
        while e:
            if conferirSenhaReg() == True: 
                limpa()
                escreverDados('DadosADM.csv', cadastro)
                escreverDados('DadosCadastro.csv',dadosCadastro)
                e = False
                return True  
            elif conferirSenhaReg() == False:
                e = False
                return 'senhaNaoCoincide'
            


#Conf = Senha?
def conferirSenhaReg():
    senha = input('Digite sua senha:')
    conf = input('Confirme a senha: ')
    if senha == conf:
        cadastro.insert(1, senha)
        dadosCadastro.insert(1, senha)            
        return True  
    else:
        limpa()
        return False

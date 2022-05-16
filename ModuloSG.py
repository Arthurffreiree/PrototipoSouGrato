#Imports
import csv
import os

#Listas, Dicionários
contasADM={}
cadastro = []
dadosCadastro = []

#Variáveis Globais
global proceed
global a
global b
global c
global d
global e
global f
global g
global logged

#Valores das Globais
a = True
b = True
c = True
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
    global f
    global proceed
    global logged
    global b
    global d
    global g
    with open(nomeArquivo,'r') as adm:
        leitor = csv.reader(adm)
        nomeDic = {l[0]:l[1] for l in leitor}
        while d == True:
            user = input('Digite o email de login: ')
            if user not in nomeDic:
                limpa()
                print('Login inválido')                  
                escolha_voltar = int(input('[1] - Tentar novamente \t [2] - Voltar \n'))
                if escolha_voltar == 2:
                    d = False
                    f = False
                    limpa()
            else:
                senha = input('Digite sua senha: ')
                if nomeDic[user] != senha:          
                    print('Senha inválida!')              
                    escolha_voltar = int(input('[1] - Tentar novamente \t [2] - Voltar \n'))
                    if escolha_voltar == 2:
                        g = False
                        d = False
                        f = False
                        limpa()
                else:
                    f = False
                    g = False
                    d = False
                    limpa()
                    proceed = input('''Login feito com sucesso!
pressione enter para continuar...''') 
                    logged = True
#Tela de Cadastro
def Cadastro(nomeArquivo, nomeDic):
    global b
    global e
    global g
    global proceed
    global logged
    with open(nomeArquivo,'r') as adm:
        leitor = csv.reader(adm)
        nomeDic = {l[0]:l[1] for l in leitor}
    user = input('Insira o email para login: ')
    if user in nomeDic:
        limpa()
        print('Email já cadastrado.')
        proceed = input("\nPressione enter para continuar...")
        b = False
        limpa()
    else:
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
                proceed = input('''As senhas não correspondem.
Pressione enter para continuar...''')
        limpa()
        escreverDados('DadosADM.csv', cadastro)
        escreverDados('DadosCadastro.csv',dadosCadastro)
        g = False
        b = False
        logged = True    
#def voluntRonda():
 #   if logged == True:
-

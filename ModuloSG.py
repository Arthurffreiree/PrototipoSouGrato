#Imports
import csv
import os
from tkinter import Menu

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
global logged

#Valores das Globais
a = True
b = True
c = True
d = True
e = True
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
        
#Verificar se Login Existe
def loginReader(nomeArquivo, nomeDic):
     with open(nomeArquivo,'r') as adm:
        leitor = csv.reader(adm)
        nomeDic = {l[0]:l[1] for l in leitor}
        
#Tela de Login
def Login(nomeDic):
        loginReader('DadosADM.csv', contasADM)
        user = input('Digite o email de login: ')
        if user not in nomeDic:
            print('Login inválido')
            limpa()
            escolha_voltar = int(input('[1] - Tentar novamente \t [2] - Voltar \n'))
            if escolha_voltar == 2:
                b = False
                limpa()
        else:
            senha = input('Digite sua senha: ')
            if nomeDic[user] != senha:          
                print('Senha inválida!')
                proceed = input("\nPressione enter para continuar...")
                limpa()
                escolha_voltar = int(input('[1] - Tentar novamente \t [2] - Voltar \n'))
                if escolha_voltar == 2:
                    b = False
                    limpa()
            else:
                logged = True
                b = False
                limpa()        
                    
#Tela de Cadastro
def Cadastro(nomeDic):
    loginReader('DadosADM.csv',contasADM)
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
        cadastro.append(nome)
        dadosCadastro.append(nome)
        dadosCadastro.append(cpf)
        while e==True:
            senha = input('Digite sua senha:')
            conf = input('Confirme a senha: ')
            if senha == conf:
                cadastro.append(senha)
                dadosCadastro.append(senha)
                e = False
            else:
                limpa()
                procd = input('''As senhas não correspondem.
Pressione enter para continuar...''')
        limpa()
        escreverDados('DadosADM', cadastro)
        escreverDados('DadosCadastro.csv',dadosCadastro)    
        

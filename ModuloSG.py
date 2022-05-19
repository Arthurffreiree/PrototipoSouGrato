import csv
from glob import glob
import os

global wMain
global logged
global wEscolha2
global wMenu
global wReg
global wVolunt
global wDonate
global wFreq
global wLogDonate

wMain = True
logged = False
wEscolha2 = True
wMenu = True
wReg = True
wVolunt = True
wDonate = True
wFreq = True
wLogDonate = True

nomeDic = {}
dadosCadastro = []
cadastro = []

def limpa():
    os.system('cls')

def escreverCadastro(nomeArquivo, nomeLista):
    with open(nomeArquivo, 'a') as adm:
        esc = ','.join(nomeLista)
        adm.writelines(esc + '\n')

def Login():
    limpa()
    user = input('Digite o email de Login: ')
    senha = input('Digite sua senha: ')
    with open('DadosLogin.csv','r') as adm:
        leitor = csv.reader(adm)
        nomeDic = {l[0]:l[1] for l in leitor}
        if user not in nomeDic or nomeDic[user] != senha:
            return False               
        else:
            return True

def Cadastro():
    global user
    
    wSenha = True
    wCadastro = True

    while wCadastro:
        limpa()
        user = input('Digite seu email de Login: ')
        nome = input('Digite seu nome: ')
        cpf = input('Digite seu cpf: ')
        with open('DadosLogin.csv','r') as adm:
            leitor = csv.reader(adm)
            nomeDic = {l[0]:l[1] for l in leitor}
            if user in nomeDic:
                print('Usuário já cadastrado!')
                escolha = int(input('[1] - Tentar novamente\n[0] - Voltar\n'))
                if escolha == 0:
                    wCadastro = False
            else:
                while wSenha:
                    senha = input('Digite sua senha: ')
                    confsenha = input('Confirme sua senha: ')
                    if senha == confsenha:
                        cadastro.append(user)
                        cadastro.append(senha)
                        dadosCadastro.append(user)
                        dadosCadastro.append(senha)
                        dadosCadastro.append(nome)
                        dadosCadastro.append(cpf)
                        escreverCadastro('DadosLogin.csv', cadastro)
                        escreverCadastro('DadosCadastro.csv',dadosCadastro)
                        wSenha = False
                        return True
                    else:
                        print('As senhas não coincidem.')
                        escolha = int(input('[1] - Tentar novamente\n[0] - Voltar\n'))
                        if escolha == 0:
                            wSenha = False
                            wCadastro = False

def TextoSG():
    limpa()
    print('''O Sou Grato é uma Iniciativa social sem fins lucrativos que surgiu em 2018 com o propósito de 
ajudar pessoas em situação de rua e famílias em vulnerabilidade. Atualmente, as ações do grupo são realizadas 
semanalmente no município de Recife-PE, no qual são distribuídos alimentos, água, ração para cães e gatos, 
kits de higiene pessoal, roupas e cobertores. Outros tipos de ações também são realizadas em parceria com outras 
iniciativas e instituições sociais para assistir comunidades em situações emergenciais.''')
#Tentar colocar isso em um TXT
    proceed = input("\nPressione enter para continuar...")
    limpa()

def Volunt():
    wVolunt = True
    limpa()
    while wVolunt:
        wReg = True
        print("Qual tipo de voluntário você deseja ser?")
        vol = int(input('''[1] - Voluntário de Ronda\n[2] - Voluntário Especializado\n[0] - Voltar\n
Atenção: Ao se inscrever como voluntário, você concorda em disponibilizar
seu nome, email e cpf para a criação de uma conta no sistema Sou Grato \x1B[2A \x1B[75D'''))
        limpa()
        while wReg:
            if vol == 0:
                limpa()
                wReg = False
                wVolunt = False
            elif vol == 1:
                dadosRonda = []
                dadosRonda.append(input("Digite seu nome: "))
                dadosRonda.append(input("Digite seu email: "))
                dadosRonda.append(input("Digite o seu número de telefone: "))
                dadosRonda.append(input("Digite o nome do seu contato de emergência: "))
                dadosRonda.append(input("Digite o número de telefone do seu contato de emergência: "))
                limpa()
                proceed = input("Pressione enter para continuar...")
                escreverCadastro('DadosSGRonda.csv', dadosRonda)
                limpa()
                wVolunt = False
                wReg = False
                wMenu = False
            elif vol == 2:
                dadosEspec = []
                dadosEspec.append(input("Digite seu nome: "))
                dadosEspec.append(input("Digite seu email: "))
                dadosEspec.append(input("Digite o seu número de telefone: "))
                limpa()
                dadosEspec.append(input("Insira o seu grau de escolaridade: "))
                dadosEspec.append(input("Insira sua área de interesse: "))
                dadosEspec.append(input("Alguma proposta?\n"))
                limpa()
                proceed = input("Pressione enter para continuar...")
                escreverCadastro('DadosSGEspec.csv', dadosEspec)
                limpa()
                wVolunt = False
                wReg = False
                wMenu = False

def DonateNotLogged():
    wDonate = True
    while wDonate:
        limpa()
        print("Com que frequência você deseja doar?")
        freqDoacao = int(input("[1] - Mensalmente\n[2] - Doação única\n[0] - Voltar\n"))
        wFreq = True
        while wFreq:
            if freqDoacao == 0:
                limpa()
                wFreq = False
                wDonate = False
            elif freqDoacao == 1:
                limpa()
                wLogDonate = True
                while wLogDonate:
                    escolha_login = int(input('[1] - Login \t [2] - Cadastrar-se \t [0] - Voltar\n'))
                    if escolha_login == 0:
                        limpa()
                        wFreq = False    
                        wLogDonate = False
                    elif escolha_login == 1:
                        if Login() == True:
                            limpa()
                            print('Pix ou Cartão aqui...')
                            proceed = input('\nPressione enter para continuar...')
                            wLogDonate = False
                            wFreq = False
                            return True
                        else:
                            limpa()
                            print('Login inválido!')
                            proceed = input("\nPressione enter para continuar...")
                            limpa()
                    elif escolha_login == 2:
                        if Cadastro() == True:
                            limpa()
                            print('Cadastro realizado com sucesso!')
                            proceed = input('\nPressione enter para continuar...')
                            limpa()
                            print('Pix ou Cartão aqui...')
                            proceed = input('\nPressione enter para continuar...')
                            wLogDonate = False
                            wFreq = False
                            return True
                        else:
                            limpa()
                            print('Não foi possível concluir seu cadastro!')
                            proceed = input("\nPressione enter para continuar...")
                            limpa()

            
            elif freqDoacao == 2:
                limpa()
                print("pix ou cartão aqui")
                proceed = input("\nPressione enter para continuar...")
                wFreq = False
                limpa()

def DonateLogged():
    wDonate = True
    while wDonate:
        limpa()
        print("Com que frequência você deseja doar?")
        freqDoacao = int(input("[1] - Mensalmente\n[2] - Doação única\n[0] - Voltar\n"))
        wFreq = True
        while wFreq:
            if freqDoacao == 0:
                limpa()
                wFreq = False
                wDonate = False
            elif freqDoacao == 1:
                limpa()
                print('Pix ou Cartão aqui...')
                proceed = input('\nPressione enter para continuar...')
                wFreq = False
            elif freqDoacao == 2:
                limpa()
                print("pix ou cartão aqui")
                proceed = input("\nPressione enter para continuar...")
                wFreq = False
                limpa()
import csv
import os
def limpa():
    os.system('cls')

'''Mudar para "not logado" e apenas "logado" '''

# Função para chamar a escrita dos dados
def escreverDados(DadosSougrato, Dados):
    with open(DadosSougrato, 'a') as texto:
        banco = ','.join(Dados)
        texto.writelines(banco+'\n')

def cadastroADM(DadosADM, contas):
    with open(DadosADM, 'a') as texto:
        banco = ','.join(contas)
        texto.writelines(banco+'\n')
# Variáveis para ciclos
a = True
b = True
c = True
d = True
# Verificações
logado = False

# Variáveis para escolhas
escolha_inicio = 0
escolha_login = 0
escolha_menu = 0

# Listas/Dicionários
contasADM = {}

# Variáveis para contagem
contRonda = 0
contEspec = 0

#Tela inicial

while a == True:
    if logado == False:
        limpa()
        escolha_inicio = int(input('[1] - Acessar o menu \t [2] - Login/Cadastro \n'))
        b = True
        c = True
    if logado == True:
        limpa()
        escolha_inicio = int(input('[1] - Acessar o menu \t [2] - Acessar seu perfil \t [3] - Logout\n'))
        c = True
    # Menu
    if escolha_inicio == 1:
        while c == True:
            limpa()
            escolha_menu = int(input('[0] - Voltar \n[1] - Quem somos \n[2] - Seja voluntário \n[3] - Seja doador \n'))
            if escolha_menu == 0:
                limpa()
                c = False
            elif escolha_menu == 1:
                limpa()
                print('''O Sou Grato é uma Iniciativa social sem fins lucrativos que surgiu em 2018 com o propósito de 
ajudar pessoas em situação de rua e famílias em vulnerabilidade. Atualmente, as ações do grupo são realizadas 
semanalmente no município de Recife-PE, no qual são distribuídos alimentos, água, ração para cães e gatos, 
kits de higiene pessoal, roupas e cobertores. Outros tipos de ações também são realizadas em parceria com outras 
iniciativas e instituições sociais para assistir comunidades em situações emergenciais.''')
                continuar = input("\nPressione enter para continuar...")
                limpa()
            elif escolha_menu == 2:
                limpa()
                print("Qual tipo de voluntário você deseja ser?")
                vol = int(input("[1] - Voluntário de Ronda\n[2] - Voluntário Especializado\n[0] - Voltar\n"))
                limpa()
                if vol == 0:
                    limpa()
                    c = False
                elif vol == 1:
                    dadosRonda = []
                    dadosRonda.append(input("Digite seu nome: "))
                    dadosRonda.append(input("Digite seu email: "))
                    dadosRonda.append(input("Digite o seu número de telefone: "))
                    dadosRonda.append(input("Digite o nome do seu contato de emergência: "))
                    dadosRonda.append(input("Digite o número de telefone do seu contato de emergência: "))
                    limpa()
                    continuar = input("Pressione enter para continuar...")
                    escreverDados('DadosSGRonda.csv', dadosRonda)
                    contRonda+=1
                    limpa()
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
                    continuar = input("Pressione enter para continuar...")
                    escreverDados('DadosSGEspec.csv', dadosEspec)
                    contEspec+=1
                    limpa()
            elif escolha_menu==3:
                limpa()
                print("Com que frenquência você deseja doar?")
                freqDoacao = int(input("[1] - Mensalmente\n[2] - Doação única\n[0] - Voltar\n"))
                d = True
                while d == True:
                    if freqDoacao == 0:
                        limpa()
                        d = False
                    elif freqDoacao == 1:
                        limpa()
                        if not logado:
                            escolha_login = int(input('[1] - Login \t [2] - Cadastrar-se \t [0] - Voltar\n'))
                            if escolha_login == 0:
                                limpa()
                                d = False
                            elif escolha_login == 1:
                                while b:
                                    limpa()
                                    with open('DadosADM.csv', 'r') as adm:
                                        dadosADM = csv.reader(adm)
                                        contasADM = {l[0]:l[1] for l in dadosADM}
                                        login = input('Digite seu login: ')
                                        if login not in contasADM:
                                            print('Login inválido!')
                                            limpa()
                                            escolha_voltar = int(input('[1] - Tentar novamente \t [2] - Voltar \n'))
                                            if escolha_voltar == 2:
                                                b = False
                                                limpa()
                                        else:
                                            senha = input('Digite sua senha: ')
                                            if contasADM[login] != senha:
                                                print('Senha inválida!')
                                                continuar = input("\nPressione enter para continuar...")
                                                limpa()
                                                escolha_voltar = int(input('[1] - Tentar novamente \t [2] - Voltar \n'))
                                                if escolha_voltar == 2:
                                                    b = False
                                                    limpa()
                                            else:
                                                logado = True
                                                b = False
                            elif escolha_login == 2:
                                while b == True:
                                    cadastro = []
                                    limpa()
                                    cadastro_usuario = input('Digite o login desejado: ')
#dar uma olhada nessa parte do usuario da cadastrado
#nao ta funcionando
                                    with open('DadosADM.csv', 'r') as adm:
                                        cadRead = csv.reader(adm, delimiter=',')
                                        contasADM ={l[0]:l[1] for l in cadRead}                    
                                        if cadastro_usuario in (contasADM(l[0]) for l in cadRead):
                                            limpa()
                                            print('Usuário já cadastrado!')
                                            escolha_voltar = int(input('[1] - Tentar novamente \t [2] - Voltar \n'))
                                            if escolha_voltar == 2:
                                                b = False
                                                limpa()
                                        else:
                                            cadastro_senha = input('Digite a senha desejada: ')
                                            cadastro.append(cadastro_usuario)
                                            cadastro.append(cadastro_senha)
                                            cadastroADM('DadosADM.csv', cadastro)
                                            limpa()
                                            logado = True
                                            b = False
    #/\/\/\Tentei fazer ele ir direto do login/cadastro pra tela da doação, mas ele volta pro menu 
                        elif logado == True:
                            limpa()
                            print("pix ou cartao aqui")
                            d = False
                            continuar = input("\nPressione enter para continuar...")
                            limpa()
                    elif freqDoacao == 2:
                        limpa()
                        print("pix ou cartão aqui")
                        continuar = input("\nPressione enter para continuar...")
                        d = False
                        limpa()
    # Tela de login
    if escolha_inicio == 2 and logado == False:
        limpa()
        escolha_login = int(input('[1] - Login \t [2] - Cadastrar-se \t [0] - Voltar\n'))
        if escolha_login == 0:
            limpa()
            c = False
        elif escolha_login == 1:
            while b == True:
                limpa()
                with open('DadosADM.csv', 'r') as adm:
                    dadosADM = csv.reader(adm)
                    contasADM = {l[0]:l[1] for l in dadosADM}
                    login = input('Digite seu login: ')
                    if login not in contasADM:
                        print('Login inválido!')
                        continuar = input("\nPressione enter para continuar...")
                        limpa()
                        escolha_voltar = int(input('[1] - Tentar novamente \t [2] - Voltar \n'))
                        if escolha_voltar == 2:
                            b = False
                            limpa()
                    else:
                        senha = input('Digite sua senha: ')
                        if contasADM[login] != senha:
                            print('Senha inválida!')
                            continuar = input("\nPressione enter para continuar...")
                            limpa()
                            escolha_voltar = int(input('[1] - Tentar novamente \t [2] - Voltar \n'))
                            if escolha_voltar == 2:
                                b = False
                                limpa()
                        else:
                            logado = True
                            b = False
        elif escolha_login == 2:
            while b == True:
                cadastro = []
                limpa()
                cadastro_usuario = input('Digite o login desejado: ')
                if cadastro_usuario in contasADM:
                    limpa()
                    print('Usuário já cadastrado!')
                    continuar = input("\nPressione enter para continuar...")
                    limpa()
                    escolha_voltar = int(input('[1] - Tentar novamente \t [2] - Voltar \n'))
                    if escolha_voltar == 2:
                        b = False
                        limpa()
                else:
                    cadastro_senha = input('Digite a senha desejada: ')
                    cadastro.append(cadastro_usuario)
                    cadastro.append(cadastro_senha)
                    cadastroADM('DadosADM.csv', cadastro)
                    limpa()
                    logado = True
                    b = False
    elif escolha_inicio == 3:
        logado = False

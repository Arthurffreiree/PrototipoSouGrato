import csv
import os

os.system('cls')

# Função para chamar a escrita dos dados
def escreverDados(DadosSougrato, Dados):
    with open(DadosSougrato, 'a') as texto:
        banco = ' , '.join(Dados)
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
        os.system('cls')
        escolha_inicio = int(input('[1] - Acessar o menu \t [2] - Login/Cadastro \n'))
        b = True
        c = True
    if logado == True:
        os.system('cls')
        escolha_inicio = int(input('[1] - Acessar o menu \t [2] - Acessar seu perfil \t [3] - Logout\n'))
        c = True
    # Menu
    if escolha_inicio == 1:
        while c == True:
            os.system('cls')
            escolha_menu = int(input('[0] - Voltar \n[1] - Quem somos \n[2] - Seja voluntário \n[3] - Seja doador \n'))
            if escolha_menu == 0:
                os.system('cls')
                c = False
            elif escolha_menu == 1:
                os.system("cls")
                print('''O Sou Grato é uma Iniciativa social sem fins lucrativos que surgiu em 2018 com o propósito de 
ajudar pessoas em situação de rua e famílias em vulnerabilidade. Atualmente, as ações do grupo são realizadas 
semanalmente no município de Recife-PE, no qual são distribuídos alimentos, água, ração para cães e gatos, 
kits de higiene pessoal, roupas e cobertores. Outros tipos de ações também são realizadas em parceria com outras 
iniciativas e instituições sociais para assistir comunidades em situações emergenciais.''')
                continuar = input("\nPressione enter para continuar...")
                os.system("cls")
            elif escolha_menu == 2:
                os.system("cls")
                print("Qual tipo de voluntário você deseja ser?")
                vol = int(input("[1]Voluntário de Ronda\n[2]Voluntário Especializado\n"))
                os.system("cls")
                if vol == 1:
                    dadosRonda = []
                    dadosRonda.append(input("Digite seu nome: "))
                    dadosRonda.append(input("Digite seu email: "))
                    dadosRonda.append(input("Digite o seu número de telefone: "))
                    dadosRonda.append(input("Digite o nome do seu contato de emergência: "))
                    dadosRonda.append(input("Digite o número de telefone do seu contato de emergência: "))
                    os.system("cls")
                    continuar = input("\nPressione enter para continuar...")
                    escreverDados('DadosSGRonda.csv', dadosRonda)
                    contRonda+=1
                    os.system("cls")
                elif vol == 2:
                    dadosEspec = []
                    dadosEspec.append(input("Digite seu nome: "))
                    dadosEspec.append(input("Digite seu email: "))
                    dadosEspec.append(input("Digite o seu número de telefone: "))
                    os.system("cls")
                    dadosEspec.append(input("Insira o seu grau de escolaridade: "))
                    dadosEspec.append(input("Insira sua área de interesse: "))
                    dadosEspec.append(input("Alguma proposta?\n"))
                    continuar = input("\nPressione enter para continuar...")
                    escreverDados('DadosSGEspec.csv', dadosEspec)
                    contEspec+=1
                    os.system("cls")
            elif escolha_menu==3:
                os.system("cls")
                print("Com que frenquência você deseja doar?")
                freqDoacao = int(input("[1]-Mensalmente\n[2]-Doação única\n"))
                while d == True:
                    if freqDoacao == 1:
                        os.system("cls")
                        if logado == False:
                            escolha_login = int(input('[1] - Login \t [2] - Cadastrar-se \n'))
                            if escolha_login == 1:
                                while b == True:
                                    os.system('cls')
                                    with open('DadosADM.csv', 'r') as adm:
                                        dadosADM = csv.reader(adm)
                                        contasADM = {l[0]:l[1] for l in dadosADM}
                                        login = input('Digite seu login: ')
                                        if login not in contasADM:
                                            print('Login inválido!')
                                            continuar = input("\nPressione enter para continuar...")
                                            'DadosADM.csv'.close()
                                            os.system('cls')
                                            escolha_voltar = int(input('[1] - Tentar novamente \t [2] - Voltar \n'))
                                            if escolha_voltar == 2:
                                                b = False
                                                os.system('cls')
                                        else:
                                            senha = input('Digite sua senha: ')
                                            if contasADM[login] != senha:
                                                print('Senha inválida!')
                                                continuar = input("\nPressione enter para continuar...")
                                                os.system('cls')
                                                escolha_voltar = int(input('[1] - Tentar novamente \t [2] - Voltar \n'))
                                                if escolha_voltar == 2:
                                                    b = False
                                                    os.system('cls')
                                            else:
                                                logado = True
                                                b = False
                            elif escolha_login == 2:
                                while b == True:
                                    cadastro = []
                                    os.system('cls')
                                    cadastro_usuario = input('Digite o login desejado: ')
                                    if cadastro_usuario in contasADM:
                                        os.system('cls')
                                        print('Usuário já cadastrado!')
                                        continuar = input("\nPressione enter para continuar...")
                                        os.system('cls')
                                        escolha_voltar = int(input('[1] - Tentar novamente \t [2] - Voltar \n'))
                                        if escolha_voltar == 2:
                                            b = False
                                            os.system('cls')
                            else:
                                cadastro_senha = input('Digite a senha desejada: ')
                                cadastro.append(cadastro_usuario)
                                cadastro.append(cadastro_senha)
                                cadastroADM('DadosADM.csv', cadastro)
                                os.system('cls')
                                logado = True
                                b = False
    #/\/\/\Tentei fazer ele ir direto do login/cadastro pra tela da doação, mas ele volta pro menu 
    #\/\/\/ tá bugado, dá uma conferida
                        if logado == True:
                            os.system("cls")
                            print("pix ou cartao aqui")
                            d == False
                            continuar = input("\nPressione enter para continuar...")
                            os.system('cls')
                    elif freqDoacao == 2:
                        os.system("cls")
                        print("pix ou cartão aqui")
                        d == False
                        continuar = input("\nPressione enter para continuar...")
                        os.system('cls')
    # Tela de login
    if escolha_inicio == 2 and logado == False:
        os.system('cls')
        escolha_login = int(input('[1] - Login \t [2] - Cadastrar-se \n'))
        if escolha_login == 1:
            while b == True:
                os.system('cls')
                with open('DadosADM.csv', 'r') as adm:
                    dadosADM = csv.reader(adm)
                    contasADM = {l[0]:l[1] for l in dadosADM}
                    login = input('Digite seu login: ')
                    if login not in contasADM:
                        print('Login inválido!')
                        continuar = input("\nPressione enter para continuar...")
                        'DadosADM.csv'.close()
                        os.system('cls')
                        escolha_voltar = int(input('[1] - Tentar novamente \t [2] - Voltar \n'))
                        if escolha_voltar == 2:
                            b = False
                            os.system('cls')
                    else:
                        senha = input('Digite sua senha: ')
                        if contasADM[login] != senha:
                            print('Senha inválida!')
                            continuar = input("\nPressione enter para continuar...")
                            os.system('cls')
                            escolha_voltar = int(input('[1] - Tentar novamente \t [2] - Voltar \n'))
                            if escolha_voltar == 2:
                                b = False
                                os.system('cls')
                        else:
                            logado = True
                            b = False
        elif escolha_login == 2:
            while b == True:
                cadastro = []
                os.system('cls')
                cadastro_usuario = input('Digite o login desejado: ')
                if cadastro_usuario in contasADM:
                    os.system('cls')
                    print('Usuário já cadastrado!')
                    continuar = input("\nPressione enter para continuar...")
                    os.system('cls')
                    escolha_voltar = int(input('[1] - Tentar novamente \t [2] - Voltar \n'))
                    if escolha_voltar == 2:
                        b = False
                        os.system('cls')
                else:
                    cadastro_senha = input('Digite a senha desejada: ')
                    cadastro.append(cadastro_usuario)
                    cadastro.append(cadastro_senha)
                    cadastroADM('DadosADM.csv', cadastro)
                    os.system('cls')
                    logado = True
                    b = False
    elif escolha_inicio == 3:
        logado = False

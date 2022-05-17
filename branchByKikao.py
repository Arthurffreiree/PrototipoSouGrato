from PROTOmod import *

#Tela Inicial
while a == True:
    if logged == False:
        limpa()
        escolha_main = int(input('[1] - Acessar o menu \t [2] - Login/Cadastro \n'))
        b = True
        c = True
    if logged == True:
        limpa()
        escolha_main = int(input('[1] - Acessar o menu \t [2] - Acessar seu perfil \t [3] - Logout\n'))
        c = True
# Menu
    if escolha_main == 1:
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
                proceed = input("\nPressione enter para continuar...")
                limpa()
            elif escolha_menu == 2:
                f = True
                limpa()
                while f:
                    b = True
                    print("Qual tipo de voluntário você deseja ser?")
                    vol = int(input('''[1] - Voluntário de Ronda\n[2] - Voluntário Especializado\n[0] - Voltar\n
Atenção: Ao se inscrever como voluntário, você concorda em disponibilizar
seu nome, email e cpf para a criação de uma conta no sistema Sou Grato \x1B[2A \x1B[75D'''))
                    limpa()
                    while b:
                        if vol == 0:
                            limpa()
                            b = False
                            f = False
                        elif vol == 1:
                            dadosRonda = []
                            dadosRonda.append(input("Digite seu nome: "))
                            dadosRonda.append(input("Digite seu email: "))
                            dadosRonda.append(input("Digite o seu número de telefone: "))
                            dadosRonda.append(input("Digite o nome do seu contato de emergência: "))
                            dadosRonda.append(input("Digite o número de telefone do seu contato de emergência: "))
                            limpa()
                            proceed = input("Pressione enter para continuar...")
                            escreverDados('DadosSGRonda.csv', dadosRonda)
                            limpa()
                            f = False
                            b = False
                            c = False
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
                            escreverDados('DadosSGEspec.csv', dadosEspec)
                            limpa()
                            f = False
                            b = False
                            c = False
            elif escolha_menu==3:
                b = True
                while b:
                    limpa()
                    print("Com que frequência você deseja doar?")
                    freqDoacao = int(input("[1] - Mensalmente\n[2] - Doação única\n[0] - Voltar\n"))
                    d = True
#Não volta pra essa tela, buga e para de funcionar
                    while d:
                        if freqDoacao == 0:
                            limpa()
                            d = False
                            b = False             
#############################################################################           
                        elif freqDoacao == 1:
                            e = True
                            limpa()
                            if logged == False:
                                while e:
                                    escolha_login = int(input('[1] - Login \t [2] - Cadastrar-se \t [0] - Voltar\n'))
                                    if escolha_login == 0:
                                        limpa()
                                        g = False
                                        e = False
                                        d = False       
                                    elif escolha_login == 1:
                                            limpa()                            
                                            Login('DadosADM.csv',contasADM)                                       
                                    elif escolha_login == 2:
                                            limpa()
                                            Cadastro('DadosADM.csv',contasADM)                                       
                            if logged == True:
                                while e == True: 
                                    limpa()
                                    print("pix ou cartao aqui")
                                    proceed = input("\nPressione enter para continuar...")
                                    e = False
                                    d = False
                                    b = False
                                    limpa()
#############################################################################                                    
                        elif freqDoacao == 2:
                            limpa()
                            print("pix ou cartão aqui")
                            proceed = input("\nPressione enter para continuar...")
                            d = False
                            limpa()
    # Tela de login
    if escolha_main == 2 and logged == False:
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
                        proceed = input("\nPressione enter para continuar...")
                        limpa()
                        escolha_back = int(input('[1] - Tentar novamente \t [2] - Voltar \n'))
                        if escolha_back == 2:
                            b = False
                            limpa()
                    else:
                        senha = input('Digite sua senha: ')
                        if contasADM[login] != senha:
                            print('Senha inválida!')
                            proceed = input("\nPressione enter para continuar...")
                            limpa()
                            escolha_back = int(input('[1] - Tentar novamente \t [2] - Voltar \n'))
                            if escolha_back == 2:
                                b = False
                                limpa()
                        else:
                            logged = True
                            b = False
        elif escolha_login == 2:
            while b == True:
                cadastro = []
                limpa()
                cadastro_usuario = input('Digite o login desejado: ')
                if cadastro_usuario in contasADM:
                    limpa()
                    print('Usuário já cadastrado!')
                    proceed = input("\nPressione enter para continuar...")
                    limpa()
                    escolha_voltar = int(input('[1] - Tentar novamente \t [2] - Voltar \n'))
                    if escolha_voltar == 2:
                        b = False
                        limpa()
                else:
                    cadastro_senha = input('Digite a senha desejada: ')
                    cadastro.append(cadastro_usuario)
                    cadastro.append(cadastro_senha)
                    Cadastro('DadosADM.csv', cadastro)
                    limpa()
                    logged = True
                    b = False
    elif escolha_main == 3:
        logged = False

from ModuloSG import *

while wMain:

    wEscolha2 = True
    
    if logged == False:
        limpa()
        escolha_menu = int(input('[1] - Acessar o menu \t [2] - Login/Cadastro \t [3] - Sair \n'))
    
    if logged == True:
        limpa()
        escolha_menu = int(input('[1] - Acessar o menu \t [2] - Acessar perfil \t [3] - Sair \t [4] - Logout \n'))

    if escolha_menu == 4:
        limpa()
        logged = False
    
    elif escolha_menu == 3:
        limpa()
        wMain = False
    
    elif escolha_menu == 2 and logged == False:

        while wEscolha2:
            limpa()
            escolha_login = int(input('[1] - Login \t [2] - Cadastrar-se \t [0] - Voltar\n'))
            
            if escolha_login == 0:
                wEscolha2 = False
            
            elif escolha_login == 1:
                if Login() == True:
                    logged = True
                    wEscolha2 = False
                else:
                    limpa()
                    print('Login inválido!')
                    proceed = input("\nPressione enter para continuar...")

            elif escolha_login == 2:
                if Cadastro() == True:
                    print('Cadastro realizado com sucesso!')
                    logged = True
                    wEscolha2 = False
                else:
                    print('Não foi possível concluir seu cadastro!')
                    proceed = input("\nPressione enter para continuar...")

    elif escolha_menu == 2 and logged == True:
        limpa()
        print("Parte não terminada do perfil do usuário.")
        proceed = input("\nPressione enter para continuar...")
        pass

    elif escolha_menu == 1:
        
        wMenu = True
        while wMenu:
            limpa()
            escolha_menu = int(input('[0] - Voltar \n[1] - Quem somos \n[2] - Seja voluntário \n[3] - Seja doador \n'))
            
            if escolha_menu == 0:
                wMenu = False
                limpa()

            elif escolha_menu == 1:
                TextoSG()

            elif escolha_menu == 2:
                Volunt()

            elif escolha_menu == 3 and logged == False:
                if DonateNotLogged() == True:
                    logged = True
            
            elif escolha_menu == 3 and logged:
                DonateLogged()

                
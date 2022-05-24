from Modulo import *

while w_main:
        
    if logged == False:
        limpa()
        escolha_menu = int(input('[1] - Acessar o menu \t [2] - Login/Cadastro \t [3] - Sair \n'))
        pass
    if logged == True:
        limpa()
        escolha_menu = int(input('[1] - Acessar o menu \t [2] - Acessar perfil \t [3] - Sair \t [4] - Logout \n'))
        pass
    if escolha_menu == 4:
        limpa()
        logged = False
        pass 
    elif escolha_menu == 3:
        limpa()
        print('Obrigadx por utilizar o app Sou Grato!')
        w_main = False
        pass

    elif escolha_menu == 2 and logged == False:
        
        w_escolha_2 = True

        while w_escolha_2:
            limpa()
            escolha_login = int(input('[1] - Login \t [2] - Cadastrar-se \t [0] - Voltar\n'))
            
            if escolha_login == 0:
                w_escolha_2 = False
            
            elif escolha_login == 1:
                w_login = True
                while w_login:

                    log = login()

                    if log == True:
                        logged = True
                        w_login = False
                        w_escolha_2 = False
                    elif log == 'cadastro':
                        limpa()
                        print('Email não encontrado.')
                        proceed = input('[1] - Cadastrar-me [2] - Voltar\n')
                        if proceed == 2:
                            w_login = False
                            logged = False
                            pass
                        else:
                            cadastro = Cadastro()
                            if cadastro == 'jaCadastrado':
                                limpa()
                                print('Email já cadastrado!')
                                proceed = input('Pressione enter para continuar.')
                                w_login = False
                                logged = False
                                pass
                            elif cadastro == 'cpfUsado':
                                limpa()
                                print('Este CPF já está em uso!')
                                proceed= input('Pressione enter para continuar.')
                                w_login = False
                                logged = False
                                pass
                            elif cadastro == 'senhaNaoCoincide':
                                limpa()
                                print('As senhas não coincidem.')
                                proceed = int(input('[1] - Tentar Novamente [2] - Voltar\n'))
                                if proceed == 2:
                                    logged = False                                
                                    w_login = False
                                    w_escolha_2 = False
                                    pass
                            elif cadastro == True:
                                limpa()
                                print('Cadastro concluído com sucesso!')
                                proceed = input('Pressione enter para continuar.')
                                logged = True
                                w_login = False
                                w_escolha_2 = False
                                pass
                    elif log == 'senhaIncorreta':
                        limpa()
                        print('Usuário ou senha incorretos.')
                        proceed = int(input('[1] - Tentar Novamente [2] - Voltar\n'))
                        if proceed == 2:
                            logged = False
                            w_login = False
                            w_escolha_2 = False
                            pass       

            elif escolha_login == 2:
                limpa()
                cadastro = Cadastro()
                if cadastro == 'jaCadastrado':
                    limpa()
                    print('Email já cadastrado!')
                    proceed = input('Pressione enter para continuar.')
                    w_login = False
                    logged = False
                    pass
                elif cadastro == 'cpfUsado':
                    limpa()
                    print('Este CPF já está em uso!')
                    proceed= input('Pressione enter para continuar.')
                    w_login = False
                    logged = False
                    pass
                elif cadastro == 'senhaNaoCoincide':
                    limpa()
                    print('As senhas não coincidem.')
                    proceed = int(input('[1] - Tentar Novamente [2] - Voltar'))
                    if proceed == 2:
                        logged = False                                
                        w_login = False
                        w_escolha_2 = False
                        pass
                elif cadastro == True:
                    limpa()
                    print('Cadastro concluído com sucesso!')
                    proceed = input('Pressione enter para continuar.')
                    logged = True
                    w_login = False
                    w_escolha_2 = False
                    pass

    elif escolha_menu == 2 and logged == True:
        limpa()
#Tentei botar o nome mas n consegui
        w_profile = True
        while w_profile:
            limpa()
            # print(f'Perfil de {nome}')
            escolha_perfil = int(input('''[1] - Metas 
[2] - Histórico de doações 
[3] - Histórico de Participações
[4] - Feedback
[0] - Voltar\n'''))
            w_goals = True
            while w_goals:
                if escolha_perfil == 1:
                    limpa()
                    # print(f'Metas de {nome}')
                    print('''As metas da semana estão perto de serem alcançadas!
Semana da Ronda do dia 15/06/22
    ███████████████████████████---------|76% Completa''')
                    proceed = input('Pressione enter para voltar...')
                    w_goals = False
                    pass
                elif escolha_perfil == 2:
                    limpa()
                    # print(f'Historico de doações de {nome}')
                    with open('donate_history.txt','r',encoding='utf8') as dh:
                        print(dh.read())     
                    proceed = input("Pressione enter para continuar...")
                    w_goals = False
                    pass
                elif escolha_perfil == 3:
                    limpa()
                    # print(f'Histórico de participação de {nome}')
                    with open('part_history.txt','r',encoding='utf8') as ph:
                        print(ph.read())
                    proceed = input('Pressione enter para continuar.')
                    w_goals = False
                elif escolha_perfil == 4:
                    limpa()
                    # print(f'Feedback de {nome}')
                    with open('feedback.txt','r',encoding='utf8') as fb:
                        print(fb.read())
                    proceed = input('Pressione enter para continuar...')
                    w_goals = False
                elif escolha_perfil == 0:
                    w_goals = False
                    w_profile = False

    elif escolha_menu == 1:
        
        w_menu = True    
        while w_menu:
            limpa()
            escolha_menu = int(input('[0] - Voltar \n[1] - Quem somos \n[2] - Seja voluntário \n[3] - Seja doador \n'))
            
            if escolha_menu == 0:
                w_menu = False
                limpa()

            elif escolha_menu == 1:
                limpa()
                w_qs = True
                while w_qs:
                    with open('quem_somos.txt','r',encoding='utf8') as quemsomos:
                        print(quemsomos.read())
                    proceed = input('\nPressione enter para continuar...')
                    w_qs = False
                    

            elif escolha_menu == 2:
                limpa()
                print("Qual tipo de voluntário você deseja ser?")
                vol = int(input('''[1] - Voluntário de Ronda\n[2] - Voluntário Especializado\n[0] - Voltar\n
Atenção: Ao se inscrever como voluntário, você concorda em disponibilizar
seu nome, email e cpf para a criação de uma conta no sistema Sou Grato \x1B[2A \x1B[75D'''))
                w_vol = True
                while w_vol:
                    if vol == 0:
                        w_vol = False
                        limpa()

                    if vol == 1:
                        reg = volunt_reg()
                        if reg == True:
                            print('''Agradecemos por você se cadastrar como voluntárix!
    Você também pode nos ajudar por meio de doações.''')
                            proceed = input('Pressione enter para continuar.')
                            w_vol = False
                            logged = True
                        elif reg=='email_usado':
                            print('Email já cadastrado.')
                            procced = input('''[1] - Tentar Novamente [2] - Voltar''')
                            if proceed == '2':
                                w_vol = False
                        elif reg == 'cpf_usado':
                            print('CPF já cadastrado.')
                            proceed = input('''[1] - Tentar Novamente [2] - Voltar''')
                            if proceed == '2':
                                w_vol = False
                        elif reg == 'senhaNaoCoincide':
                            print('Senha inválida.')
                            proceed = input('[1] - Tentar Novamente [2] - Voltar')
                            if proceed == '2':
                                w_vol = False
                        elif reg == 'usuario_nao_encontrado':
                            print('Usuário não encontrado.')
                            proceed = input('[1] - Tentar Novamente [2] - Voltar')
                            if proceed == '2':
                                w_vol = False                      
                    elif vol == 2:
                        espec = volunt_espec()
                        if espec == True:
                            print('''Agradecemos por você se cadastrar como voluntárix!
    Você também pode nos ajudar por meio de doações.''')
                            proceed = input('Pressione enter para continuar.')
                            w_vol = False
                            logged = True
                        elif espec=='email_usado':
                            print('Email já cadastrado.')
                            procced = input('''[1] - Tentar Novamente [2] - Voltar''')
                            if proceed == '2':
                                w_vol = False
                        elif espec == 'cpf_usado':
                            print('CPF já cadastrado.')
                            procced = input('''[1] - Tentar Novamente [2] - Voltar''')
                            if proceed == '2':
                                w_vol = False
                        elif espec == 'senhaNaoCoincide':
                            print('Senha inválida.')
                            proceed = input('[1] - Tentar Novamente [2] - Voltar')
                            if proceed == '2':
                                w_vol = False
                        elif espec == 'usuario_nao_encontrado':
                            print('Usuário não encontrado.')
                            proceed = input('[1] - Tentar Novamente [2] - Voltar')
                            if proceed == '2':
                                w_vol = False 
                        
            elif escolha_menu == 3:
                limpa()
                print("Com que frequência você deseja doar?")
                freqDoacao = int(input("[1] - Mensalmente\n[2] - Doação única\n[0] - Voltar\n"))
                w_freq = True
                while w_freq:
                    if freqDoacao == 0:
                        w_freq = False
                        pass
                    elif freqDoacao == 1:
                        limpa()
                        mes = donate_mes()
                        if mes == 'Logado':
                            limpa()
                            print('Pix ou Cartão aqui')
                            proceed = input('Pressione enter para continuar.')
                            w_freq = False
                        if mes == 'login':
                            limpa()
                            print('Pix ou Cartão aqui')
                            proceed = input('Pressione enter para continuar.')
                            w_freq = False
                            logged = True
                            pass
                        elif mes == 'cadastrado':
                            limpa()
                            print('Pix ou Cartão aqui')
                            proceed = input('Pressione enter para continuar.')
                            w_freq = False
                            logged = True
                            pass
                        elif mes == 'cadastro':
                            limpa()
                            print('Email não encontrado.')
                            proceed = input('[1] - Cadastrar-me [2] - Voltar\n')
                            if proceed == 2:
                                w_freq = False
                                logged = False
                                pass
                            else:
                                cadastro = Cadastro()
                                if cadastro == 'jaCadastrado':
                                    limpa()
                                    print('Email já cadastrado!')
                                    proceed = input('Pressione enter para continuar.')
                                    w_freq = False
                                    logged = False
                                    pass
                                elif cadastro == 'cpfUsado':
                                    limpa()
                                    print('Este CPF já está em uso!')
                                    proceed= input('Pressione enter para continuar.')
                                    w_freq = False
                                    logged = False
                                    pass
                                elif cadastro == 'senhaNaoCoincide':
                                    limpa()
                                    print('As senhas não coincidem.')
                                    proceed = int(input('[1] - Tentar Novamente [2] - Voltar\n'))
                                    if proceed == 2:
                                        logged = False                                
                                        w_freq = False                                        
                                        pass
                                elif cadastro == True:
                                    limpa()
                                    print('Pix ou Cartão aqui')
                                    proceed = input('Pressione enter para continuar.')
                                    logged = True
                                    w_freq = False                                                   
                                pass
                        elif mes == 'senhaIncorreta':
                            limpa()
                            print('Usuário ou senha incorretos.')
                            proceed = int(input('[1] - Tentar Novamente [2] - Voltar\n'))
                            if proceed == 2:
                                logged = False
                                w_freq = False
                                pass
                    elif freqDoacao == 2:
                        limpa()
                        print('Pix ou Cartão aqui')
                        proceed = input('Pressione enter para continuar.')
                        w_freq = False

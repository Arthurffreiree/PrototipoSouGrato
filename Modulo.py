#Imports
import csv
import os

#Variáveis Globais
global w_main
global logged
global w_escolha_2
global w_menu
global w_reg
global w_espec
global w_donate
global w_freq
global w_log_donate
global w_cadastro_mod
global w_cadastro_main
global w_vol
global w_qs
global w_mes
global w_goals
global nome
global user
global cpf
global senha

#Valores das variáveis booleanas   
logged = False
w_main = True
w_escolha_2 = True
w_menu = True
w_reg = True
w_espec = True
w_donate = True
w_freq = True
w_log_donate = True
w_login = True
w_vol = True
w_qs = True
w_mes = True
w_goals = True

#Listas e Dicionários
contas_adm = {}
dados_cadastro = []
cadastro = []
dados_ronda = []
dados_espec = []
emails = []
senhas = []
cpfs = []
nomes = []

#Limpeza do terminal
def limpa():
    os.system('cls')

#Escrita dos dados nos arquivos CSV
def escrever_dados(nome_arquivo, nome_lista):
    with open(nome_arquivo, 'a') as adm:
        esc = ','.join(nome_lista)
        adm.writelines(esc + '\n')

#Login do usuário na plataforma
def login():
    global user

    limpa()
    
    user = input('Digite o email de login: ')
    senha = input('Digite sua senha: ')

    with open('DadosContas.csv','r') as adm:
        leitor = csv.DictReader(adm)
        contas_adm = {l['colEmail']:l['colSenha'] for l in leitor}

    if user not in contas_adm:
        return 'cadastro'
    elif user in contas_adm and contas_adm[user]!= senha:
        return 'senhaIncorreta'               
    elif user in contas_adm and contas_adm[user] == senha:
        return True 
    else:
        print('Não foi possível fazer o login') 
        pass

#Cadastro do usuário
def Cadastro():
    global nome
    global user
    global senha
    global cpf
    w_senha = True
    w_cadastro_mod = True

    existence()

    while w_cadastro_mod:

        limpa()

        user = input('Digite seu email de Login: ')

        if user not in emails:        
            nome = input('Digite seu nome: ')
            cpf = input('Digite seu cpf: ')
            if cpf not in cpfs:
                dados_cadastro.append(user)
                dados_cadastro.append(nome)
                dados_cadastro.append(cpf)
                while w_senha:
                    if pass_confirm(dados_cadastro) == True: 
                        limpa()
                        escrever_dados('DadosContas.csv',dados_cadastro)
                        w_senha = False
                        return True  
                    elif pass_confirm(dados_cadastro) == False:
                        w_senha = False
                        w_cadastro_mod = False
                        return 'senhaNaoCoincide'
            else:
                w_cadastro_mod = False
                return 'cpfUsado'
        else:
            w_cadastro_mod = False
            return 'jaCadastrado'
#Cadastro/Login do voluntário de ronda
def volunt_reg(logged):
    global nome
    global user
    global senha

    w_reg = True
    w_senha = True

    limpa()
    existence()

    while w_reg:
        if logged == True:
            cpf = cpfs[emails.index(user)]
            senha = senhas[emails.index(user)]
            nome = nomes[emails.index(user)]

            dados_ronda.append(input('Insira seu número de telefone: '))
            dados_ronda.append(input('Insira o nome do seu contato de emergência: '))
            dados_ronda.append(input('Insira o número do seu contato de emergência: '))
            dados_ronda.insert(0,user)
            dados_ronda.insert(1,nome)
            dados_ronda.insert(2,cpf)
            dados_ronda.insert(3,senha)

            escrever_dados('DadosSGRonda.csv',dados_ronda)
            w_reg = False
            return True

        if logged == False:
            log = int(input('[1] - Login [2] - Cadastro\n'))

            if log == 1:
                limpa()
                user = input('Insira o email para login: ')
                if user not in emails:
                    print('Usuário não encontrado.')
                    proceed = input('Pressione enter para continuar.')
                    return 'usuario_nao_encontrado'
                else:
                    senha = input('Insira a senha: ')
                    if senha!=senhas[emails.index(user)]:
                        print('Senha invalida.')
                        proceed = input('Pressione enter para continuar.')
                        return 'senhaNaoCoincide'
                    else: 
                        logged = True
                        pass
                    
            else:
                user = input('Insira o email para login: ')
                if user in emails:                    
                    return 'email_usado'
                cpf = input('Insira seu CPF: ')
                if cpf in cpfs:
                    return 'cpf_usado'
                else:
                    nome = input('Insira seu nome: ')
                    while w_senha:
                        if pass_confirm(dados_ronda) == True: 
                            limpa()
                            senha = senha
                            dados_ronda.append(input('Insira seu número de telefone: '))
                            dados_ronda.append(input('Insira o nome do seu contato de emergência: '))
                            dados_ronda.append(input('Insira o número do seu contato de emergência: '))
                            dados_ronda.insert(0, user)
                            dados_ronda.insert(1, nome)

                            escrever_dados('DadosSGRonda.csv', dados_ronda)

                            dados_cadastro.insert(0,user)
                            dados_cadastro.insert(1,nome)
                            dados_cadastro.insert(2,cpf)
                            dados_cadastro.insert(3,senha)

                            escrever_dados('DadosContas.csv', dados_cadastro)
                            w_reg = False
                            logged = True
                            w_senha = False
                            return True  
                        elif pass_confirm(dados_ronda) == False:
                            w_senha = False
                            w_reg = False
                            return 'senhaNaoCoincide'
                        
#Cadastro/Login do voluntário especializado                    
def volunt_espec(logged):
    global nome
    global user
    global senha
    global cpf
    w_senha = True
    w_espec = True

    limpa()
    existence()

    while w_espec:

        if logged == True:
            cpf = cpfs[emails.index(user)]
            senha = senhas[emails.index(user)]
            nome = nomes[emails.index(user)]

            dados_espec.append(input('Insira seu número de telefone: '))
            dados_espec.append(input('Insira o seu grau de escolaridade: '))
            dados_espec.append(input('Insira sua área de interesse: '))
            dados_espec.append(input('Alguma proposta para a organização?\n'))
            dados_espec.insert(0,user)
            dados_espec.insert(1,nome)
            dados_espec.insert(2,cpf)
            dados_espec.insert(3,senha)

            escrever_dados('DadosSGEspec.csv',dados_espec)
            w_espec = False
            return True

        elif logged == False:

            log = int(input('[1] - Login [2] - Cadastro\n'))

            if log == 1:
                limpa()
                user = input('Insira o email para login: ')

                if user not in emails:
                    limpa()
                    print('Usuário não encontrado.')
                    proceed = input('Pressione enter para continuar.')
                    return 'usuario_nao_encontrado'
                else:
                    senha = input('Insira a senha: ')
                    if senha!=senhas[emails.index(user)]:
                        limpa()
                        print('Senha invalida.')
                        proceed = input('Pressione enter para continuar.')
                        return 'senhaNaoCoincide'
                    else: 
                        logged = True
                        pass
            else:
                limpa()
                user = input('Insira o email para login: ')
                if user in emails:                    
                    return 'email_usado'
                cpf = input('Insira seu CPF: ')
                if cpf in cpfs:
                    return 'cpf_usado'
                else:
                    nome = input('Insira seu nome: ')
                while w_senha:
                    if pass_confirm(dados_espec) == True: 
                        limpa()
                        senha = senha
                        dados_espec.append(input('Insira seu número de telefone: '))
                        dados_espec.append(input('Insira o seu grau de escolaridade: '))
                        dados_espec.append(input('Insira sua área de interesse: '))
                        dados_espec.append(input('Alguma proposta para a organização?\n'))
                        dados_espec.insert(0,user)
                        dados_espec.insert(1,nome)
                        escrever_dados('DadosSGEspec.csv', dados_espec)
                        dados_cadastro.insert(0,user)
                        dados_cadastro.insert(1,nome)
                        dados_cadastro.insert(2,cpf)
                        dados_cadastro.insert(3,senha)
                        escrever_dados('DadosContas.csv', dados_cadastro)
                        w_espec = False
                        logged = True
                        w_senha = False
                        return True  
                    elif pass_confirm(dados_espec) == False:
                        w_senha = False
                        w_espec = False
                        return 'senhaNaoCoincide'

#Confirmação da senha do cadastro
def pass_confirm(lista):
    global senha
    global user
    senha = input('Digite sua senha:')
    confsenha = input('Confirme a senha: ')
    if senha == confsenha:
        lista.insert(3, senha)            
        return True  
    else:
        limpa()
        return False

#Separação das colunas dos arquivos CSV
#Serve para facilitar a busca por informações
def existence():
    with open('DadosContas.csv') as contas:
        leitor = csv.DictReader(contas)
        for c in leitor:
            emails.append(c['colEmail'])
            senhas.append(c['colSenha'])
            nomes.append(c['colNome'])
            cpfs.append(c['colCpf'])

#Cadastro/Login do doador mensal
def donate_mes():
    global logged
    w_mes = True
    while w_mes:
        # nao ta tomando como logado
        if logged == True:
            return 'Logado'
        if logged == False:
            log = int(input('[1] - Login [2] - Cadastro\n'))
            if log == 1:
                if login() == True:
                    return 'login'
                else:
                    return login()
            elif log == 2:
                if Cadastro() == True:
                    return 'cadastrado'
                else:
                    return Cadastro()

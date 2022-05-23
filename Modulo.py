import csv
import os

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

w_main = True
logged = False
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

contas_adm = {}
dados_cadastro = []
cadastro = []
dados_ronda = []
dados_espec = []
emails = []
senhas = []
cpfs = []
nomes = []

def limpa():
    os.system('cls')

def escreverDados(nome_arquivo, nome_lista):
    with open(nome_arquivo, 'a') as adm:
        esc = ','.join(nome_lista)
        adm.writelines(esc + '\n')

def login():
    limpa()
    global user
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

def Cadastro():
    global nome
    wSenha = True
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
                while wSenha:
                    if passConfirm(dados_cadastro) == True: 
                        limpa()
                        escreverDados('DadosContas.csv',dados_cadastro)
                        wSenha = False
                        return True  
                    elif passConfirm(dados_cadastro) == False:
                        wSenha = False
                        w_cadastro_mod = False
                        return 'senhaNaoCoincide'
            else:
                w_cadastro_mod = False
                return 'cpfUsado'
        else:
            w_cadastro_mod = False
            return 'jaCadastrado'
def volunt_reg():
    global nome
    w_reg = True
    wSenha = True
    global user
    global senha
    global logged
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
            escreverDados('DadosSGRonda.csv',dados_ronda)
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
                    while wSenha:
                        if passConfirm(dados_ronda) == True: 
                            limpa()
                            senha = senha
                            dados_ronda.append(input('Insira seu número de telefone: '))
                            dados_ronda.append(input('Insira o nome do seu contato de emergência: '))
                            dados_ronda.append(input('Insira o número do seu contato de emergência: '))
                            dados_ronda.insert(0, user)
                            dados_ronda.insert(1, nome)
                            escreverDados('DadosSGRonda.csv', dados_ronda)
                            dados_cadastro.insert(0,user)
                            dados_cadastro.insert(1,nome)
                            dados_cadastro.insert(2,cpf)
                            dados_cadastro.insert(3,senha)
                            escreverDados('DadosContas.csv', dados_cadastro)
                            w_reg = False
                            logged = True
                            wSenha = False
                            return True  
                        elif passConfirm(dados_ronda) == False:
                            wSenha = False
                            w_reg = False
                            return 'senhaNaoCoincide'
                        
                    
def volunt_espec():
    global nome
    w_espec = True
    global user
    global senha
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
            escreverDados('DadosSGEspec.csv',dados_espec)
            w_espec = False
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
                nome = input('Insira seu nome: ')
                while wSenha:
                    if passConfirm(dados_espec) == True: 
                        limpa()
                        senha = senha
                        dados_espec.append(input('Insira seu número de telefone: '))
                        dados_espec.append(input('Insira o seu grau de escolaridade: '))
                        dados_espec.append(input('Insira sua área de interesse: '))
                        dados_espec.append(input('Alguma proposta para a organização?\n'))
                        dados_espec.insert(0, user)
                        dados_espec.insert(1, nome)
                        escreverDados('DadosSGEspec.csv', dados_espec)
                        dados_cadastro.insert(0,user)
                        dados_cadastro.insert(1,nome)
                        dados_cadastro.insert(2,cpf)
                        dados_cadastro.insert(3,senha)
                        escreverDados('DadosContas.csv', dados_cadastro)
                        w_espec = False
                        logged = True
                        wSenha = False
                        return True  
                    elif passConfirm(dados_espec) == False:
                        wSenha = False
                        w_espec = False
                        return 'senhaNaoCoincide'

def passConfirm(lista):
    global senha
    senha = input('Digite sua senha:')
    confsenha = input('Confirme a senha: ')
    if senha == confsenha:
        lista.insert(3, senha)            
        return True  
    else:
        limpa()
        return False

def existence():
    with open('DadosContas.csv') as contas:
        leitor = csv.DictReader(contas)
        for c in leitor:
            emails.append(c['colEmail'])
            senhas.append(c['colSenha'])
            nomes.append(c['colNome'])
            cpfs.append(c['colCpf'])

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

# def name():
#     global nome
#     global user
#     existence()
#     nome = nomes[emails.index(user)]
#     return nome
# print(name())

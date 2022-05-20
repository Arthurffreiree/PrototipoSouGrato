import csv
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

contasADM = {}
dadosCadastro = []
cadastro = []
dadosRonda = []
dadosEspec = []
emails = []
senhas = []
cpfs = []
nomes = []

def limpa():
    os.system('cls')

def escreverDados(nomeArquivo, nomeLista):
    with open(nomeArquivo, 'a') as adm:
        esc = ','.join(nomeLista)
        adm.writelines(esc + '\n')

def Login():
    limpa()
    global user
    user = input('Digite o email de login: ')
    senha = input('Digite sua senha: ')
    with open('DadosContas.csv','r') as adm:
        leitor = csv.DictReader(adm)
        contasADM = {l['colEmail']:l['colSenha'] for l in leitor}
    if user not in contasADM:
        return 'cadastro'
    elif user in contasADM and contasADM[user]!= senha:
        return 'senhaIncorreta'               
    elif user in contasADM and contasADM[user] == senha:
        return True 
    else:
        print('Não foi possível fazer o login') 
        pass

def Cadastro():
    wSenha = True
    wCadastro = True
    while wCadastro:
        limpa()
        Cadastro.user = input('Digite seu email de Login: ')
        if Cadastro.user in emails:
            wCadastro = False
            return 'jaCadastrado'
        else:
            Cadastro.nome = input('Digite seu nome: ')
            cpf = input('Digite seu cpf: ')
            if cpf in cpfs:
                wCadastro = False
                return 'cpfUsado'
            else:
                dadosCadastro.append(Cadastro.user)
                dadosCadastro.append(Cadastro.nome)
                dadosCadastro.append(cpf)
                while wSenha:
                    if passConfirm(dadosCadastro) == True: 
                        limpa()
                        escreverDados('DadosContas.csv',dadosCadastro)
                        wSenha = False
                        return True  
                    elif passConfirm(dadosCadastro) == False:
                        wSenha = False
                        wCadastro = False
                        return 'senhaNaoCoincide'

def VoluntReg():
    # while wVolunt:
        wReg = True
        wSenha = True
        global user
        global senha
        global logged
#         print("Qual tipo de voluntário você deseja ser?")
#         vol = int(input('''[1] - Voluntário de Ronda\n[2] - Voluntário Especializado\n[0] - Voltar\n
# Atenção: Ao se inscrever como voluntário, você concorda em disponibilizar
# seu nome, email e cpf para a criação de uma conta no sistema Sou Grato \x1B[2A \x1B[75D'''))
        limpa()
        existence()
        while wReg:
            if logged == True:
                cpf = cpfs[emails.index(user)]
                senha = senhas[emails.index(user)]
                nome = nomes[emails.index(user)]
                dadosRonda.append(input('Insira seu número de telefone: '))
                dadosRonda.append(input('Insira o nome do seu contato de emergência: '))
                dadosRonda.append(input('Insira o número do seu contato de emergência: '))
                dadosRonda.insert(0,user)
                dadosRonda.insert(1,nome)
                dadosRonda.insert(2,cpf)
                dadosRonda.insert(3,senha)
                escreverDados('DadosSGRonda.csv',dadosRonda)
                wReg = False
                return True
            if logged == False:
                user = input('Insira o email para login: ')
                if user in emails:
                    return 'emailsUsado'
                cpf = input('Insira seu CPF: ')
                if cpf in cpfs:
                    return 'cpfUsado'
                else:
                    nome = input('Insira seu nome: ')
                    while wSenha:
                        if passConfirm(dadosRonda) == True: 
                            limpa()
                            senha = senha
                            dadosRonda.append(input('Insira seu número de telefone: '))
                            dadosRonda.append(input('Insira o nome do seu contato de emergência: '))
                            dadosRonda.append(input('Insira o número do seu contato de emergência: '))
                            dadosRonda.insert(0, user)
                            dadosRonda.insert(1, nome)
                            escreverDados('DadosSGRonda.csv', dadosRonda)
                            dadosCadastro.insert(0,user)
                            dadosCadastro.insert(1,nome)
                            dadosCadastro.insert(2,cpf)
                            dadosCadastro.insert(3,senha)
                            escreverDados('DadosContas.csv', dadosCadastro)
                            wReg = False
                            logged = True
                            wSenha = False
                            return True  
                        elif passConfirm(dadosRonda) == False:
                            wSenha = False
                            wReg = False
                            return 'senhaNaoCoincide'
                        
                    
def VoluntEspec():
    wEspec = True
    global user
    global senha
    limpa()
    existence()
    while wEspec:
        if logged == True:
            cpf = cpfs[emails.index(user)]
            senha = senhas[emails.index(user)]
            nome = nomes[emails.index(user)]
            dadosRonda.append(input('Insira seu número de telefone: '))
            dadosRonda.append(input('Insira o nome do seu contato de emergência: '))
            dadosRonda.append(input('Insira o número do seu contato de emergência: '))
            dadosRonda.insert(0,user)
            dadosRonda.insert(1,nome)
            dadosRonda.insert(2,cpf)
            dadosRonda.insert(3,senha)
            escreverDados('DadosSGRonda.csv',dadosRonda)
            wReg = False
            return True
        if logged == False:
            user = input('Insira o email para login: ')
            if user in emails:
                return 'emailsUsado'
            cpf = input('Insira seu CPF: ')
            if cpf in cpfs:
                return 'cpfUsado'
            else:
                nome = input('Insira seu nome: ')
                while wSenha:
                    if passConfirm(dadosRonda) == True: 
                        limpa()
                        senha = senha
                        dadosRonda.append(input('Insira seu número de telefone: '))
                        dadosRonda.append(input('Insira o nome do seu contato de emergência: '))
                        dadosRonda.append(input('Insira o número do seu contato de emergência: '))
                        dadosRonda.insert(0, user)
                        dadosRonda.insert(1, nome)
                        escreverDados('DadosSGRonda.csv', dadosRonda)
                        dadosCadastro.insert(0,user)
                        dadosCadastro.insert(1,nome)
                        dadosCadastro.insert(2,cpf)
                        dadosCadastro.insert(3,senha)
                        escreverDados('DadosContas.csv', dadosCadastro)
                        wReg = False
                        logged = True
                        wSenha = False
                        return True  
                    elif passConfirm(dadosRonda) == False:
                        wSenha = False
                        wReg = False
                        return 'senhaNaoCoincide'
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
            cpfs.append(c['colCpf'])
            nomes.append(c['colNome'])

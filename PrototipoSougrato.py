import os
import csv

os.system("cls")

def escreverDados(DadosSougrato, Dados):
    with open(DadosSougrato, 'a') as texto:
        banco = ' , '.join(Dados)
        texto.writelines(banco+'\n')

contasADM = {}
contEspec = 0
contRonda = 0
reset = 1
a = 1
i = 1

while a != 0:  
    if reset == 1:
        i = 1
        # Identificação
        id = int(input("[1] - Voluntário\t[2] - Admin\n\t[0] - Sair\n"))
        os.system("cls")
        reset = 2
    if id == 0:
                a = 0
        # Menu do voluntário
    elif id == 1:
        escolha = int(input('''[0] - Voltar
[1] - Quem somos?
[2] - Redes sociais
[3] - Seja voluntário
[4] - Seja doador
[5] - Informações
''')) 
        os.system("cls")
            # Voltar ao menu principal
        if escolha == 0:
                os.system("cls")
                reset = 1
            # Quem somos?
        elif escolha == 1:
                print('''O Sou Grato é uma Iniciativa social sem fins lucrativos que surgiu em 2018 com o propósito de 
ajudar pessoas em situação de rua e famílias em vulnerabilidade. Atualmente, as ações do grupo são realizadas 
semanalmente no município de Recife-PE, no qual são distribuídos alimentos, água, ração para cães e gatos, 
kits de higiene pessoal, roupas e cobertores. Outros tipos de ações também são realizadas em parceria com outras 
iniciativas e instituições sociais para assistir comunidades em situações emergenciais.''')
                continuar = input("\nPressione enter para continuar...")
                os.system("cls")
            # Redes sociais
        elif escolha == 2:
                print("Nosso Whatsapp: +55 81 9716-9065\nNosso Instagram: @gruposougrato")
                continuar = input("\nPressione enter para continuar...")
                os.system("cls")
            # Seja voluntário
        elif escolha == 3:
                print("Qual tipo de voluntário você deseja ser?")
                vol = int(input("[1]Voluntário de Ronda\n[2]Voluntário Especializado\n"))
                os.system("cls")
                if vol == 1:
                    dadosRonda = []
                    dadosRonda.append(input("Digite seu nome: "))
                    dadosRonda.append(input("Digite seu email: "))
                    dadosRonda.append(input("Digite o seu número de telefone: "))
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
            # Doações
        elif escolha == 4:
                doacao = int(input("Qual tipo de doação você deseja fazer?\n[1]Dinheiro\n[2]Alimento\n[3]Marmita\n[4]Produtos de higiene\n"))
                if doacao==1:
                    print("Envie a doação ao nosso pix!\nsougrato@zegratinho.com.br")
                    continuar = input("\nPressione enter para continuar...")
                    os.system("cls")
                elif doacao==2:
                    print('''Você pode enviar a doação por meio de um portador ao endereço Rua José Grato, 78 ou
    Enviar o valor equivalente no pix sougrato@zegratinho.com.br''')
                    continuar = input("\nPressione enter para continuar...")
                    os.system("cls")    
                elif doacao==3:
                    print('''Você pode enviar a marmita por meio de um portador ao endereço Rua José Grato, 78 ou
    Enviar previamente pago por meio de um aplicativo de entrega de alimentos.''')
                    continuar = input("\nPressione enter para continuar...")
                    os.system("cls")
                elif doacao==4:
                    print('''Você pode enviar a doação por meio de um portador ao endereço Rua José Grato, 78 ou
    Enviar o valor equivalente no pix sougrato@zegratinho.com.br''')
                    continuar = input("\nPressione enter para continuar...")
                    os.system("cls")
            # Informações
        elif escolha == 5:
                print('''Para mais informações, envie uma mensagem nas nossas redes sociais:
                Whatsapp: +55 81 9716-9065
                Nosso Instagram: @gruposougrato
                Email: sougrato@zegratinho.com.br
                Ou nos visite na sede: Rua José Grato,78''')
                continuar = input("\nPressione enter para continuar...")
                os.system("cls")
            # Opção de erro
        else: 
                print("Escolha uma ação válida.")
                continuar = input("\nPressione enter para continuar...")
                os.system("cls")

    elif id == 2:
        with open('DadosADM.csv', 'r') as adm:
            dadosADM = csv.reader(adm)
            contasADM = {l[0]:l[1] for l in dadosADM}
            login = input('Digite seu login: ')
            if login not in contasADM:
                print('Login inválido!')
                continuar = input("\nPressione enter para continuar...")
                os.system('cls')
            else:
                senha = input('Digite sua senha: ')
                if contasADM[login] != senha:
                    print('Senha inválida!')
                    continuar = input("\nPressione enter para continuar...")
                    os.system('cls')
                else:
                    dict.clear(contasADM)
                    adm.close()
                    os.system("cls") 
                    while i != 0:
                        os.system("cls")
                        opcao = int(input('''Escolha uma opção:
[0] - Voltar
[1] - Total de voluntários
[2] - Total de doações
[3] - Contato dos voluntários
[4] - Número de doações necessárias\n'''))
                        os.system("cls")
                            # Retorno ao menu
                        if opcao == 0:
                                reset = 1
                                i = 0
                        if opcao == 1:
                            with open('DadosSGRonda.csv', 'r') as dados:
                                ronda_csv = csv.reader(dados)
                                for l in ronda_csv:
                                    print(ronda_csv[l])
                                continuar = input("\nPressione enter para continuar...")
                            
                        
                        
                        
                        
                        ''' # Contagem de voluntários
                            elif opcao == 1:
                                open('DadosSGEspec.csv')
                                open('DadosSGRonda.csv')
                                voluntariosTotal = (len('DadosSGEspec.csv'.readlines-1)+len('DadosSGRonda.csv'.readlines-1))
                                print(f"Há {voluntariosTotal} voluntários cadastrados no momento.")
                                continuar = input("\nPressione enter para continuar...")
                                os.system("cls")
                            # Total de doações
                        elif opcao == 2:
                                print("O total de doações no momento é:\nR${VALOR}\nXXX fatias de queijo\nXXX fatias de mortadela...")
                #Essa parte teria um contador externo linkado a uma conta da organização
                #Ainda não sei fazer então vou deixar assim
                                continuar = input("\nPressione enter para continuar...")
                                os.system("cls")
                            # Consulta dos arquivos .csv
                        elif opcao == 3:
                                with open('DadosSGRonda.csv', 'r') as bancoR:
                                    ronda = csv.reader(bancoR, delimiter=',')
                                    print("Dados dos Voluntário de Ronda:")
                                    for l in bancoR:
                                        Nome =  l.split(',')[0]
                                        Num = l.split(',')[2]
                                        print(f"{Nome} ; {Num}")
                                    with open('DadosSGEspec.csv', 'r') as bancoE:
                                        espec = csv.reader(bancoE, delimiter=',')
                                        print("\nDados dos Voluntários Especializados:")
                                        for l in bancoE:   
                                            nome = l.split(',')[0]
                                            num = l.split(',')[2]  
                                            print(f"{nome} ; {num}")
                                        continuar = input("\nPressione enter para continuar...")
                                        os.system("cls")'''
                    

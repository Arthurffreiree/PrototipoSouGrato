from tkinter import *

def tela_inicio():
    
    global tela_inicial

    tela_inicial = Tk()

    tela_inicial.title('Protótipo Sou Grato')
    tela_inicial.geometry('320x480+806+206')
    tela_inicial.resizable(False, False)

    logo_sou_grato = Label(tela_inicial, text = 'Sou Grato', font = ("Arial", 25))
    logo_sou_grato.place(relx = 0.5, rely = 0.3, anchor = 'center')

    botao_menu = Button(tela_inicial, text = 'Menu', width = 4, height = 1, font = ('Arial', 15), command = abrir_menu)
    botao_menu.place(relx = 0.17, rely = 0.0, anchor = 'ne')

    botao_sair = Button(tela_inicial, text = 'Sair', width = 4, height = 1, font = ('Arial', 15), command = tela_inicial.destroy)
    botao_sair.place(relx = 0.83, rely = 1, anchor = 'sw')

    botao_perfil = Button(tela_inicial, text = 'Perfil', width = 4, height = 1, font = ('Arial', 15), command = abrir_perfil)
    botao_perfil.place(relx = 0.83, rely = 0.0, anchor = 'nw')

    tela_inicial.mainloop()

def abrir_menu():
    
    global menu

    menu = Tk()

    tela_inicial.destroy()

    menu.title('Protótipo Sou Grato')
    menu.geometry('320x480+806+206')
    menu.resizable(False, False)

    botao_x = Button(menu, text = 'X', font = ('Arial', 15), width = 2, height = 1, command = menu_voltar)
    botao_x.place(relx = 0.9, rely = 0.0, anchor = 'nw')
    # Tem q botar o comando nesse botão
    botao_quem_somos = Button(menu, text = 'QUEM SOMOS?', font = ('Arial', 15), height = 2)
    botao_quem_somos.place(x = 160, y = 120, width = 320, height = 40, anchor = 'center')
    # Tem q botar o comando nesse botão
    botao_seja_voluntario = Button(menu, text = 'SEJA VOLUNTÁRIO', font = ('Arial', 15), height = 2)
    botao_seja_voluntario.place(x = 160, y = 160, width = 320, height = 40, anchor = 'center')
    # Tem q botar o comando nesse botão
    botao_seja_doador = Button(menu, text = 'SEJA DOADOR', font = ('Arial', 15), height = 2)
    botao_seja_doador.place(x = 160, y = 200, width = 320, height = 40, anchor = 'center')
    # Tem q botar o comando nesse botão
    botao_oque_precisamos = Button(menu, text = 'O QUE PRECISAMOS', font = ('Arial', 15), height = 2)
    botao_oque_precisamos.place(x = 160, y = 240, width = 320, height = 40, anchor = 'center')
    # Tem q botar o comando nesse botão
    botao_contato = Button(menu, text = 'CONTATO', font = ('Arial', 15), height = 2)
    botao_contato.place(x = 160, y = 280, width = 320, height = 40, anchor = 'center')

    menu.mainloop()

def abrir_perfil():
    
    global perfil

    perfil = Tk()

    tela_inicial.destroy()

    perfil.title('Protótipo Sou Grato')
    perfil.geometry('320x480+806+206')
    perfil.resizable(False, False)

    perfil.mainloop()

def menu_voltar():
    
    menu.destroy()
    tela_inicio()

tela_inicio()
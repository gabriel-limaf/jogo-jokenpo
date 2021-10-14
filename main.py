import random
import PySimpleGUI as sg


def inicio():
    sg.theme('Dark Blue 3')  # please make your creations colorful
    layout = [[sg.Text('Faça a sua escolha !!')],
              [sg.Button('Pedra'), sg.Button('Papel'), sg.Button('Tesoura')],
              [sg.Button('Cancelar')]
              ]
    return sg.Window('Jogo Jokenpo', layout=layout, size=(300, 100), finalize=True)


def perdeu():
    sg.theme('Dark Blue 3')  # please make your creations colorful
    layout = [[sg.Text('Você perdeu !!')],
              [sg.Button('Voltar'), sg.Button('Cancelar')]]
    return sg.Window('ATENÇÃO', layout=layout, size=(300, 100), finalize=True)


def ganhou():
    sg.theme('Dark Blue 3')  # please make your creations colorful
    layout = [[sg.Text('Você ganhou !!')],
              [sg.Button('Voltar'), sg.Button('Cancelar')]]
    return sg.Window('ATENÇÃO', layout=layout, size=(300, 100), finalize=True)


def empate():
    sg.theme('Dark Blue 3')  # please make your creations colorful
    layout = [[sg.Text('Empate !!')],
              [sg.Button('Voltar'), sg.Button('Cancelar')]]
    return sg.Window('ATENÇÃO', layout=layout, size=(300, 100), finalize=True)


janela1, janela2, janela3, janela4 = inicio(), None, None, None
while True:
    machine_choice = random.choice(('Pedra', 'Papel', 'Tesoura'))
    window, event, values = sg.read_all_windows()
    if window == janela1 and event == sg.WINDOW_CLOSED:
        break
    if window == janela1 and event == 'Cancelar':
        break
    if window == janela1 and event == machine_choice:
        janela1.close()
        janela2 = empate()
    if window == janela1 and event == 'Pedra' and machine_choice == 'Papel':
        janela1.close()
        janela2 = perdeu()
    if window == janela1 and event == 'Papel' and machine_choice == 'Tesoura':
        janela1.close()
        janela2 = perdeu()
    if window == janela1 and event == 'Tesoura' and machine_choice == 'Pedra':
        janela1.close()
        janela2 = perdeu()
    if window == janela1 and event == 'Tesoura' and machine_choice == 'Papel':
        janela1.close()
        janela2 = ganhou()
    if window == janela1 and event == 'Pedra' and machine_choice == 'Tesoura':
        janela1.close()
        janela2 = ganhou()
    if window == janela1 and event == 'Papel' and machine_choice == 'Pedra':
        janela1.close()
        janela2 = ganhou()
    if window == janela2 and event == 'Voltar':
        janela2.close()
        janela1 = inicio()
    if window == janela2 and event == 'Cancelar':
        break

'''
while True:
    choice = int(input('Qual sua escolha?: \n'
                       'Pedra: Digite 1\n'
                       'Papel: Digite 2\n'
                       'Tesoura: Digite 3\n'
                       'Encerrar: Digite 4\n'))
    if choice not in [1, 2, 3, 4]:
        continue
    if choice == 4:
        break
    else:
        machine_choice = random.choice((1, 2, 3))
        #if choice == machine_choice:
            print('Empate\n') 
        #if choice == 1 and machine_choice == 2:
            print('Você escolheu Pedra e a máquina Papel. Você perdeu !!\n')
        #if choice == 2 and machine_choice == 3:
            print('Você escolheu Papel e a máquina Tesoura. Você perdeu !!\n')
        #if choice == 3 and machine_choice == 1:
            print('Você escolheu Tesoura e a máquina Pedra. Você perdeu !!\n')
        if choice == 1 and machine_choice == 3:
            print('Você escolheu Pedra e a máquina Tesoura. Você ganhou !!\n')
        if choice == 2 and machine_choice == 1:
            print('Você escolheu Papel e a máquina Pedra. Você ganhou !!\n')
        if choice == 3 and machine_choice == 2:
            print('Você escolheu Tesoura e a máquina Papel. Você ganhou !!\n')

'''

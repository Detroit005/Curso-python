import PySimpleGUI as sg 
import numpy as np
n=0
layout = [[sg.Text('Digite a quantidade de números que dejesa iserir:')],
    [sg.Input(key='N')],[sg.Button('ok'),sg.Button('Cancelar')]]
jan = sg.Window('Calculadora',layout)
while True:
    evento, valores = jan.read()
    if evento == sg.WIN_CLOSED or evento =='cancelar':
        jan.close()
        break
    if evento == 'ok':
        try:
            n = int(valores['N'])
            if n <=0:
                sg.popup('Insira somente números positivos')
                continue
            break
        except:
            sg.popup('Por favor, insira um valor valido')
jan.close()
numeros = [] #outra lista
for i in range(n):
    layout = [[sg.Text(f'Digite o {i+1}° número')],[sg.Input(key='C')],[sg.Button('ok'),sg.Button('Cancelar')]]
    janela = sg.Window('Entrada de número', layout)
    while True:
        evento, valores = janela.read()  
        if evento == sg.WIN_CLOSED or evento =='Cancelar':
            jan.close()
            break
        if evento == 'ok':
            try:
                num = int(valores['C'])
                numeros.append(num)
                break
            except:
                sg.popup('Por favor, insira valores validos')
jan.close()
# Numpy
vetor = np.array(numeros)
soma = np.sum(vetor)
media = np.mean(vetor)
# Resultados
sed_layout = [[sg.Text('Elementos do vetor')],[sg.Text(','.join(map(str,vetor)))],
              [sg.Text(f'Soma dos elementos = {soma}')],[sg.Text(f'Media dos elementos:')],
              [sg.Button('Fechar')]]
resultado_janela = sg.Window('Resultado',sed_layout)
while True:
    eventor = resultado_janela.read()
    if eventor == sg.WIN_CLOSED or 'Fechar' in eventor:
        resultado_janela.close()
        break
resultado_janela.close()
if __name__ =='__main__':
    main()
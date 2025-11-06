from streamlit import header,write,text_input,button,warning,error,set_page_config
from math import sqrt,pow
set_page_config(page_title = 'Bhaskara Calculator')
# Função python
def calculo(delta):
    valor = (sqrt(delta)) / 2 * a
    return valor
header('Calculadora Bhaskara')
write('Calculadora de raízes \n de uma equação de 2º grau')
write('ax² + bx + c = 0')
# Entrada
a = text_input(f'Digite o valor de a:')
b = text_input(f'Digite o valor de b:')
c = text_input(f'Digite o valor de c:')
# Processamento
if button('Calcular raízes'):
    try:
        a = float(a)
        b = float(b)
        c = float(c)
        delta = pow(b,2) - 4 * a * c
        if delta < 0:
            warning('A equação não possui raízes reais')
        elif delta == 0:
            raiz= (-b + calculo(delta))
            write(f'A equação possui uma raiz real: {raiz}')
        else:
            raiz1= (-b + calculo(delta))
            raiz2 = (-b - calculo(delta))
            write(f'As raízes da equação são: \n Raíz-1:{raiz1: .2f} \n Raíz-2: {raiz2: .2f}')
    except ValueError:
        error('Por favor, insira valores validos para a, b e c')
    except ZeroDivisionError:
        error('O valor de "a" não pode ser zero em uma equação de 2º grau')
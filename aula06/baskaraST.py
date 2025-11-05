import streamlit as st 
import math as mt
st.set_page_config(page_title = 'Bhaskara Calculator')
st.header('Calculadora Bhaskara')
st.write('Calculadora de raízes \n de uma equação de 2º grau')
st.write('ax² + bx + c = 0')
# Entrada
a = st.text_input('Digite o valor de a:')
b = st.text_input('Digite o valor de b:')
c = st.text_input('Digite o valor de c:')
# Processamento
if st.button('Calcular raízes'):
    try:
        a = float(a)
        b = float(b)
        c = float(c)
        delta = mt.pow(b,2) - 4 * a * c
        if delta < 0:
            st.warning('A equação não possui raízes reais')
        elif delta == 0:
            raiz= (-b + mt.sqrt(delta)) / (2*a)
            st.write(f'A equação possui uma raiz real: {raiz}')
        else:
            raiz1= (-b + mt.sqrt(delta)) / (2*a)
            raiz2 = (-b - mt.sqrt(delta)) / (2*a)
            st.write(f'As raízes da equação são: \n Raíz-1:{raiz1:.2f} \n Raíz-2: {raiz2:.2f}')
    except:
        st.error('Por favor, insira valores validos para a, b e c')
st.write('Valor de delta é: {delta}')
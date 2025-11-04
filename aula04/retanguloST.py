import streamlit as st
# Problema Retângulo
st.title('Problema Retângulo')
# Entrada de dados
base = st.number_input('Digite a base do reângulo: ')
altura = st.number_input('Digite a altura do retângulo: ')
# Processamento de dados 
area = base * altura
perimetro = 2 * (base + altura)
diagonal = (base**2 + altura**2)**0.5
# Saída de dados 
st.write(f'A área do retângulo é: {area}')
st.write(f'O perímetro do retângulo é: {perimetro}')
st.write(f'A diagonal do retângulo é: {diagonal}')
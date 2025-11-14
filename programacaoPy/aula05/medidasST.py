import streamlit as st #Framework
import math as mt 
# Problemas medidas:
TITULO = 'Calculo de área de um quadrado, triângulo e trapézio'
st.markdown('<h1 style='text-align:)
# Entrada de dados
medidaA = st.number_input('Inserir a medida A: ',min_value = 0.0)
medidaB = st.number_input('Inserir a medida B: ',min_value = 0.0)
medidaC = st.number_input('Inserir a medida C: ',min_value = 0.0)
# Processamento de dados
areaQuadrado = mt.pow(medidaA, 2)
areaTriangulo = (medidaA * medidaB)/2
areaTrapezio = ((medidaA + medidaC) * medidaB)/2
# Saída de dados
st.markdown('<h2 style='text-align: left;'>Resultados:<\h2>', unsafe_allow_html=True)
st.write(f'A área do quadrado é: {areaQuadrado:.4f}')
st.write(f'A área do quadrado é: {areaTriangulo:.4f}')
st.write(f'A área do quadrado é: {areaTrapezio:.4f}')
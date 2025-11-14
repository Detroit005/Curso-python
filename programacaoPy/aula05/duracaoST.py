import streamlit as st #Framework
# Problema duração de tempo
TITULO = 'Calculadora de Duração de Tempo'
st.set_page_config(page_title = 'Duração de tempo')
st.title(TITULO)
# Entrada de dados
tempo = st.number_input("Digite o tempo em segundos: ",min_value = 0, step = 1, 
                        help="Insira a duração total em segundos para converter em minutos e segundos")
#processamento de dados
horas = tempo // 3600 #Calculo horas
minutos = (tempo % 3600)//60 #Calculos min
segundos = tempo % 60 #Calculo seg
#Saída de dados 
st.write(f'{horas} horas, {minutos} minutos e {segundos} segundos.')
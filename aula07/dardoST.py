import streamlit as st 
st.title('🎯Simulação de lançamento de dardos🎯')
'''Simulação de lançamento de tres dardos. O objetivo do aplicativo é mostrar o dardo com a maior distância.'''
# Enrda de dados
st.header('Inserir as tres distâncias do dados lançados pelo jogador.')
coluna1,coluna2,coluna3 = st.columns(3)
with coluna1:
    dardo1 = st.number_input('Distância do 1º dardo em (m):',min_value=0.0,step=1.0)
with coluna2:
    dardo2 = st.number_input('Distância do 2º dardo em (m):',min_value=0.0,step=1.0)
with coluna3:
    dardo3 = st.number_input('Distância do 3º dardo em (m):',min_value=0.0,step=1.0)
# Estrutura de controle de decisão
if (dardo1 > dardo2) and (dardo1 > dardo3):
    dardo_vencedor = 'Dardo 1'
elif (dardo2 > dardo1) and (dardo2 > dardo3):
    dardo_vencedor = "Dardo 2"
else:
    dardo_vencedor = "Dardo 3"
# Saida de dados
if st.button('Apresentar lançamentos'):
    st.write(f'O dardo com maior distãncia é {dardo_vencedor}🎉🎉')
import streamlit as st 
def grafico(datsu1,datsu2,datsu3):
    # Apresentação de grafico exibindo lançamento
    st.bar_chart([0,1,2,3,4,5,6,7,8,9, datsu1],use_container_width=True,height=200, color="#fff700")
    st.bar_chart([0,1,2,3,4,5,6,7,8,9, datsu2],use_container_width=True,height=200, color="#ff005d")
    st.bar_chart([0,1,2,3,4,5,6,7,8,9, datsu3],use_container_width=True,height=200, color="#002aff")
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
maior_dist = max(dardo1,dardo2,dardo3)
# Estrutura de controle de decisão
if (dardo1 > dardo2) and (dardo1 > dardo3):
    dardo_vencedor = 'Dardo 1'
elif (dardo2 > dardo1) and (dardo2 > dardo3):
    dardo_vencedor = "Dardo 2"
elif (dardo1 == dardo2) or (dardo1 == dardo3) or (dardo2 == dardo3):
    dardo_vencedor = 'Empate'
else:
    dardo_vencedor = "Dardo 3"
# Saida de dados
if st.button('Apresentar lançamentos'):
    if dardo_vencedor == 'Empate':
        st.error('Houve empate, sem vencedores😔')
    else:
        st.success(f'🎉O dardo com maior distância é {dardo_vencedor} com {maior_dist} de distância🎉')
        grafico(dardo1,dardo2,dardo3)
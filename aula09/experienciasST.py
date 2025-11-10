import streamlit as st 
# Problema experiencias
st.title('Laboratório de cobaias')
# Entrada de dados
n = st.number_input('Digite o número de experimentos:',min_value=0,step=1)
t_c= 0
t_r= 0
t_s= 0
t_cl= 0
# Entrada de dados
n=st.number_input('Digite o número de experiencias:',min_value=0,step=1)
# Estrutura de controle 
for i in range(n):
    quantidade = st.number_input(f'Experimento {i+1} - Quantidade de cobaias utilizadas:',min_value=0,step=1)
    tipo =  st.selectbox(f'Experimento {i+1} - Tipo cd cobaia (C:Coelho, R:Rato, S:Sapo):', options=['C','R','S'])
# Processamento
    t_c+=quantidade
    if tipo == 'C':
        t_cl += quantidade
    elif tipo =='R':
        t_r += quantidade
    elif tipo =="S":
        t_s += quantidade
if t_c >0:
    p_cl = (t_cl/t_c) * 100
    p_r = (t_r/t_c) * 100
    p_s = (t_s/t_c) * 100
else: 
    p_cl = p_r = p_s = 0
# Saida de dados
st.subheader('Resultados:')
st.write('Total de cobaias utilizadas: ',t_c)
st.write('Total de cobaias utilizadas: ',t_cl)
st.write('Total de cobaias utilizadas: ',t_r)
st.write('Total de cobaias utilizadas: ',t_s)
# Percentual
st.write(f'Percentual de coelhos: {p_cl:.2f} %')
st.write(f'Percentual de ratos: {p_r:.2f} %')
st.write(f'Percentual de sapos: {p_s:.2f} %')
import streamlit as st 
# Porcentagem
def porcentagem(c):
    return (c / t_c) * 100
def qtd(t):
    t += quantidade
    return t
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
    t_c = qtd(t_c)
    if tipo == 'C':
        t_cl = qtd(t_cl)
    elif tipo =='R':
        t_r = qtd(t_r)
    elif tipo =="S":
        t_s = qtd(t_cl)
if t_c >0:
    p_cl = porcentagem(t_cl)
    p_r = porcentagem(t_r)
    p_s = porcentagem(t_s)
else: 
    p_cl = p_r = p_s = 0
# Saida de dados
st.subheader('Resultados:')
st.write('Total de cobaias utilizadas: ',t_c)
st.write('Total de coelhos utilizados: ',t_cl)
st.write('Total de ratos utilizados: ',t_r)
st.write('Total de sapos utilizadas: ',t_s)
# Percentual
if p_cl>0:
    st.write(f'Percentual de coelhos: {p_cl:.2f} %')
elif p_r>0:
    st.write(f'Percentual de ratos: {p_r:.2f} %')
elif p_s>0:
    st.write(f'Percentual de sapos: {p_s:.2f} %')
else:
    st.write('Sem resultados')
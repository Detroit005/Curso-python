import streamlit as st 
# Tabuada
T = 'Tabuada'
st.title(T)
st.set_page_config(T)
# Entrada
n = None
botao = st.button('Calcular')
try:
    n = int(st.number_input('Deseja a tabuada de qual número?',step=1))
    if botao == True:
        for i in range(1,11):
                saida = f'{n} X {i} = {n*i}'
                st.markdown(f'''{saida}''')
except ValueError:
    if n is None:
        st.warning('Digite algum valor')
    else:
        st.error('Digigte somente números inteiros')

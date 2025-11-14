import streamlit as st 
# Site de vendas
TITULO = 'Compra'
st.set_page_config(page_title = 'Calculo do troco')
st.title(TITULO)
# Entrada de dados 
precoP = st.number_input('Preço do produto: ', min_value=0.00,step=1.00)
quant = st.number_input('Quantidade de produtos: ', min_value=0, step=1)
pagamentoC = st.number_input('Quanto você irá pagar? ', min_value=0.00,step=1.00)
#Processamento de dados 
totalcompra = precoP * quant
troco = pagamentoC - totalcompra
troco2 = troco * -1
#Saída de dados
st.write(f'Valor do produto R$ {precoP:.2f}')
st.write(f'Quantidade de produtos: {quant}')
st.write(f'Valor pago R$ {pagamentoC:.2f}')
st.write(f'O total da sua compra é R$ {totalcompra:.2f}')
if troco < 0:
    st.write(f'Pagamento insuficiente, você deve pagar mais R$ {troco2:.2f} .')
elif troco == 0:
    st.write('Pagamento exato, sem troco.')
else:
    st.write(f'Seu troco é de R$ {troco:.2f}')
pass
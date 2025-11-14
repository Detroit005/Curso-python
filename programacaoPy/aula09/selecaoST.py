import streamlit as st 
# pobrema lanchonete
st.title('Clodolneche')
st.header('Menu de opções')
st.subheader('Opções de lanches')
st.markdown(''' 
| Código | Descrição do item | Preço  |
|--------|-------------------|--------|
| 1001   | X-Burguer         |R$ 8,00 |
| 1002   | X-SENAI           |R$ 10,00|
| 1003   | X-Campeão         |R$ 12,00|
| 1004   | X-C37             |R$ 15,00|
| 1005   | X-ESP32           |R$ 18,00|
''')
opcao = st.selectbox('Selecione o código do lanche: ',
                     options=['1001','1002','1003','1004','1005'])
codigo = int(opcao)
quantidade = st.number_input('Digite a quantidade desejada:',min_value=1,step=1)
match codigo:
    case 1001:
        preco = 8.00
    case 1002:
        preco = 10.00
    case 1003:
        preco = 12.00
    case 1004:
        preco = 15.00
    case 1005:
        preco = 18.00
total = preco * quantidade
st.subheader('Total a pagar: R$ '+ (str(total)))

import streamlit as st 
# Titulo
st.title('Sistema de login simples')
# declaraçao]
U='clodoaldo'
S='senha123'
# entrada
usuario_enter=st.text_input('Nome do usuario:')
senha_enter= st.text_input('Senha',type='password')
# controle loop
botao=st.button('Logar')
# tentativas
MAXIMO_TENTATIAS = 3
if 'tentativas' not in st.session_state:
    st.session_state.tentativas = 0
if botao:
    if st.session_state.tentativas >= MAXIMO_TENTATIAS:
        st.error('Maximo de tentativas atingido. Acesso bloqueado')
    else:
        while st.session_state.tentativas <MAXIMO_TENTATIAS:
            if usuario_enter==U and senha_enter==S:
                st.success('Login bem sucedido!🎉')
                st.session_state.tentativas = 0
                break
            else:
                st.session_state.tentativas+=1
                tentativas_r = MAXIMO_TENTATIAS - st.session_state['tentativas']
                st.warning(f'Credenciais invalidas. Tentativas restantes {tentativas_r}')
                break

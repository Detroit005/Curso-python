import streamlit as st 
st.title('Confirmação de triângulo')
st.set_page_config(page_title='Triângulo')
# entrada
a = st.number_input('Digite a primeira medida (base menos):',min_value=0.0, format='%.2f',step=1.0)
b = st.number_input('Digite a segunda medida (base maior):',min_value=0.0, format='%.2f',step=1.0)
c = st.number_input('Digite a terceira medida (altura):',min_value=0.0, format='%.2f',step=1.0)
# processamento / saida
if st.button('Calcular'):
        if a <= 0 or b <= 0 or c <= 0:
            st.warning('Insira valores maiores que zero para as medidas')
        elif (a+b)>c and (a+c)>b and (b+c)>a :
            p= a+b+c
            st.success('A figura é um triângulo')
            if a==b and b==c and a==c:
                st.write('A figura é um triângulo equilatero')
            elif a==c and a==b:
                st.write('A figura é um triângulo isósceles')
            else:
                st.write('A figura é um triângulo escaleno')
            st.write(f'O perímetro do triângulo é: {p:.2f}')
        else:
            t = (a+b)*c/2
            st.error('A figura formada será um trapésio')
            st.write(f'A área do trapézio é: {t:.2f}')
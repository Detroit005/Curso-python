import streamlit as st 
st.title('Calculadora de níveis de glicose no sangue')
st.set_page_config(page_title = 'Níveis de glicose')
st.markdown(
    """
| Nível de glicose | Classificação |
|------------------|---------------|
|      0 - 70      | Hipoglicemia  |
|     71 - 100     |    Normal     |
|    101 - 140     | Pré-diabetes  |
|    141 ou mais   |   Diabetes    |
""")
glicose = st.number_input('Insira o nível de glicose no sangue (mg/dl): ', min_value = 0)
if st.button('Classificar'):
    if glicose <= 70:
        st.write('Classificação: Hipoglicemico')
    elif glicose <= 100:
        st.write('Classificação: Normal')
        st.balloons()
        # st.confetti()
    elif glicose <= 140:
        st.write('Classificação: Pré-diabetico')
    else:
        st.write('Classificação: Diabetico')

import streamlit as st

st.title("👥 Cadastro de Pessoas")

n = st.number_input('Digite o número de pessoas:', min_value=1, max_value=10, step=1)

nomes = []
idades = []
alturas = []

# Entrada de dados
for i in range(n):
    st.subheader(f'{i+1}ª Pessoa')
    nome = st.text_input(f'Nome da pessoa {i+1}:', key=f'nome_{i}')
    idade = st.number_input(f'Idade da pessoa {i+1}:', min_value=0, max_value=150, step=1, key=f'idade_{i}')
    altura = st.number_input(f'Altura da pessoa {i+1} (m):', min_value=0.3, max_value=3.0, step=0.3, key=f'altura_{i}')
    
    nomes.append(nome)
    idades.append(idade)
    alturas.append(altura)

# Botão para calcular
if st.button('Calcular Resultados'):
    if any(nome == "" for nome in nomes):
        st.warning(" Preencha todos os nomes antes de calcular.")
    else:
        media_altura = sum(alturas) / n
        menores = [nomes[i] for i in range(n) if idades[i] < 16]
        porcentagem_menores = (len(menores) / n) * 100

        st.subheader(" Resultados")
        st.write(f"Altura média: **{media_altura:.2f} m**")
        st.write(f"Pessoas com menos de 16 anos: **{porcentagem_menores:.1f}%**")

        if menores:
            st.write("Nomes das pessoas com menos de 16 anos:")
            for nome in menores:
                st.write(f"- {nome}")
        else:
            st.info("Nenhuma pessoa com menos de 16 anos.")

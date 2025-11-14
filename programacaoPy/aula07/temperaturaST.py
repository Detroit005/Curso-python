import streamlit as st
# Funções de conversão
def celsius_fahrenheit(temp):
        return (temp*1.8) + 32
def celsius_kelvin(temp):
        return temp + 273.15
def f_celcius(temp):
        return (temp - 32) * 5/9
def f_kelvin(temp):
        return f_celcius(temp) + 273.15
def k_celsius(temp):
        return temp - 273.15
def k_fahrenheit(temp):
        return celsius_fahrenheit(k_celsius(temp))
# Problema temperatura
st.sidebar.title('🌡️Conversor de temperaturas🌡️')
st.title('🌡️Conversor de temperatura🌡️')
st.set_page_config(page_title='Conversor de Temp')
st.sidebar.markdown('Converte a temperatura entre Celsius, Fahrenheit e Kelvin.')
opcao_selec = st.sidebar.radio(options=['Celsius','Fahrenheit','Kelvin'],label='Selecione uma:')
# Entrada de dados
temp = st.number_input('Valor da temperatura',format='%.2f',step=1.0)
# Processamento de dados
if st.button('Converter',icon='🌡️'):
          if opcao_selec == 'Celsius':
                  st.write(f'{temp}°C em {celsius_fahrenheit(temp)}°F')
                  st.write(f'{temp}°C em {celsius_kelvin(temp)} K')
          elif opcao_selec == 'Fahrenheit':
                  st.write(f'{temp}°F em {f_celcius(temp):.2f}°C',)
                  st.write(f'{temp}°F em {f_kelvin(temp):.2f}K')
          elif opcao_selec == 'Kelvin':
                  st.write(f'{temp} K em {k_celsius(temp):.2f}°C')
                  st.write(f'{temp} K em {k_fahrenheit(temp):.2f}°F')
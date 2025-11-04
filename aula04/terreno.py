# Problema terreno
# Declaração de variaveis
largura:float
comprimento:float
# Entrada de dados
largura = float(input('Digite a largura do terreno em metros: '))
comprimento = float(input('Digite o comprimento do terreno em metros: '))
valor_metro_quadrado = float(input('Digite o valor do metro quadrado do terreno em reais: '))
# Processamento de dados
area = largura * comprimento
preco = area * valor_metro_quadrado
# Saída de dados
print(f'A área do terreno é de {area}.')
print(f'O preço do terreno é de R$ {preco}.')
# Problema triangulo sem oop
# Entrada de dados
# Triangulo x
print('Inserir as medidas do triangiulo X')
ax = int(input('Digigte a medida a:'))
bx = int(input('Digigte a medida b:'))
cx = int(input('Digigte a medida c:'))
# Triangulo Y
print('Inserir as medidas do triangiulo Y')
ay = int(input('Digite a medida a:'))
by = int(input('Digite a medida b:'))
cy = int(input('Digite a medida c:'))
# Processamento de dados
p = (ax + bx + cx) /2
areax = (p*(p-ax)* (p-bx)* (p-cx))**0.5
p = (ay + by + cy) /2
areay = (p*(p-ay)* (p-by)* (p-cy))**0.5
if areax > areay : 
    saida = 'A área do Triangulo X é maior que área do Triangulo Y'
elif areay > areax : 
    saida = 'A área do Triangulo Y é maior que área do Triangulo X'
else:
    saida = 'As áreas dos triângulos são iguais'
# saida de dados
print(f'A área do triângulo X = {areax:.1f}')
print(f'A área do triângulo Y = {areay:.1f}')
print(saida)
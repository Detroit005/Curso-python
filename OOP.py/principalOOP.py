import triaguloOOP as tl
trianguloX=tl.triangulo()
trianguloY=tl.triangulo()
# entrada de dados
print('Digite as medidas do triângulo X')
trianguloX.a = int(input('Digite a medida a:'))
trianguloX.b = int(input('Digite a medida b:'))
trianguloX.c = int(input('Digite a medida c:'))
print('Digite as medidas do triângulo Y:')
trianguloY.a = int(input('Digite a medida a:'))
trianguloY.b = int(input('Digite a medida b:'))
trianguloY.c = int(input('Digite a medida c:'))
# Processamento
areax=trianguloX.area()
areay=trianguloY.area()
# triangulo maior
if areax > areay : 
    saida = 'A área do Triangulo X é maior que área do Triangulo Y'
elif areay > areax : 
    saida = 'A área do Triangulo Y é maior que área do Triangulo X'
else:
    saida = 'As áreas dos triângulos são iguais'
# saida
print(f'A area do triangulo X = {areax:.1f}')
print(f'A area do triangulo Y = {areay:.1f}')
print(saida)
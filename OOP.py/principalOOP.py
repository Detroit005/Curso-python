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
p = ((trianguloX.a + trianguloX.b + trianguloX.c)/2)
areax = (p*(p-trianguloX.a)* (p-trianguloX.b) * (p-trianguloX.c))**0.5
p = (trianguloY.a + trianguloY.b + trianguloY.c) /2
areay = (p*(p-trianguloY.a)* (p-trianguloY.b)* (p-trianguloY.c))**0.5
# triangulo maior
if areax > areay : 
    saida = 'A área do Triangulo X é maior que área do Triangulo Y'
elif areay > areax : 
    saida = 'A área do Triangulo Y é maior que área do Triangulo X'
else:
    saida = 'As áreas dos triângulos são iguais'
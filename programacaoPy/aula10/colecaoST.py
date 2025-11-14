# indices  0        1    2   3
lista = ['Senai', True, 22, 3.5]
print(lista)
print(type(lista))
print(lista[2])
print(len(lista))
lista.insert(1,'Campeao')
lista.append('Feriado')
del lista[3]
lista.append('Senai')
for i in range(len(lista)):
    print(lista[i])

# Tupla
tupla= ('Senai', True, 56, 74.6)
print(tupla)
print(type(tupla))
print(tupla[3])
print(tupla[1])
tupla.insert(1, ' Campeao ')

# dicionário
dicionario = {'nome' : 'senai','logica': False,'num1':2,'num2':1.5}
print(dicionario)
print(type(dicionario))
print(dicionario['lógica'])
for chave in dicionario.keys():
    print(chave, '->', dicionario[chave])
dicionario.update({'novo': 'senai'})
dicionario.update({'novo': 'terca'})
del dicionario['lógica']

# conjunto
conjunto = {'senai', False, 10, 2.69}
print(conjunto)
print(type(conjunto))
print(conjunto[2])
conjunto.add(23)
conjunto.discard('senai')
conjunto.clear()
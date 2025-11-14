import produtoOOP as p 
p1 = p.Produto()
# entrada
print('Digite os dados do produto')
p1.nome=input('\tNome:')
p1.preco=float(input('\tPreco: R$'))
p1.saldo=int(input('\tQuantidade:'))
# saida 1
print('Dados do produto')
print(f'\tNome do produto: {p1.nome}')
print(f'\tValor de compra: R${p1.preco:.2f}')
print(f'\tQuantidade em estoque: {p1.saldo}')
print(f'Valor total em estoque: R${p1.valorte():.2f}')
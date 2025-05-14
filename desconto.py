produto = input('Nome do produto: ')
preço = float(input('preço do produto: '))
porcentagem = float(input('porcentagem com desconto: '))
valor_desconto = preço * (porcentagem/ 100)
valor_novo = preço - valor_desconto
print(valor_novo)
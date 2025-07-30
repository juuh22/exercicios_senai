contador = 0
fim = int(input('Escolha um número que irei somar para você:'))
soma = 0
while contador <= fim:
    soma = soma + contador
    contador = contador+1

print(f'Resultado: {soma}')   
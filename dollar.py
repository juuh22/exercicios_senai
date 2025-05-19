print('Escolha uma opçao: ')
print('1 - Dollar para real ')
print('2 - Real para dollar ')
opcao = int(input('Informe a opçao: '))
valor = float(input('Informe a cotaçao atual do dollar: '))

if opcao == 1:
    dolares = float(input('Informe a quantidade de dolares:'))
    print(f'O valor em reais é R${valor * dolares:.2f}')

elif opcao == 2:
    reais = float(input('Informe a quantidade de reais:'))
    print(f'O valor em dollar é R${reais/valor:.2f}')

else:
    print('Opcao errada.')
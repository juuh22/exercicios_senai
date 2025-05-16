print('Calculadora')
print('1 - Soma')
print('2 - Subtraçao')
print('3 - Multiplicaçao')
print('4 - Divisao')
opçoes = int(input('Digite uma das opçoes:'))
n1 = int(input('Digite o primeiro numero:'))
n2 = int(input('Digite o segundo numero:'))

if opçoes== 1:
    print('O resultado e:', n1+n2)
if opçoes== 2:
    print('O resultado e:' , n1-n2)
if opçoes== 3:
    print('O resultado e:', n1*n2)
if opçoes== 4:
    print('O resultado e:', n1/n2)
    print('Deseja continuar?')       
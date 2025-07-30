nome = input('Qual é seu nome? ')
idade = int(input('Qual é a sua idade? '))
if idade >= 18:
    print('Maior de idade')
    c_motorista = input('Possui carteira de maotorista? (1-Sim/ 2-Não)')
    if c_motorista == 1:
        print('Pode dirigir.')
        
    if c_motorista == 2:
        print('Não pode dirigir.')    
else:
   print('Menor de idade')


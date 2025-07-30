print(30*'-')
print('| CÁLCULO DE IMC')
print(30*'-')
nome = input('| Olá, qual é o seu nome? ')
altura = float(input('| Digite a sua altura: '))
peso = float(input('| Digite o seu peso: '))
Imc = peso / (altura ** 2)
print(30*'-')
print('| Seu Imc é: ' , round(Imc, 2))

if Imc <= 18.5:
    print(f'| AVISO: {nome}, Tome cuidado você está abaixo do peso! ')
    print(f'| RECOMENDAÇÃO: Procure um médico.')

elif Imc <= 24.9:
    print(f'| AVISO: Tudo certo com você {nome}, seu peso está normal. ')
    print(f'| RECOMENDAÇÃO: Caso tiver alguma dúvida procure um médico.')

elif Imc <= 29.9:
    print(f'| AVISO: Você está sobrepeso. ') 
    print(f'| RECOMENDAÇÃO: Procure fazer mais exercicios físicos diariamlmente para ajudar na sua saúde. ')

elif Imc <= 34.9:
    print(f'| AVISO: você está com Obesidade Grau |. ')
    print(f'| RECOMENDAÇÃO: Procure fazer mais exercicios e a ajuda de um médico para te ajudar a cuidar da sua saúde. ')

elif Imc <= 39.9:
    print(f'| AVISO: Você está com Obesidade Grau ||. ')   
    print(f'| RECOMENDAÇÃO: Amigo, vamos estar cuidando mais da saúde antes que você chegue no Grau 3. ')

else:
    print(f'| AVISO: Obesidade Grau |||.')
    print(f'| RECOMENDAÇÃO: Te aconselho passar com um médico ele ira dar uma guia para você passar em um nutricionista para a melhorar a sua alimentação e começar na academia.')    
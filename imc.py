# IMC formula = peso/(altura X altura)

altura = float(input('Qual é a sua altura? '))
peso = float(input('Qual é a sua peso? '))
imc= peso / (altura * altura) # round(expressaõ, quantidades de casas depois da virgula)

resultado = round(imc, 2)

print(resultado)
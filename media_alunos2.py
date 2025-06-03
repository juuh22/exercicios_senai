print('SISTEMAS DE PROVAS DOS ALUNOS')
print('')
prova = int(input('Quantas provas o aluno realizou? '))
soma = 0
contador = 1
while contador <= prova:
    nota= float(input('Digite a nota da prova: '))
    soma = soma + nota
    contador = contador+1

media = soma/prova
print(f'Média: {media}')   
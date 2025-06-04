qnt_filmes =  int(input('Quantos filmes você quer adicionar na lista? '))
contador = 1
filmes = []
while contador <= qnt_filmes:
    nome_filme = input('Digite o nome do filme: ')
    contador = contador+1
    filmes.append(nome_filme)

print(filmes)    
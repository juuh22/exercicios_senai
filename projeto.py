import os

tarefas ={
    'tarefas': ['Arrumar o quarto', 'Passear com os cachorros'],
    'datas': ['30/06', '30/06']
}

def mostrar_tarefas():
    print('-' * 40)
    print('TAREFAS:')
    for i in range(len(tarefas['tarefas'])):
        print(f'{i+1}. {tarefas['tarefas'][i]} - data: {tarefas['datas'][i]}')
    print('-' * 40)

def adicionar_tarefas():
    tarefa = input('| Digite o nome da tarefa: ')
    data = input('| Digite a data (dd/mm): ')
    tarefas['tarefas'].append(tarefa)
    tarefas['datas'].append(data)
    print('| Tarefa adicionada com sucessoo!!')

def remover_tarefa():



def menu():
    while True:
        os.system('cls')
        print('-' * 25)
        print('| TAREFAS')
        print('-' * 25)
        print('| (1) Mostrar tarefas')
        print('| (2) Adicionar tarefas')
        print('| (3) Remover tarefa')
        print('| (4) Sair')
        print('-' * 25)
        opcao = int(input('| Escolha uma das opçoes:'))


        if opcao == 1:
            os.system('cls')
            mostrar_tarefas()
            input('Pressione o enter para continuar..')

        if opcao == 2:
            adicionar_tarefas()
            input('Pressione o enter para continuar..')

        if opcao == 3:
            print()

        if opcao == 4:
            print('encerrando...')
            break
        
        else:
            print('Digite uma opçao válida.')


menu()

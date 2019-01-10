from funcoes import *
from menu import menu_demandas

opcao = 0
while opcao != 10:
    menu_demandas()
    opcao = int(input('Informe uma opção: '))

    if opcao == 1:
        id_projeto = int(input('Informe o Id do projeto: '))
        descricao = input('Informe o descricao do contato: ')
        data_ent = input('Informe a data de entrega: ')

        lista_data = data_ent.split('-')
        lista_data.reverse()
        data_entrega = '-'.join(lista_data)

        cadastrar_d(id_projeto, descricao, data_entrega)

    elif opcao == 2:
        id_projeto = input('Digite aqui o id do projeto para ver suas demandas:')
        listar_todos_d(id_projeto)
    elif opcao == 3:
        id = int(input('Informe o ID para poder buscar: '))
        buscar_por_id_d(id)
    elif opcao == 4:
        descricao = input('Informe o descrição do contato para poder buscar: ')
        buscar_por_descricao_d(descricao)
    elif opcao == 5:
        id = int(input('Informe o ID do contato que você desaja alterar: '))
        alterar_descricao_d(id)
    elif opcao == 6:
        id = input('Informe o ID do contato para alterar o Id do projeto: ')
        alterar_id_projeto_d(id)
    elif opcao == 7:
        id = int(input('Informe o ID para ativar o projeto: '))
        ativar_d(id)
    elif opcao == 8:
        id = int(input('Informe o ID para inativar o projeto: '))
        inativar_d(id)
    elif opcao == 9:
        id = int(input('Informe o ID do contato para que possa ser excluida: '))
        excluir_d(id)
    elif opcao == 10:
        print("SAINDO...")
        break

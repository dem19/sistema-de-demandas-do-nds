from funcoes import *
from menu import menu_projetos

opcao = 0
while True:
    menu_projetos()
    opcao = int(input('Informe uma opção: '))

    if opcao == 1:
        nome = input('Informe o nome: ')
        descricao = input('Informe o descrição: ')
        data_cad = input('Informe a Data de cadastro: ')
        data_ent = input('Informe a Data de entrega: ')

        lista_data = data_cad.split('-')
        lista_data.reverse()
        data_cadastro = '-'.join(lista_data)
        lista_data = data_ent.split('-')
        lista_data.reverse()
        data_entrega = '-'.join(lista_data)

        cadastrar_p(nome, descricao, data_cadastro, data_entrega)


    elif opcao == 2:
        print('Esses são os contatos listados')
        listar_todos_p()
    elif opcao == 3:
        id = int(input('Informe o ID para poder buscar: '))
        buscar_por_id_p(id)
    elif opcao == 4:
        nome = input('Informe o nome do contato para poder buscar: ')
        buscar_por_descricao_p(nome)
    elif opcao == 5:
        id = int(input('Informe o ID do contato para alterar a descrição: '))
        alterar_descricao_p(id)
    elif opcao == 6:
        id = int(input('Informe o ID do contato para alterar o nome: '))
        alterar_nome_p(id)
    elif opcao == 7:
        id = int(input('Informe o ID do contato para alterar o nome: '))
        ativar_p(id)
    elif opcao == 8:
        id = int(input('Informe o ID do contato para alterar o nome: '))
        inativar_p(id)
    elif opcao == 9:
        id = int(input('Informe o ID do contato para que possa ser excluida: '))
        excluir_p(id)

    elif opcao == 10:
        print("SAINDO...")
        break

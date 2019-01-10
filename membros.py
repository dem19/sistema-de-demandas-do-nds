from funcoes import *
from menu import menu_membros

opcao = 0
while opcao != 8:
    menu_membros()
    opcao = int(input('Informe uma opção: '))

    if opcao == 1:
        nome = input('Informe o nome: ')
        email = input('Informe o E-mail do contato: ')
        gerente = input('Informe se o contato é gerente: ')
        if gerente == "sim":

            dev,frontend,backend,fullstack = True,True,True,True
        elif gerente == "nao":
            funcao = input('Com o que você trabalha(Fullstack, Backend ou Frontend)?')
            if funcao == 'Fullstack':
                fullstack = True
                backend, frontend = True, True
            elif funcao == 'Backend':
                backend = True
                fullstack, frontend = False, False
            elif funcao == 'Frontend':
                frontend = True
                fullstack, backend = False, False
            else:
                print('Opção inválida')
                exit()
        else:
            print("Opção inválida")
            exit()

        id_projeto = int(input('Informe o id do projeto que ele participará: '))

        cadastrar_m(nome, email, gerente, dev, fullstack, backend, frontend, id_projeto)

    elif opcao == 2:
        id_projeto = input("Id do projeto a ser mostrado seus membros:")
        listar_todos_m(id_projeto)
    elif opcao == 3:
        id = int(input('Informe o ID para poder buscar: '))
        buscar_por_id_m(id)
    elif opcao == 4:
        nome = input('Informe o nome do contato para poder buscar: ')
        buscar_por_nome_m(nome)
    elif opcao == 5:
        id = int(input('Informe o ID do contato que você desaja alterar o nome: '))
        alterar_nome_m(id)
    elif opcao == 6:
        id = int(input('Informe o ID do contato para alterar o E-mail: '))
        alterar_email_m(id)
    elif opcao == 7:
        id = int(input('Informe o ID do contato para que possa ser excluida: '))
        excluir_m(id)
    elif opcao == 8:
        print("SAINDO...")

        break

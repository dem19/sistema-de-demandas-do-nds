import sqlite3

BD = 'ProjetoAB.db'

######################################       PRONTO       ####################################################
def listar_todos():
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = "SELECT * FROM membros"
    cursor.execute(sql)
    ProjetoAB = cursor.fetchall()
    if ProjetoAB.__len__() > 0:
        for produto in ProjetoAB:
            print('Id: ', produto[0], ' - nome: ', produto[1],
                  ' - email: ', produto[2], ' - gerente: ', produto[3],
                  ' - dev: ', produto[4], '- backend',produto[5],'- frontend',produto[6],
                  '- fullstack',produto[7],'- id_projeto',produto[8])
    else:
        print('Nenhum produto cadastrado!')
    cursor.close()
    conexao.close()
######################################      PRONTO     ####################################################

def buscar_por_id(id):
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = "SELECT * FROM membros WHERE id='%d'" % id
    cursor.execute(sql)
    produto = cursor.fetchone()
    if produto:
        print('Id: ', produto[0], ' - nome: ', produto[1],
              ' - email: ', produto[2], ' - gerente: ', produto[3],
              ' - dev: ', produto[4], '- backend', produto[5], '- frontend', produto[6],
              '- fullstack', produto[7], '- id_projeto', produto[8])

        return True
    else:
        print('Nenhum produto cadastrado!')
        return False
    cursor.close()
    conexao.close()

######################################      PRONTO      ##################################################

def buscar_por_nome(nome):
    descricao = nome+'%'
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = "SELECT * FROM membros WHERE nome LIKE '%s'" % nome
    cursor.execute(sql)
    ProjetoAB = cursor.fetchall()
    if ProjetoAB:
        for produto in ProjetoAB:
            print('Id: ', produto[0], ' - nome: ', produto[1],
                  ' - email: ', produto[2], ' - gerente: ', produto[3],
                  ' - dev: ', produto[4], '- backend', produto[5], '- frontend', produto[6],
                  '- fullstack', produto[7], '- id_projeto', produto[8])
        return True
    else:
        print('Não tá cadastrado!')
        return False
    cursor.close()
    conexao.close()

######################################      PRONTO      ##################################################

def cadastrar(nome,email,gerente,dev,backend,frontend,fullstack,id_projeto):
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = "INSERT INTO membros (nome,email,gerente,dev,backend,frontend,fullstack,id_projeto) VALUES \
          ('%s','%s','%s','%s','%s','%s','%s','%d')" %(nome,email,gerente,dev,backend,frontend,fullstack,id_projeto)

    cursor.execute(sql)
    if cursor.rowcount == 1:
        conexao.commit()
        print(nome, ' cadastrado')
    else:
        conexao.rollback()
        print('Não foi possível cadastrar')
    cursor.close()
    conexao.close()

###################################    PRONTO    ##############################################################



def excluir(id):
    if buscar_por_id(id):
        resposta = input('Deseja realmente exlcuir este produto? ').lower()
        if resposta == 's':
            conexao = sqlite3.connect(BD)
            cursor = conexao.cursor()
            sql = "DELETE FROM membros WHERE id='%d'" % id
            cursor.execute(sql)
            if cursor.rowcount == 1:
                conexao.commit()
                print('Nome deletado!')
            else:
                conexao.rollback()
                print('Não foi possível deletar Nome')

###################################    PRONTO    ##############################################################


def alterar_nome(id):
    if buscar_por_id(id):
        nome = input('Informe o nome: ')
        conexao = sqlite3.connect(BD)
        cursor = conexao.cursor()
        sql = "UPDATE membros SET nome='%s' WHERE id='%d' " % (nome, id)
        cursor.execute(sql)
        if cursor.rowcount == 1:
            conexao.commit()
            print('Nome alterado!')
        else:
            conexao.rollback()
            print('Não foi possível alterar o Nome')

###################################   PRONTO     ##############################################################


def alterar_email(id):
    if buscar_por_id(id):
        email = input('Informe o novo Email: ')
        conexao = sqlite3.connect(BD)
        cursor = conexao.cursor()
        sql = "UPDATE membros SET email='%s' WHERE id='%d'" % (email, id)
        cursor.execute(sql)
        if cursor.rowcount == 1:
            conexao.commit()
            print('Email alterado!')
        else:
            conexao.rollback()
            print('Não foi possível alterar Email')


print('############################################')
print('#        1 - Cadastrar Membros             #')
print('#        2 - Listar Todos                  #')
print('#        3 - Buscar por ID                 #')
print('#        4 - Buscar por nome               #')
print('#        5 - Alterar nome                  #')
print('#        6 - Alterar E-mail                #')
print('#        7 - Excluir ID                    #')
print('#        99 - SAIR                         #')
print('############################################')

op = 0
while op != 99:
    op = int(input('Informe uma opção: '))

    if op == 1:
        nome = input('Informe o nome: ')
        email = input('Informe o E-mail do contato: ')
        gerente = input('Informe se o contato é gerente: ')
        id_projeto = int(input('Informe o id do projeto: '))
        if gerente == 's':

            
        if gerente == 'n':

            dev = input("Informe se é desenvolvedor: ")
            fullstack = input('Informe se o contato é Fullstack: ')
            backend = input('Informe se o contato é Backend: ')
            frontend = input('Informe se o contato é Frontend: ')
            id_projeto = int(input('Informe o id do projeto: '))



            cadastrar(nome,email,gerente,dev,backend,frontend,fullstack,id_projeto)

    elif op == 2:
        print('Esses são os contatos listados')
        listar_todos()
    elif op == 3:
        id = int(input('Informe o ID para poder buscar: '))
        buscar_por_id(id)
    elif op == 4:
        nome = input('Informe o nome do contato para poder buscar: ')
        buscar_por_nome(nome)
    elif op == 5:
        id = int(input('Informe o ID do contato que você desaja alterar: '))
        alterar_nome(id)
    elif op == 6:
        id = input('Informe o ID do contato para alterar o E-mail: ')
        alterar_email(id)
    elif op == 7:
        id = int(input('Informe o ID do contato para que possa ser excluida: '))
        excluir(id)
    elif op == 99:
        print("SAINDO...")

        break





import sqlite3

BD = 'ProjetoAB.db'

######################################       PRONTO       ####################################################
def listar_todos():
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = "SELECT * FROM demandas"
    cursor.execute(sql)
    ProjetoAB = cursor.fetchall()
    if ProjetoAB.__len__() > 0:
        for produto in ProjetoAB:
            print('Id: ', produto[0], ' - id_projeto: ', produto[1],
                  ' - Descrição: ', produto[2], ' - Data_entrega: ', produto[3], '- Ativa',produto[4])
    else:
        print('Nenhum projeto cadastrado!')
    cursor.close()
    conexao.close()
######################################      PRONTO     ####################################################

def buscar_por_id(id):
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = "SELECT * FROM projetos WHERE id='%d'" % id
    cursor.execute(sql)
    produto = cursor.fetchone()
    if produto:
        print('Id: ', produto[0], ' - id_projeto: ', produto[1],
              ' - Descrição: ', produto[2], ' - Data_entrega: ', produto[3], '- Ativa', produto[4])

        return True
    else:
        print('Nenhum projeto cadastrado!')
        return False
    cursor.close()
    conexao.close()

######################################      PRONTO      ##################################################

def buscar_por_descricao(descricao):
    descricao = descricao+'%'
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = "SELECT * FROM demandas WHERE descricao LIKE '%s'" % descricao
    cursor.execute(sql)
    ProjetoAB = cursor.fetchall()
    if ProjetoAB:
        for produto in ProjetoAB:
            print('Id: ', produto[0], ' - id_projeto: ', produto[1],
                  ' - Descrição: ', produto[2], ' - Data_entrega: ', produto[3], '- Ativa',produto[4])
        return True
    else:
        print('Não tá cadastrado!')
        return False
    cursor.close()
    conexao.close()

######################################      PRONTO      ##################################################

def cadastrar(id_projeto,descricao,data_entrega,ativa):
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = "INSERT INTO demandas(id_projeto,descrição,data_entrega,ativa) VALUES ('%d','%s','%s','%s')" % (id_projeto,descricao,data_entrega,ativa)
    cursor.execute(sql)
    if cursor.rowcount == 1:
        conexao.commit()
        print(descricao, ' cadastrado')
    else:
        conexao.rollback()
        print('Não foi possível cadastrar')
    cursor.close()
    conexao.close()

###################################    PRONTO    ##############################################################



def excluir(id):
    if buscar_por_id(id):
        resposta = input('Deseja realmente exlcuir? ').lower()
        if resposta == 's':
            conexao = sqlite3.connect(BD)
            cursor = conexao.cursor()
            sql = "DELETE FROM projetos WHERE id='%d'" % id
            cursor.execute(sql)
            if cursor.rowcount == 1:
                conexao.commit()
                print('Nome deletado!')
            else:
                conexao.rollback()
                print('Não foi possível deletar Nome')

###################################    PRONTO    ##############################################################


def alterar_descricao(id):
    if buscar_por_id(id):
        descricao = input('Informe a descrição: ')
        conexao = sqlite3.connect(BD)
        cursor = conexao.cursor()
        sql = "UPDATE projetos SET descricao='%s' WHERE id='%d' " % (descricao, id)
        cursor.execute(sql)
        if cursor.rowcount == 1:
            conexao.commit()
            print('Nome alterado!')
        else:
            conexao.rollback()
            print('Não foi possível alterar o Nome')

###################################   PRONTO     ##############################################################

def alterar_id_projeto(id_projeto):
    if buscar_por_id(id):
        id_projeto = input('Informe o novo Id do projeto: ')
        conexao = sqlite3.connect(BD)
        cursor = conexao.cursor()
        sql = "UPDATE projetos SET nome='%s' WHERE id='%d'" % (id_projeto,id)
        cursor.execute(sql)
        if cursor.rowcount == 1:
            conexao.commit()
            print('Nome alterado!')
        else:
            conexao.rollback()
            print('Não foi possível alterar Nome')

###################################   OLHAR       ##############################################################


def ativar(id):
    if buscar_por_id(id):
        conexao = sqlite3.connect(BD)
        cursor = conexao.cursor()
        sql = "UPDATE membros SET ativo='True' WHERE id='%d'" % id
        cursor.execute(sql)
        if cursor.rowcount == 1:
            conexao.commit()
            print('Produto ativado!')
            return True
        else:
            conexao.rollback()
            print('Não foi possível ativar produto')

###################################   OLHAR     ##############################################################


def inativar(id):
    if buscar_por_id(id):
        conexao = sqlite3.connect(BD)
        cursor = conexao.cursor()
        sql = "UPDATE membros SET ativo='False' WHERE id='%d'" % id
        cursor.execute(sql)
        if cursor.rowcount == 1:
            conexao.commit()
            print('Produto inativado!')
        else:
            conexao.rollback()
            print('Não foi possível inativar produto')



print('##############################################')
print('#          1 - Cadastrar Membros             #')
print('#          2 - Listar Todos                  #')
print('#          3 - Buscar por ID                 #')
print('#          4 - Buscar por descrição          #')
print('#          5 - Alterar Descrição             #')
print('#          6 - Alterar data de entrega       #')
print('#          7 - Excluir ID                    #')
print('#          99 - SAIR                         #')
print('##############################################')

op = 0
while op != 99:
    op = int(input('Informe uma opção: '))

    if op == 1:
        id_projeto = int(input('Informe o Id do projeto: '))
        descricao = input('Informe o descricao do contato: ')
        data_ent = input('Informe a data de entrega: ')
        ativa = input('Informe se o contato é ativa: ')
        if ativa == 't':
            ativa = True
            #ativa == ativ

        else:
            ativa = False
            #ativa == ativ

        lista_data = data_ent.split('-')
        lista_data.reverse()
        data_entrega = '-'.join(lista_data)

        cadastrar(id_projeto,descricao,data_entrega,ativa)

    elif op == 2:
        print('Esses são os contatos listados')
        listar_todos()
    elif op == 3:
        id = int(input('Informe o ID para poder buscar: '))
        buscar_por_id(id)
    elif op == 4:
        descricao = input('Informe o descrição do contato para poder buscar: ')
        buscar_por_descricao(descricao)
    elif op == 5:
        id = int(input('Informe o ID do contato que você desaja alterar: '))
        alterar_descricao(id)
    elif op == 6:
        id = input('Informe o ID do contato para alterar o Id do projeto: ')
        alterar_id_projeto(id)
    elif op == 7:
        id = int(input('Informe o ID do contato para que possa ser excluida: '))
        excluir(id)
    elif op == 8:
        ativar(id)
    elif op == 9:
        inativar(id)
    elif op == 99:
        print("SAINDO...")
        break


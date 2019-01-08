

import sqlite3

BD = 'ProjetoAB.db'

######################################       PRONTO       ####################################################
def listar_todos():
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = "SELECT * FROM projetos"
    cursor.execute(sql)
    ProjetoAB = cursor.fetchall()
    if ProjetoAB.__len__() > 0:
        for produto in ProjetoAB:
            print('Id:',produto[0], ' - nome:',produto[1],
                  ' - Descrição:',produto[2],' - Data_Cadastro:',produto[3],
                  ' - Data_Entrega:',produto[4], '- Ativo',produto[5])
    else:
        print('Nenhum projeto cadastrado!')
    cursor.close()
    conexao.close()
######################################      PRONTO     ####################################################
#id,nome,descrição,data_cadastro,data_entrega,ativo


def buscar_por_id(id):
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = "SELECT * FROM projetos WHERE id='%d'" % id
    cursor.execute(sql)
    produto = cursor.fetchone()
    if produto:
        print('Id: ', produto[0], ' - nome: ', produto[1],
              ' - Descrição: ', produto[2], ' - Data_Cadastro: ', produto[3],
              ' - Data_Entrega: ', produto[4], '- Ativo', produto[5])

        return True
    else:
        print('Nenhum projeto cadastrado!')
        return False
    cursor.close()
    conexao.close()

######################################      PRONTO      ##################################################

def buscar_por_descricao(descricao):
    descricao = nome+'%'
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = "SELECT * FROM projetos WHERE nome LIKE '%s'" % descricao
    cursor.execute(sql)
    ProjetoAB = cursor.fetchall()
    if ProjetoAB:
        for produto in ProjetoAB:
            print('Id: ', produto[0], ' - nome: ', produto[1],
                  ' - Descrição: ', produto[2], ' - Data_Cadastro: ', produto[3],
                  ' - Data_Entrega: ', produto[4], '- Ativo',produto[5])
        return True
    else:
        print('Não tá cadastrado!')
        return False
    cursor.close()
    conexao.close()

######################################      PRONTO      ##################################################

def cadastrar(nome,descricao,data_cadastro,data_entrega,ativo):
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = ("INSERT INTO projetos(nome,descricao,data_cadastro,data_entrega,ativo) VALUES ('%s','%s','%s','%s','%s')"
          % (nome,descricao,data_cadastro,data_entrega,ativo))
    cursor.execute(sql)
    if cursor.rowcount == 1:
        conexao.commit()
        print(nome,' cadastrado')
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
#id,nome,descrição,data_cadastro,data_entrega,ativo

def alterar_nome(id):
    if buscar_por_id(id):
        nome = input('Informe o novo Nome: ')
        conexao = sqlite3.connect(BD)
        cursor = conexao.cursor()
        sql = "UPDATE projetos SET nome='%s' WHERE id='%d' " % (nome,id)
        cursor.execute(sql)
        if cursor.rowcount == 1:
            conexao.commit()
            print('Nome alterado!')
        else:
            conexao.rollback()
            print('Não foi possível alterar Nome')


def alterar_descricao(id):
    if buscar_por_id(id):
        descricao = input('Informe a descrição do produto')
        conexao = sqlite3.connect(BD)
        cursor = conexao.cursor()
        sql = "UPDATE produto SET descricao='%s' WHERE id='%d' " % (
            descricao, id)
        cursor.execute(sql)
        if cursor.rowcount == 1:
            conexao.commit()
            print('Produto alterado!')
        else:
            conexao.rollback()
            print('Não foi possível alterar produto')





print('###########################################')
print('###############    MENU      ##############')
print('###########################################')
print('##        1 - Cadastrar Membros          ##')
print('##        2 - Listar Todos               ##')
print('##        3 - Buscar por ID              ##')
print('##        4 - Buscar por descrição       ##')
print('##        5 - Alterar Descrição          ##')
print('##        6 - Alterar Nome               ##')
print('##        7 - Excluir                    ##')
print('##        99 - SAIR                      ##')
print('###########################################')

op = 0
while True:
    op = int(input('Informe uma opção: '))

    if op == 1:
        nome = input('Informe o nome: ')
        descricao = input('Informe o descrição: ')
        data_cad = input('Informe a Data de cadastro: ')
        data_ent = input('Informe a Data de entrega: ')
        ativo = input('Informe o ativo do projeto: ')



        lista_data = data_cad.split('-')
        lista_data.reverse()
        data_cadastro = '-'.join(lista_data)
        lista_data = data_ent.split('-')
        lista_data.reverse()
        data_entrega = '-'.join(lista_data)

        cadastrar(nome,descricao,data_cadastro,data_entrega,ativo)

    elif op == 2:
        print('Esses são os contatos listados')
        listar_todos()
    elif op == 3:
        id = int(input('Informe o ID para poder buscar: '))
        buscar_por_id(id)
    elif op == 4:
        nome = input('Informe o nome do contato para poder buscar: ')
        buscar_por_descricao(nome)
    elif op == 5:
        id = int(input('Informe o ID do contato para alterar a descrição: '))
        alterar_descricao(id)
    elif op == 6:
        id = input('Informe o ID do contato para alterar o nome: ')
        alterar_nome(id)
    elif op == 7:
        id = int(input('Informe o ID do contato para que possa ser excluida: '))
        excluir(id)

    elif op == 99:
        print("SAINDO...")
        break


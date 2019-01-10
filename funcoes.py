import sqlite3

BD = 'ProjetoAB.db'


######################################       DEMANDAS       ####################################################
def listar_todos_d(id_projeto):
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = "select * from demandas where id_projeto = '%s'" % id_projeto
    cursor.execute(sql)
    demandas = cursor.fetchall()
    if demandas:
        #print(membros)
        for demandas in demandas:
            print('Id:',demandas[0],'- Id_projeto:',demandas[1],'- Descrição:', demandas[2],'- Data de entrega:',demandas[3],
                  '- Ativo:',demandas[4])
    else:
        print('Nenhum membro cadastrado neste projeto!')
    cursor.close
    conexao.close




def buscar_por_id_d(id):
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



def buscar_por_descricao_d(descricao):
    descricao = descricao + '%'
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = "SELECT * FROM demandas WHERE descricao LIKE '%s'" % descricao
    cursor.execute(sql)
    ProjetoAB = cursor.fetchall()
    if ProjetoAB:
        for produto in ProjetoAB:
            print('Id: ', produto[0], ' - id_projeto: ', produto[1],
                  ' - Descrição: ', produto[2], ' - Data_entrega: ', produto[3], '- Ativa', produto[4])
        return True
    else:
        print('Não tá cadastrado!')
        return False
    cursor.close()
    conexao.close()


def cadastrar_d(id_projeto, descricao, data_entrega):
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = "INSERT INTO demandas(id_projeto,descricao,data_entrega) VALUES ('%d','%s','%s')" % (
    id_projeto, descricao, data_entrega)
    cursor.execute(sql)
    if cursor.rowcount == 1:
        conexao.commit()
        print(descricao, ' cadastrado')
    else:
        conexao.rollback()
        print('Não foi possível cadastrar')
    cursor.close()
    conexao.close()




def excluir_d(id):
    if buscar_por_id_d(id):
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




def alterar_descricao_d(id):
    if buscar_por_id_d(id):
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



def alterar_id_projeto_d(id_projeto):
    if buscar_por_id_d(id):
        id_projeto = input('Informe o novo Id do projeto: ')
        conexao = sqlite3.connect(BD)
        cursor = conexao.cursor()
        sql = "UPDATE projetos SET nome='%s' WHERE id='%d'" % (id_projeto, id)
        cursor.execute(sql)
        if cursor.rowcount == 1:
            conexao.commit()
            print('Nome alterado!')
        else:
            conexao.rollback()
            print('Não foi possível alterar Nome')




def ativar_d(id):
    if buscar_por_id_d(id):
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




def inativar_d(id):
    if buscar_por_id_d(id):
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


######################################       MEMBROS       ####################################################
def listar_todos_m(id_projeto):
    """lista todos os membros"""
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = "select * from membros where id_projeto = '%s'" % id_projeto
    cursor.execute(sql)
    membros = cursor.fetchall()
    if membros:
        #print(membros)
        for membros in membros:
            print('Id: ', membros[0], ' - nome: ', membros[1],' - email: ', membros[2], ' - gerente: ', membros[3],
               ' - dev: ', membros[4], '- fullstack', membros[5], '- backend', membros[6],'- frontend', membros[7])
    else:
        print('Nenhum membro cadastrado neste projeto!')
    cursor.close
    conexao.close



def buscar_por_id_m(id):
    """busca pelo id do projeto"""
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = "SELECT * FROM membros WHERE id='%d'" % id
    cursor.execute(sql)
    produto = cursor.fetchone()
    if produto:
        print('Id: ', produto[0], ' - nome: ', produto[1],
              ' - email: ', produto[2], ' - gerente: ', produto[3],
              ' - dev: ', produto[4], '- fullstack', produto[5], '- backend', produto[6],
              ' - frontend', produto[7], '- id_projeto', produto[8])

        return True
    else:
        print('Nenhum membro cadastrado!')
        return False
    cursor.close()
    conexao.close()


def buscar_por_nome_m(nome):
    descricao = nome + '%'
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
        print('Não tem membro cadastrado!')
        return False
    cursor.close()
    conexao.close()


def cadastrar_m(nome, email, gerente, dev,fullstack, backend, frontend, id_projeto):
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = "INSERT INTO membros (nome,email,gerente,dev,backend,frontend,fullstack,id_projeto) VALUES \
          ('%s','%s','%s','%s','%s','%s','%s','%d')" % (
    nome, email, gerente, dev, fullstack, backend, frontend, id_projeto)

    cursor.execute(sql)
    if cursor.rowcount == 1:
        conexao.commit()
        print(nome, ' cadastrado')
    else:
        conexao.rollback()
        print('Não foi possível cadastrar')
    cursor.close()
    conexao.close()


def excluir_m(id):
    if buscar_por_id_m(id):
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


def alterar_nome_m(id):
    if buscar_por_id_m(id):
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


def alterar_email_m(id):
    if buscar_por_id_m(id):
        email = input('Informe o novo Email: ')
        conexao = sqlite3.connect(BD)
        cursor = conexao.cursor()
        sql = "UPDATE membros SET email='%s' WHERE id='%d' " % (email, id)
        cursor.execute(sql)
        if cursor.rowcount == 1:
            conexao.commit()
            print('Email alterado!')
        else:
            conexao.rollback()
            print('Não foi possível alterar Email')






######################################       PROJETOS       ####################################################
def listar_todos_p():
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = "SELECT * FROM projetos "
    cursor.execute(sql)
    ProjetoAB = cursor.fetchall()
    if ProjetoAB.__len__() > 0:
        for produto in ProjetoAB:
            print('Id:', produto[0], ' - nome:', produto[1],
                  ' - Descrição:', produto[2], ' - Data_Cadastro:', produto[3],
                  ' - Data_Entrega:', produto[4], '- Ativo', produto[5])
    else:
        print('Nenhum produto cadastrado!')
    cursor.close()
    conexao.close()




def buscar_por_id_p(id):
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
        print('Nenhum produto cadastrado!')
        return False
    cursor.close()
    conexao.close()




def buscar_por_descricao_p(nome):
    descricao = nome + '%'
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = "SELECT * FROM projetos WHERE nome LIKE '%s'" % descricao
    cursor.execute(sql)
    ProjetoAB = cursor.fetchall()
    if ProjetoAB:
        for produto in ProjetoAB:
            print('Id: ', produto[0], ' - nome: ', produto[1],
                  ' - Descrição: ', produto[2], ' - Data_Cadastro: ', produto[3],
                  ' - Data_Entrega: ', produto[4], '- Ativo', produto[5])
        return True
    else:
        print('Não tá cadastrado!')
        return False
    cursor.close()
    conexao.close()



def cadastrar_p(nome, descricao, data_cadastro, data_entrega):
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = ("INSERT INTO projetos(nome,descricao,data_cadastro,data_entrega) VALUES ('%s','%s','%s','%s')"
           % (nome, descricao, data_cadastro, data_entrega))
    cursor.execute(sql)
    if cursor.rowcount == 1:
        conexao.commit()
        print(nome, ' cadastrado')
    else:
        conexao.rollback()
        print('Não foi possível cadastrar')
    cursor.close()
    conexao.close()



def excluir_p(id):
    if buscar_por_id_p(id):
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



def alterar_descricao_p(id):
    if buscar_por_id_p(id):
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
            print('Não foi possível alterar a descrição do projeto')



def alterar_nome_p(id):
    if buscar_por_id_p(id):
        nome = input('Informe o novo Nome: ')
        conexao = sqlite3.connect(BD)
        cursor = conexao.cursor()
        sql = "UPDATE projetos SET nome='%s' WHERE id='%d' " % (nome, id)
        cursor.execute(sql)
        if cursor.rowcount == 1:
            conexao.commit()
            print('Nome alterado!')
        else:
            conexao.rollback()
            print('Não foi possível alterar descricao')


def ativar_p(id):
    if buscar_por_id_p(id):
        conexao = sqlite3.connect(BD)
        cursor = conexao.cursor()
        sql = "UPDATE projetos SET ativo == 'True' WHERE id =='%d'" % id
        cursor.execute(sql)
        if cursor.rowcount == 1:
            conexao.commit()
            print('Produto ativado!')
        else:
            conexao.rollback()
            print('Não foi possível ativar produto')


def inativar_p(id):
    if buscar_por_id_p(id):
        conexao = sqlite3.connect(BD)
        cursor = conexao.cursor()
        sql = "UPDATE produto SET ativo='False' WHERE id='%d'" % id
        cursor.execute(sql)
        if cursor.rowcount == 1:
            conexao.commit()
            print('Produto inativado!')
        else:
            conexao.rollback()
            print('Não foi possível inativar produto')


import sqlite3
from model.Usuario import Usuario

class UsuarioDAO():

    def inserir(self,usuario):
        conn = sqlite3.connect("ifteractdb")
        cursor = conn.cursor()

        query =  """
            insert into tb_Usuario(nome,email,senha,data_nasc,profissao,genero,cidade,estado,pais) values(?, ?, ?, ?, ?, ?, ?, ?, ?)
            """
        values = (usuario.nome,usuario.email,usuario.senha,usuario.dataNasc,usuario.profissao,usuario.genero, usuario.cidade, usuario.estado, usuario.pais)

        cursor.execute(query,values)
        conn.commit()

        cursor.close()
        conn.close()

    def listar(self):
        conn = sqlite3.connect("ifteractdb")
        cursor = conn.cursor()

        usuarios = []

        query = """
            Select * From tb_Usuario;
            """
        values = ()

        resultado = cursor.execute(query,values)

        for linha in resultado:
            nome = linha[1]
            email = linha[2]
            nascimento = linha[4]
            profissao = linha[5]
            genero = linha[6]
            senha = linha[3]
            usuario = Usuario(nome, email, senha, nascimento, profissao, genero)
            usuarios.append(usuario)

        cursor.close()
        conn.close()


        return usuarios

    def atualizar(self,usuario, idUsuario):
        conn = sqlite3.connect("ifteractdb")
        cursor = conn.cursor()

        usuario.nome = str(input("Digite o novo Nome:"))
        usuario.email = str(input("Digite o novo Email:"))
        usuario.senha = str(input("Digite a nova Senha:"))

        cursor.execute("""
            update tb_Usuario
            set nome = ?,email = ?,profissao = ?, senha=?
            where id = ?
            """, (usuario.nome,usuario.email,usuario.profissao,usuario.senha, idUsuario))
        conn.commit()

        cursor.close()
        conn.close()

    def deletar(self,idUsuario):
        conn = sqlite3.connect("ifteractdb")
        cursor = conn.cursor()

        cursor.execute("""
             delete from tb_Usuario
             where id = ?
             """,(idUsuario,))

        conn.commit()
        cursor.close()
        conn.close()



    def logar(self):
        #Criacao do cursor da conexao(Banco de Dados - SQLite3)

        conn = sqlite3.connect("ifteractdb")
        cursor = conn.cursor()

        #Pedindo Dados
        email = input("Digite o seu email:\n ")
        senha = input("Digite sua senha:\n ")

        #Comando Sql de Consulta(Select
        cursor.execute("""
            Select * From tb_Usuario where email = ? and senha = ?;
        """, (email, senha))
        user = cursor.fetchone()
        print(user)

        cursor.close()
        conn.close()


        return user



    def verificarEmail(self,emailUser):
        conn = sqlite3.connect("ifteractdb")
        cursor = conn.cursor()

        cursor.execute("""
            Select email from tb_Usuario
        """)

        emails = cursor.fetchall()

        for email in emails:
            if (emailUser == email[0]):
                return False
        cursor.close()
        conn.close()

        return True







































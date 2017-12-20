import sqlite3
import datetime
from model.Comentario import Comentario

class ComentarioDAO():

    def insert(self):
        conn = sqlite3.connect("ifteractdb")
        cursor = conn.cursor()

        mensagem = str(input("Digite o seu comentario:"))

        dataHora = datetime.datetime.now()
        curtidas = 0

        cursor.execute("""
            Insert Into tb_Comentario(mensagem,data_hora,curtidas)
            values(?,?,?)
        """,(mensagem,dataHora,curtidas))

        conn.commit()
        cursor.close()
        conn.close()

    def listar(self):

        conn = sqlite3.connect("ifteractdb")
        cursor = conn.cursor()

        comentarios = []

        query = """
            Select * From tb_Comentario;
            """
        values = ()

        resultado = cursor.execute(query,values)

        for linha in resultado:
            mensagem = linha[1]
            dataHora = linha[2]
            curtidas = linha[3]
            comentario = Comentario(mensagem,dataHora,curtidas)
            comentarios.append(comentario)

        cursor.close()
        conn.close()


        return comentarios

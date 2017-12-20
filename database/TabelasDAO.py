import sqlite3


def criarTabelas():

    try:

        conn = sqlite3.connect("ifteractdb")
        cursor = conn.cursor()



        cursor.execute("""
            CREATE TABLE tb_Usuario (
                id INTEGER NOT NULL PRIMARY KEY autoincrement,
                nome VARCHAR(70) NOT NULL,
                email VARCHAR(50) NOT NULL UNIQUE,
                senha VARCHAR(30) NOT NULL,
                data_nasc DATE,
                profissao VARCHAR(50),
                genero VARCHAR(10),
                cidade varchar(50),
                estado varchar(50),
                pais varchar(50)
             );

        """)

        cursor.execute("""
             Create Table tb_Comentario (
                id INTEGER NOT NULL PRIMARY KEY autoincrement,
                mensagem varchar(100),
                data_hora datetime,
                curtidas integer
                );

        """)

        cursor.close()
        conn.close()

    except Exception as err:
        print(err)


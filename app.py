import datetime
from database.TabelasDAO import criarTabelas
from database.UsuarioDAO import UsuarioDAO
from database.ComentarioDAO import ComentarioDAO
from model.Comentario import Comentario
from model.Usuario import Usuario


def cadastrar():
    usuarioDAO = UsuarioDAO()

    nome = str(input("Digite o Nome do Usuario:"))
    email = str(input("Digite o Email do Usuario:"))

    if(usuarioDAO.verificarEmail(email) != True):
        print("Este Email já esta sendo utilizado")
        return ""

    while(True):
        try:
            print("Data de Nascimento. OBS: A DATA DE NASCIMENTO DEVE SER DIGITADA UTILIZANDO NUMEROS")

            dia = int(input("Dia:"))
            mes = int(input("Mes"))
            ano = int(input("Ano:"))

            dataNasc = datetime.date(ano,mes,dia)
            break
        except:
            print("\n Data Invalida\n")


    profissao = str(input("Digite sua Profissao:"))

    genero = str(input("Digite o seu Genero:"))

    senha = str(input("Digite a sua senha:"))

    usuario = Usuario(nome,email,senha,dataNasc,profissao,genero)

    usuarioDAO = UsuarioDAO()
    usuarioDAO.inserir(usuario)
    return usuario



def exibirMenuInicial():
    print("""
        1-Cadastrar
        2-Listar Usuario
        3-Logar
        0-Sair

    """)

def exibirMenuHome():

    print("""
        1-Atualizar
        2-Listar Usuarios
        3-Deletar Conta
        4-Fazer Comentario
        5-Informacoes do Usuario
        6-Ver Comentarios
        0-Sair

    """)





def main():
    criarTabelas()
    comentarioDAO = ComentarioDAO()
    usuarioDAO = UsuarioDAO()

    sair = False
    logar = False
    usuario = None
    idUsuario = -1
    while (sair == False):
        exibirMenuInicial()
        try:
            escolha = int(input("Digite a opcao desejada:"))

            #INICIO
            if(escolha == 1):
                cadastrar()

            elif(escolha == 2):
                users = usuarioDAO.listar()
                for user in users:
                        print(user)
            elif(escolha == 3):
                usuario = usuarioDAO.logar()
                if(usuario != None):
                    logar = True
                    idUsuario = usuario[0]
                    nome = usuario[1]
                    email = usuario[2]
                    nascimento = usuario[4]
                    profissao = usuario[5]
                    genero = usuario[6]
                    senha = usuario[3]
                    usuario = Usuario(nome,email,senha,nascimento,profissao,genero)


            elif(escolha == 0):
                sair = True


            #HOME
            while(logar == True):
                exibirMenuHome()
                try:
                    escolha = int(input("Digite a opcao desejada:"))


                    if(escolha == 1):
                        usuarioDAO.atualizar(usuario, idUsuario)

                    elif(escolha == 2):
                        users = usuarioDAO.listar()
                        for user in users:
                            print(user)

                    elif(escolha == 3):
                        usuarioDAO.deletar(idUsuario)
                        logar = False

                    elif(escolha == 4):
                        comentarioDAO.insert()

                    elif(escolha == 5):
                        print("""
                            Nome: %s
                            Email: %s
                            Data de Nascimento: %s
                            Genero: %s
                            Profissao: %s
                            Cidade: %s
                            Estado: %s
                            Pais: %s
                            Senha: %s

                        """ % (usuario.nome,usuario.email, usuario.dataNasc, usuario.genero, usuario.profissao, usuario.cidade, usuario.estado, usuario.pais, usuario.senha))

                    elif(escolha == 6):
                        comentarios = comentarioDAO.listar()
                        for comentario in comentarios:
                            print(comentario)

                    elif(escolha == 0):
                        logar = False
                except:
                    print("Valor Invalido!!Digite um Numero")
        except:
            print("Valor Invalido!!Digite um Numero")

if __name__ == '__main__':
    main()
































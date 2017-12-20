

class Usuario():

    def __init__(self, nome, email, senha, dataNasc, profissao, genero, cidade = "Campina Grande", estado = "Paraíba", pais = "Brasil", amigos = []):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.dataNasc = dataNasc
        self.profissao = profissao
        self.genero = genero
        self.cidade = cidade
        self.estado = estado
        self.pais = pais

    def __str__(self):
        return "Nome: " + self.nome + " Email: " + self.email


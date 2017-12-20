import datetime

class Comentario():

    def __init__(self, mensagem, dataHora = datetime.datetime.now(), curtidas = 0):
        self.mensagem = mensagem
        self.dataHora = dataHora
        self.curtidas = curtidas

    def __str__(self):
        return "mensagem: " + self.mensagem + " data e hora" + str(self.dataHora)

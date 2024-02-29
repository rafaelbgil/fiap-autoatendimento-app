
class Cliente():
    nome: str = None
    email: str = None
    uuid: str = None
    cpf: str = None

    def __init__(self, nome, email, uuid, cpf):
        self.nome = nome
        self.email = email
        self.uuid = uuid.__str__().replace('-', '')
        self.cpf = cpf

    def setUuid(self, uuid):
        self.uuid = uuid.__str__().replace('-', '')



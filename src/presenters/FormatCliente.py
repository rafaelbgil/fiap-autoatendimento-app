from src.entities.Cliente import Cliente


class FormatCliente:
    """
    Classe com métodos para formatar objetos do tipo Cliente
    """
    @staticmethod
    def fromClienteToDict(cliente: Cliente) -> dict:
        return ({
            'uuid': cliente.uuid,
            'nome': cliente.nome,
            'email': cliente.email,
            'cpf' : cliente.cpf
        })
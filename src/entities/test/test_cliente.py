import unittest
from src.entities.Cliente import Cliente
from src.entities.ClienteFactory import ClienteFactory

class TestClienteFactory(unittest.TestCase):
    def test_client_from_dict(self):
        dicionario_cliente = {
            'nome' : 'Joao Silva',
            'email' : 'joao.silva@teste.com',
            'cpf' : '01234567890'
        }

        cliente = ClienteFactory.fromDict(dicionario_cliente=dicionario_cliente)
        self.assertIsInstance(cliente, Cliente)
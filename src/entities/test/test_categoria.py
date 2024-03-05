import unittest
from src.entities.CategoriaFactory import CategoriaFactory
from src.entities.CategoriaFactory import _validar_nome_categoria


class TestCategoriaFactory(unittest.TestCase):
    def test_categoria_from_dict(self):
        dicionario_categoria = {
            'nome': 'refrigerante',
            'id': 1
        }
        categoria = CategoriaFactory.fromDict(dicionario_categoria=dicionario_categoria)
        self.assertEqual(categoria.nome, 'refrigerante')

    def test_categoria_nome_null(self):
        dicionario_categoria = {
            'id': 1
        }

        self.assertRaises(AttributeError, CategoriaFactory.fromDict, [dicionario_categoria])

    def test_categoria_nome_caracteres_excedidos(self):
        nome = 'abcdferffffffffdkdlfkdlkfldkfldklfdklfdklsdkfldsklfskdlfkdslfkdslkfdslkfdslkfdslkfdslkfldskflsdk'

        self.assertRaises(AttributeError, _validar_nome_categoria, nome)

    def test_categoria_nome_sem_caracteres(self):
        nome = ''

        self.assertRaises(AttributeError, _validar_nome_categoria, nome)



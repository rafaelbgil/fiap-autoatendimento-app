import unittest
from src.entities.CategoriaFactory import CategoriaFactory

class TestCategoriaFactory(unittest.TestCase):
    def test_categoria_from_dict(self):
        dicionario_categoria = {
            'nome' : 'refrigerante',
            'id' : 1
        }
        categoria = CategoriaFactory.fromDict(dicionario_categoria=dicionario_categoria)
        self.assertEqual(categoria.nome,'refrigerante')




#if __name__ == '__main__':
#    unittest.main()
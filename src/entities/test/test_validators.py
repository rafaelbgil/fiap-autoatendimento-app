import unittest

from src.entities.validators import _validarEmail, _validarUuid, _validarNome

class TestValidators(unittest.TestCase):
    def test_validator_validar_email(self):
        self.assertEqual(_validarEmail('joao@silva.com'), 'joao@silva.com')

    def test_validator_validar_email_attribute_error(self):
        self.assertRaises(AttributeError, _validarEmail, None)
        self.assertRaises(AttributeError, _validarEmail,'teste.com')
        self.assertRaises(AttributeError, _validarEmail, 'teste@com')
        self.assertRaises(AttributeError, _validarEmail, 'joço@teste.com')

    def test_validator_uuid(self):
        self.assertTrue(_validarUuid('550e8400-e29b-41d4-a716-446655440000'))
        self.assertTrue(_validarUuid('550e8400e29b41d4a716446655440000'))

    def test_validator_uuid_none(self):
        self.assertIsNone(_validarUuid(None))

    def test_validator_uuid_attribute_error(self):
        self.assertRaises(AttributeError, _validarUuid,'ass')
        self.assertRaises(AttributeError, _validarUuid, '~~~')

    def test_validator_nome_attribute_error(self):
        self.assertRaises(AttributeError,_validarNome, '')

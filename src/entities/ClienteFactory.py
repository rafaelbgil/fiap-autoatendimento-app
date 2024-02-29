from .Cliente import Cliente
from .TypeCpf import Cpf
from .validators import _validarEmail, _validarNome, _validarUuid


class ClienteFactory:
    def fromDict(dicionario_cliente: dict, validar_campos=True) -> Cliente:
        nome = None
        email = None
        uuid = None
        cpf = None

        if 'email' in dicionario_cliente:
            if validar_campos:
                email = _validarEmail(dicionario_cliente['email'])
            else:
                email = dicionario_cliente['email']

        if 'uuid' in dicionario_cliente:
            if validar_campos:
                uuid = _validarUuid(dicionario_cliente['uuid'])
            else:
                uuid = dicionario_cliente['uuid'].__str__().replace('-', '')

        if 'nome' in dicionario_cliente:
            if validar_campos:
                nome = _validarNome(dicionario_cliente['nome'])
            else:
                nome = dicionario_cliente['nome']

        if 'cpf' in dicionario_cliente:
            cpf = Cpf(cpf=dicionario_cliente['cpf']).cpf

        return Cliente(nome=nome, email=email, uuid=uuid, cpf=cpf)

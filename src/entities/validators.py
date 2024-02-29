from uuid import UUID
import re


def _validarEmail(email: str) -> str:
    if email == None:
        raise Exception('E-mail não preenchido.')

    if not re.search('@', email):
        raise Exception('E-mail inválido.')

    if not re.search('\.', email):
        raise Exception('E-mail inválido.')

    if not re.match('^[a-z0-9][\w.-]*@[a-z0-9][\w.-]*[a-z0-9]$', email):
        raise Exception('E-mail inválido.')
    return email


def _validarUuid(uuid: str | UUID) -> str:
    if not uuid:
        return None

    if type(uuid) == UUID:
        uuid = uuid.__str__()

    uuid_formatado = uuid.replace('-', '').lower()

    if re.match('[^a-z0-9]', uuid_formatado):
        raise Exception('O UUID informado é inválido')

    if len(uuid_formatado) != 32:
        raise Exception('O UUID informado é inválido')
    return uuid_formatado


def _validarNome(nome: str) -> str:
    if nome and len(nome) > 1:
        return nome
    raise Exception('O nome deve ser informado')

from __future__ import annotations

from uuid import UUID
import re


def _validarEmail(email: str) -> str:

    if email == None:
        raise AttributeError('E-mail não preenchido.')

    email = email.lower()

    if not re.search('@', email):
        raise AttributeError('E-mail inválido.')

    if not re.search('\.', email):
        raise AttributeError('E-mail inválido.')

    if not re.match('^[a-z0-9._-]*@[a-z0-9._-]*[a-z0-9]$', email):
        raise AttributeError('E-mail inválido.')

    return email


def _validarUuid(uuid: str | UUID) -> str | None:
    if not uuid or not str:
        return None

    if  isinstance(uuid, UUID):
        uuid = uuid.__str__()

    uuid_formatado = uuid.replace('-', '').lower()

    if re.match('[^a-z0-9]', uuid_formatado):
        raise AttributeError('O UUID informado é inválido')

    if len(uuid_formatado) != 32:
        raise AttributeError('O UUID informado é inválido')
    return uuid_formatado


def _validarNome(nome: str) -> str:
    if nome and len(nome) > 1:
        return nome
    raise AttributeError('O nome deve ser informado')

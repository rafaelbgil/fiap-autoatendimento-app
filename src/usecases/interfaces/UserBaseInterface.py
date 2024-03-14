from abc import ABC, abstractmethod
from src.entities.Cliente import Cliente


class UserBase(ABC):

    @staticmethod
    def criar_usuario(cliente: Cliente, senha: str) -> dict:
        pass

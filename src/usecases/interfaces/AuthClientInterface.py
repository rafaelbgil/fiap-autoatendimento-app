from abc import ABC, abstractmethod
class AuthClientInterface(ABC):
    @staticmethod
    def autenticar(cpf: str, senha: str) ->dict:
        pass
from abc import ABC, abstractmethod
from requests import Request


class MeioPagamentoInterface(ABC):
    @abstractmethod
    @staticmethod
    def criarCobranca(descricao: str, valor: float, url_webhook: str) -> Request:
        pass

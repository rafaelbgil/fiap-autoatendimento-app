from abc import ABC, abstractmethod
from src.entities.Pedido import Pedido

class PedidoRepositoryInterface(ABC):
    @staticmethod
    def getPedido(id: int) -> Pedido:
        pass
    
    @staticmethod
    def listPedido() -> list[Pedido]:
        pass
    
    @staticmethod
    def addPedido(pedido: Pedido) -> Pedido:
        pass

    @staticmethod
    def addPedidoFromDict( dicionario_pedido: dict) -> dict:
        pass

    @staticmethod
    def updateStatus(pedido: Pedido, status: str) -> Pedido:
        pass

from abc import ABC, abstractmethod
from src.entities.Cliente import Cliente

class ClienteDaoInterface(ABC):
    @abstractmethod
    def getCliente(uuid: str) -> Cliente:
        pass
    
    @abstractmethod
    def deleteCliente(uuid: str) -> bool:
        pass

    @abstractmethod
    def listCliente() -> list[Cliente]:
        pass

    @abstractmethod
    def addCliente(cliente: Cliente):
        pass
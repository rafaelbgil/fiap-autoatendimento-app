from abc import ABC, abstractmethod
from src.entities.Categoria import Categoria

class CategoriaDaoInterface(ABC):
    @staticmethod
    def getCategoria(id: int) -> Categoria:
        pass

    @staticmethod
    def deleteCategoria(id: int) -> bool:
        pass

    @staticmethod
    def addCategoria(categoria: Categoria):
        pass

    @staticmethod 
    def listCategoria() -> list[Categoria]:
        pass
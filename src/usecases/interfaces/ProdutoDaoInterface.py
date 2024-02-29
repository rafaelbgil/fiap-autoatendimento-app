from abc import ABC, abstractmethod
from src.entities.Produto import Produto

class ProdutoDaoInterface(ABC):
    @abstractmethod
    def getProduto(id : int) -> Produto:
        pass

    @abstractmethod
    def listProdutoByCategoria(categoria_nome: str) -> list[Produto]:
        pass
    
    @abstractmethod
    def listProduto()-> list[Produto]:
        pass

    @abstractmethod
    def deleteProduto(id: int) -> bool:
        pass

    @abstractmethod
    def addProduto(produto: Produto) -> Produto:
        pass

    @abstractmethod
    def updateProduto(produto: Produto, id: str) -> Produto:
        pass
    

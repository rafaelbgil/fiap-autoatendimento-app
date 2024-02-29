from src.entities.Produto import Produto
from .interfaces.ProdutoDaoInterface import ProdutoDaoInterface

class UseCaseProduto:
    @staticmethod
    def obterListaProduto(repository_produto: ProdutoDaoInterface) -> list[Produto]:
        return repository_produto.listProduto()
    
    @staticmethod
    def obterListaProdutoPorCategoria(repository_produto: ProdutoDaoInterface, categoria_nome: str) -> list[Produto]:
        return repository_produto.listProdutoByCategoria(categoria_nome=categoria_nome)
    
    @staticmethod
    def obterProduto(repository_produto: ProdutoDaoInterface, id: int) -> Produto:
        return repository_produto.getProduto(id=id)
    
    @staticmethod
    def criarProduto(repository_produto: ProdutoDaoInterface, produto: Produto) -> Produto:
        return repository_produto.addProduto(produto=produto)
    
    @staticmethod
    def atualizarProduto(repository_produto: ProdutoDaoInterface, produto: Produto, id: int) -> Produto:
        return repository_produto.updateProduto(produto=produto, id=id)

    @staticmethod
    def removerProduto(repository_produto: ProdutoDaoInterface, id: int) -> bool:
        return repository_produto.deleteProduto(id=id)
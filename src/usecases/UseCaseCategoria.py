from src.entities.Categoria import Categoria
from src.usecases.interfaces.CategoriaDaoInterface import CategoriaDaoInterface

class UseCaseCategoria:
    def obterListaCategoria(repository_categoria: CategoriaDaoInterface) -> list[Categoria]:
        return repository_categoria.listCategoria()
    
    def obterCategoria(repository_categoria: CategoriaDaoInterface, id: int) -> Categoria:
        return repository_categoria.getCategoria(id=id)
    
    def criarCategoria(repository_categoria: CategoriaDaoInterface, categoria: Categoria) -> Categoria:
        return repository_categoria.addCategoria(categoria=categoria)
    
    def removerCategoria(repository_categoria: CategoriaDaoInterface, id: int) -> bool:
        return repository_categoria.deleteCategoria(id=id)
   
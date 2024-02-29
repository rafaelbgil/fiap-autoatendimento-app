from src.entities.Categoria import Categoria


class FormatCategoria:
    """
    Classe com métodos para formatar objetos do tipo Categoria
    """
    def fromCategoriaToDict(categoria: Categoria):
        return ({
            'id' : categoria.id,
            'nome' : categoria.nome
        })
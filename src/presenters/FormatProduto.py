from src.entities.Produto import Produto


class FormatProduto:
    """
    Classe com métodos para formatar objetos do tipo Produto
    """
    @staticmethod
    def fromProdutoToDict(produto: Produto) -> dict:
        return({
            'id' : produto.id,
            'nome' : produto.nome,
            'preco' : produto.preco,
            'id_categoria' : produto.id_categoria,
            'descricao' : produto.descricao,
            'imagem_url' : produto.imagem_url,
        })
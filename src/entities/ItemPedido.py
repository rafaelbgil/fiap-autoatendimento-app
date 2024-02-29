from src.entities.Produto import Produto

class ItemPedido(Produto):
    quantidade : int 

    def __init__(self, nome, descricao, preco, id=None, id_categoria=None, imagem_url=None, quantidade=None):
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.id = id
        self.id_categoria = id_categoria
        self.imagem_url = imagem_url
        self.quantidade = quantidade
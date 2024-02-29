class Produto:
    id : int | None
    id_categoria: int | None
    nome: str | None
    descricao: str | None
    preco: float | None
    imagem_url: str | None

    def __init__(self, nome, descricao, preco, id=None, id_categoria=None, imagem_url=None):
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.id = id
        self.id_categoria = id_categoria
        self.imagem_url = imagem_url


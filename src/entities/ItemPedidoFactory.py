from .Produto import Produto
from .ItemPedido import ItemPedido


class ItemPedidoFactory:
    def createByProduto(produto: Produto, quantidade=1) -> ItemPedido:
        return ItemPedido(nome=produto.nome,
                          descricao=produto.descricao,
                          preco=produto.preco,
                          id_categoria=produto.id_categoria,
                          imagem_url=produto.imagem_url,
                          quantidade=quantidade
                          )

    def fromDict(dicionario_item) -> ItemPedido:
        quantidade = 1
        nome = None
        descricao = None
        preco = 0
        id_categoria = None
        imagem_url = None

        if 'quantidade' in dicionario_item:
            quantidade = dicionario_item['quantidade']

        nome = dicionario_item['nome']

        if 'descricao' in dicionario_item:
            descricao = dicionario_item['descricao']

        preco = dicionario_item['preco']

        if 'id_categoria' in dicionario_item:
            id_categoria = dicionario_item['id_categoria']

        if 'imagem_url' in dicionario_item:
            imagem_url = dicionario_item['imagem_url']

        return ItemPedido(nome=nome,
                          descricao=descricao,
                          preco=preco,
                          id_categoria=id_categoria,
                          imagem_url=imagem_url,
                          quantidade=quantidade)

from .Produto import Produto


def _validar_nome_produto(nome: str, update=False) -> str:
    if len(nome) > 40:
        raise Exception(
            'Excedido o tamanho máximo de caracteres para o nome(max: 40).')
    if len(nome) == 0 and update == False:
        raise Exception('Nome do produto definido como vazio.')
    return nome


def _validar_descricao_produto(descricao: str) -> str:
    if not descricao:
        return descricao
    if len(descricao) > 1024:
        raise Exception(
            'Excedido o tamanho máximo de caracteres para a descricao(max: 1024).')
    return descricao


def _validar_imagem_url_produto(imagem_url: str) -> str:
    if not imagem_url:
        return imagem_url
    if len(imagem_url) > 1024:
        raise Exception(
            'Excedido o tamanho máximo de caracteres para a descricao(max: 1024).')
    return imagem_url


def _validar_preco_produto(preco: int | float | str, update=False) -> float | None:
    if type(preco) == int or type(preco) == float:
        return float(preco)

    if (preco == None or preco == 'None' or len(preco) == 0) and (update == True):
        return None

    if type(preco) == str:
        try:
            return float(preco.replace(',', '.'))
        except:
            raise Exception(
                'Formato de preco inválido, utilize somente inteiros ou float.')

    raise Exception(
        'Formato de preco inválido, utilize somente inteiros ou float.')


class ProdutoFactory:
    @staticmethod
    def fromDict(dicionario_produto, update=False) -> Produto:
        id = None
        nome = None
        descricao = None
        id_categoria = None
        preco = None
        imagem_url = None


        nome = _validar_nome_produto(nome=dicionario_produto['nome'], update=update)
        descricao = _validar_descricao_produto(
            descricao=dicionario_produto['descricao'])
        preco = _validar_preco_produto(preco=dicionario_produto['preco'], update=update)
        imagem_url = _validar_imagem_url_produto(
            imagem_url=dicionario_produto['imagem_url'])
        
        if 'id' in dicionario_produto:
            id = dicionario_produto['id']

        if 'id_categoria' in dicionario_produto:
            id_categoria = dicionario_produto['id_categoria']
        
        return Produto(id=id, nome=nome, descricao=descricao, preco=preco, imagem_url=imagem_url, id_categoria=id_categoria)

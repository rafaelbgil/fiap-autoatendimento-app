from .Categoria import Categoria

def _validar_nome_categoria(nome: str) -> str:
    if len(nome) > 40:
        raise AttributeError('Excedido o tamanho máximo de caracteres para categoria(max: 40).')
    if len(nome) == 0:
        raise AttributeError('Nome da categoria definido como vazio.')
    return nome


class CategoriaFactory:
    def fromDict(dicionario_categoria: dict, validar_campos=True) -> Categoria: 
        nome = None
        id = None
        if 'nome' in dicionario_categoria:
            nome = _validar_nome_categoria(dicionario_categoria['nome'])
        else:
            raise AttributeError('Nome da categoria não preenchido.')
        
        if 'id' in dicionario_categoria:
            id = dicionario_categoria['id']
        
        return Categoria(nome=nome, id=id)
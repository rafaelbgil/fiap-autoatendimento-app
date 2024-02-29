from abc import ABC
from .Cobranca import Cobranca

class Pedido(ABC):
    id: int | None
    status: str
    cpf: str | None
    numero: int | None
    lista_itens: list | None
    valor: float

    def __init__(self, numero: int, valor: float, status: str = 'aguardando_pagamento', lista_itens: list | None = None, cpf: str | None = None, id: int = None, cobranca: Cobranca = None):
        self.numero = numero
        self.status = status
        self.cpf = cpf
        self.lista_itens = lista_itens
        self.valor = float(valor)
        self.id = id
        self.cobranca = cobranca

    def atualizarStatusPedido(self, status: str):
        if self.status == 'cancelado' or self.status == 'finalizado':
            raise Exception('Pedidos com status cancelado ou finalizado nao podem ser alterados')

        if (self.status == 'aguardando_pagamento'):
            if (status == 'recebido' or status == 'cancelado'):
                self.status = status
                return
            else:
                raise Exception('Pedidos com status aguardando_pagamento so podem ser alterados para cancelado ou recebido')           
        
        if (self.status == 'recebido'):
            if (status == 'preparando' or status == 'cancelado'):
                self.status = status
                return
            else:
                raise Exception('Pedidos com status recebido so podem ser alterados para cancelado ou preparando')     
        
        if (self.status == 'preparando'):
            if (status == 'pronto' or status == 'cancelado'):
                self.status = status
                return
            else:
                raise Exception('Pedidos com status preparando so podem ser alterados para cancelado ou pronto')
    
        if (self.status == 'pronto'):
            if (status == 'finalizado' or status == 'cancelado'):
                self.status = status
                return
            else:
                raise Exception('Pedidos com status preparando so podem ser alterados para cancelado ou pronto')
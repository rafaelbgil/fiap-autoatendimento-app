from src.entities.Pedido import Pedido
from .interfaces.PedidoRepositoryInterface import PedidoRepositoryInterface

class UseCasePedido:
    def obterListaPedidos(repositorio_pedido: PedidoRepositoryInterface) -> list[Pedido]:
        lista_pedidos = repositorio_pedido.listPedido()
        lista_pedidos_prontos = []
        lista_pedidos_preparando = []
        lista_pedidos_entregues = []
        lista_pedidos_aguardando_pagamento = []
        
        for pedido_selecionado in lista_pedidos:
            if pedido_selecionado.status == 'preparando':
                lista_pedidos_preparando.append(pedido_selecionado)
            if pedido_selecionado.status == 'pronto':
                lista_pedidos_prontos.append(pedido_selecionado)
            if pedido_selecionado.status == 'recebido':
                lista_pedidos_entregues.append(pedido_selecionado)
            if pedido_selecionado.status == 'aguardando_pagamento':
                lista_pedidos_aguardando_pagamento.append(pedido_selecionado)

        lista_pedidos_ordenada = lista_pedidos_prontos + lista_pedidos_preparando + lista_pedidos_entregues + lista_pedidos_aguardando_pagamento

        return lista_pedidos_ordenada

    
    def criarPedidoFromDict(repositorio_pedido: PedidoRepositoryInterface, dicionario_pedido: dict) -> Pedido:
        return repositorio_pedido.addPedidoFromDict(dicionario_pedido=dicionario_pedido)
    
    def obterPedido(repositorio_pedido: PedidoRepositoryInterface, id: str) -> Pedido:
        return repositorio_pedido.getPedido(id=id)
    
    def atualizarStatusPagtoViaWebhook(repositorio_pedido: PedidoRepositoryInterface, pedido: Pedido, status_pagto: str):
        return repositorio_pedido.updateStatusPgto(pedido=pedido, status_pgto=status_pagto)
    
    def atualizarStatusPedido(repositorio_pedido: PedidoRepositoryInterface, pedido: Pedido, status: str)-> Pedido:
        return repositorio_pedido.updateStatus(pedido=pedido, status=status)
from os import environ
from uuid import uuid4

from src.usecases.interfaces.PedidoRepositoryInterface import PedidoRepositoryInterface
from src.entities.Pedido import Pedido
from src.entities.PedidoFactory import PedidoFactory
from src.entities.ItemPedidoFactory import ItemPedidoFactory
from src.entities.Cobranca import Cobranca
from src.entities.CobrancaFactory import CobrancaFactory
from src.entities.CategoriaFactory import CategoriaFactory
from src.entities.TypeCpf import Cpf

from src.external.mercadopago.cobranca import CobrancaMercadoPago

from api.models import Pedido as PedidoModel
from api.models import ItemPedido as ItemPedidoModel
from api.models import Produto as ProdutoModel
from api.models import Cobranca as CobrancaModel


class PedidoRepositoryOrm(PedidoRepositoryInterface):
    @staticmethod
    def listPedido() -> list[Pedido]:
        pedidos_queryset = PedidoModel.objects.all()
        lista_pedidos = []

        if not pedidos_queryset:
            return lista_pedidos

        for pedido_orm in pedidos_queryset:
            pedido = PedidoRepositoryOrm.pedidoOrmToPedido(pedido_orm)
            lista_pedidos.append(pedido)

        return lista_pedidos

    @staticmethod
    def pedidoOrmToPedido(pedido_orm: PedidoModel) -> Pedido:
        lista_itens_orm = pedido_orm.itempedido_set.all()
        lista_itens = []
        for item in lista_itens_orm:
            lista_itens.append(item.__dict__)

        pedido_dict = pedido_orm.__dict__
        pedido_dict['numero'] = pedido_orm.id
        pedido_dict['lista_itens'] = lista_itens

        pedido = PedidoFactory.fromDict(
            dicionario_pedido=pedido_dict)

        if pedido_orm.cobranca_set.exists():
            cobranca_orm = pedido_orm.cobranca_set.get()
            cobranca = CobrancaFactory.createCobranca(
                valor=cobranca_orm.valor, fornecedor_meio_pagto=cobranca_orm.fornecedor_meio_pagto, codigo=cobranca_orm.codigo, status=cobranca_orm.status, pix_codigo=cobranca_orm.pix_codigo)

            pedido.cobranca = cobranca       

        return pedido

    @staticmethod
    def addPedidoFromDict(dicionario_pedido: dict) -> Pedido:
        if not 'lista_itens' in dicionario_pedido:
            raise Exception('A lista de itens não pode ser vazia.')

        lista_itens = []
        valor_total = 0
        cpf = None
        # Verifica se produto consultado pelo id existe, cria um objeto ItemPedido e o adiciona a lista_itens
        for item in dicionario_pedido['lista_itens']:
            try:
                produto_model = ProdutoModel.objects.get(id=item['id'])
            except:
                raise Exception(
                    'Nao foi possivel localizar o item com id %s.' % (item['id']))
            item_pedido = ItemPedidoFactory.fromDict(
                dicionario_item=produto_model.__dict__)
            item_pedido.quantidade = item['quantidade']
            valor_total = valor_total + \
                (item['quantidade'] * item_pedido.preco)
            lista_itens.append(item_pedido)

        if 'cpf' in dicionario_pedido:
            cpf = Cpf(cpf=dicionario_pedido['cpf'])

        pedido_orm = PedidoModel()
        pedido_orm.cpf = cpf
        pedido_orm.valor = valor_total
        try:
            pedido_orm.save()
        except:
            raise (Exception)

        for item_da_lista in lista_itens:
            item_pedido_orm = ItemPedidoModel()
            item_pedido_orm.pedido = pedido_orm
            item_pedido_orm.nome = item_da_lista.nome
            item_pedido_orm.descricacao = item_da_lista.descricao
            item_pedido_orm.quantidade = item_da_lista.quantidade
            item_pedido_orm.imagem_url = item_da_lista.imagem_url
            item_pedido_orm.preco = item_da_lista.preco
            try:
                item_pedido_orm.save()
            except:
                raise (Exception)
        
        if environ.get('MERCADOPAGO_EMAIL') and environ.get('MERCADOPAGO_TOKEN'):
            print('passou pelo mercadopago')
            try:
                uuid_cobranca = uuid4()
                WEBHOOK_DOMAIN = 'https://teste.com.br'
                if environ.get('WEBHOOK_DOMAIN'):
                    WEBHOOK_DOMAIN = environ.get('WEBHOOK_DOMAIN')

                URL_WEBHOOK = WEBHOOK_DOMAIN + '/api/pedido/mercadopago/' + uuid_cobranca.__str__()    
                
                cobranca_mercadopago = CobrancaMercadoPago(token=environ.get('MERCADOPAGO_TOKEN'))
                retorno_cobranca_mercadopago = cobranca_mercadopago.criarCobranca('pagamento lanchonete fiap', valor=pedido_orm.valor, url_webhook=URL_WEBHOOK)
                
                cobranca_orm = CobrancaModel()
                cobranca_orm.pix_codigo = retorno_cobranca_mercadopago.json()['point_of_interaction']['transaction_data']['qr_code']
                print('webhook url: %s' % retorno_cobranca_mercadopago.json()['notification_url'])
                print('Pagamento url: %s' % retorno_cobranca_mercadopago.json()['point_of_interaction']['transaction_data']['ticket_url'])
                cobranca_orm.pedido = pedido_orm
                cobranca_orm.valor = pedido_orm.valor
                cobranca_orm.save()
            except Exception as erro:
                raise(erro)
        return PedidoRepositoryOrm.pedidoOrmToPedido(pedido_orm=pedido_orm)

    @staticmethod
    def getPedido(id: int) -> Pedido:
        try:
            pedido_orm = PedidoModel.objects.get(id=id)
        except:
            raise Exception(
                'Nao foi possivel localizar o pedido com id %s.' % (id))

        return PedidoRepositoryOrm.pedidoOrmToPedido(pedido_orm=pedido_orm)

    @staticmethod
    def updateStatus(pedido: Pedido, status: str) -> Pedido:
        pedido.atualizarStatusPedido(status=status)
        pedido_orm = PedidoModel.objects.get(id=pedido.numero)
        pedido_orm.status = pedido.status
        pedido_orm.save()
        return pedido

    @staticmethod
    def updateStatusByWebhook(uuid_cobranca: str, dicionario_cobranca: dict) -> bool:
        try:
            cobranca_orm = CobrancaModel.objects.get(codigo=uuid_cobranca)
            if dicionario_cobranca['status'] == 'pending':
                return True
            if dicionario_cobranca['status'] == 'approved' or dicionario_cobranca['status'] == 'authorized' :
                cobranca_orm.pedido.status = 'recebido'
                cobranca_orm.status = 'recebido'
                cobranca_orm.pedido.save()
                cobranca_orm.save()
                return True
            if dicionario_cobranca['status'] == 'cancelled' or dicionario_cobranca['status'] == 'rejected':
                cobranca_orm.pedido.status = 'cancelado'
                cobranca_orm.status = 'cancelado'
                cobranca_orm.pedido.save()
                cobranca_orm.save()
                return True
        except:
            raise Exception('Cobranca invalida %s.' % (uuid_cobranca))
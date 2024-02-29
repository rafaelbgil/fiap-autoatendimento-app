from src.db.django_orm.PedidoRepositoryOrm import PedidoRepositoryOrm
from src.usecases.UseCasePedido import UseCasePedido
from src.presenters.FormatPedido import FormatPedido

from api.serializers import PedidoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiExample


class PedidoView(APIView):
    """
    Api para gerencimento de pedidos
    """
    serializer_class = PedidoSerializer

    @extend_schema(summary='Obtém lista de pedidos', examples=[
        OpenApiExample('Exemplo de pedido', value=[{
            "id": 1,
            "cpf": "12345678901",
            "valor": 10.90,
            "status": "aguardando_pagamento",
            "lista_itens": [
                {
                    "id": 1,
                    "nome": "Hamburguer",
                    "preco": 10.90,
                    "imagem_url": 'hamburger.png',
                    "quantidade": 1
                }
            ]
        }], response_only=True)
    ])
    def get(self, request, format=None):
        """
        Obtém lista de **pedidos**
        """
        pedidos = UseCasePedido.obterListaPedidos(PedidoRepositoryOrm)
        pedido_dict = FormatPedido.fromListPedidoToDict(pedidos)
        return Response(data=pedido_dict, status=status.HTTP_200_OK)

    @extend_schema(summary='Adiciona novo pedido', examples=[
        OpenApiExample('Exemplo de pedido', value={
            "cpf": "12345678901",
            "lista_itens": [
                {
                    "id": 1,
                    "quantidade": 1
                }
            ]
        }, request_only=True),
        OpenApiExample('Exemplo de pedido', value=
            [
                {"id": 1,
                "cpf": "12345678901",
                "valor": 10.90,
                "status": "aguardando_pagamento",
                "lista_produtos": [
                    {
                        "id": 1,
                        "nome": "Hamburguer",
                        "preco": 10.90,
                        "imagem_url": 'hamburger.png',
                        "quantidade": 1
                    },
                ]}
            ],
        response_only=True)
    ])
    def post(self, request, format=None):
        """
        Adiciona novo **pedido**
        """
        pedido = PedidoRepositoryOrm.addPedidoFromDict(
            dicionario_pedido=request.data)
        pedido_dict = FormatPedido.fromPedidoToDict(pedido)
        return Response(data=pedido_dict, status=status.HTTP_201_CREATED)

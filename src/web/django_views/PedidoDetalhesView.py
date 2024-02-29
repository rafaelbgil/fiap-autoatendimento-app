from src.db.django_orm.PedidoRepositoryOrm import PedidoRepositoryOrm
from src.usecases.UseCasePedido import UseCasePedido
from src.presenters.FormatPedido import FormatPedido

from api.serializers import PedidoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiExample


class PedidoDetalhesView(APIView):
    """
    Api para obter informacoes do pedido selecionado
    """
    serializer_class = PedidoSerializer

    @extend_schema(summary='Obtém dados de pedido selecionado',
                   examples=[
                       OpenApiExample('Exemplo de uso',
                                      value={
                                          "numero": 1,
                                          "status": "pronto",
                                          "cpf": "12345678901",
                                          "valor": 403.3,
                                          "id": 1,
                                          "lista_itens": [
                                              {
                                                  "nome": "x-bacon",
                                                  "descricao": None,
                                                  "preco": 10.9,
                                                  "id": None,
                                                  "imagem_url": "http://127.0.0.1/images/nao_implementado",
                                                  "quantidade": 37
                                              }
                                          ]
                                      },
                                      request_only=False,
                                      response_only=True,
                                      )
                   ])
    def get(self, request, id, format=None):
        """
        Obtém informacao de **pedido** selecionado
        """
        try:
            pedido = UseCasePedido.obterPedido(
                repositorio_pedido=PedidoRepositoryOrm, id=id)
        except Exception as erro:
            return Response(data={'status': 'erro', 'descricao': erro.__str__()}, status=status.HTTP_404_NOT_FOUND)

        pedido_dict = FormatPedido.fromPedidoToDict(pedido)
        return Response(data=pedido_dict, status=status.HTTP_200_OK)

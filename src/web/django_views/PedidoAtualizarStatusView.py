from src.db.django_orm.PedidoRepositoryOrm import PedidoRepositoryOrm
from src.usecases.UseCasePedido import UseCasePedido
from src.presenters.FormatPedido import FormatPedido

from api.serializers import PedidoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiExample


class PedidoAtualizarStatusView(APIView):
    """
    Api para atualizar status do pedido
    """
    serializer_class = PedidoSerializer

    @extend_schema(summary='Atualiza status do pedido', examples=[
        OpenApiExample('Definir como pagamento recebido e pedido na fila',
                       value={
                           "status": 'recebido',
                       },
                       request_only=True,
                       response_only=False,
                       ),
        OpenApiExample('Definir como pedido em preparacao',
                       value={
                           "status": 'preparando',
                       },
                       request_only=True,
                       response_only=False,
                       ),
         OpenApiExample('Definir o pedido como pronto para o cliente retirar',
                       value={
                           "status": 'pronto',
                       },
                       request_only=True,
                       response_only=False,
                       ),
        OpenApiExample('Definir o pedido como finalizado após o cliente retirar',
                       value={
                           "status": 'finalizado',
                       },
                       request_only=True,
                       response_only=False,
                       ),
        OpenApiExample('Definir o pedido como cancelado',
                       value={
                           "status": 'cancelado',
                       },
                       request_only=True,
                       response_only=False,
                       ),
    ])
    def post(self, request, id, format=None):
        """
       Atualiza status do **pedido**
        """
        try:
            pedido = UseCasePedido.obterPedido(repositorio_pedido=PedidoRepositoryOrm, id=id)
            pedido_atualizado = UseCasePedido.atualizarStatusPedido(repositorio_pedido=PedidoRepositoryOrm, pedido=pedido, status=request.data['status'])
        except Exception as erro:
            return Response(data={'status': 'erro', 'descricao': erro.__str__()}, status=status.HTTP_400_BAD_REQUEST)

        
        return Response(FormatPedido.fromPedidoToDict(pedido_atualizado), status=status.HTTP_200_OK)

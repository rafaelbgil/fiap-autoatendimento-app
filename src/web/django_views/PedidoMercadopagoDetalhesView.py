from src.db.django_orm.PedidoRepositoryOrm import PedidoRepositoryOrm
from src.usecases.UseCasePedido import UseCasePedido
from src.presenters.FormatPedido import FormatPedido

from api.serializers import PedidoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiExample

class PedidoMercadopagoDetalhesView(APIView):
    """
    Url para webhook do mercadopago
    """
    def post(self, request, uuid, format=None):
        """
        Url webhook mercadopago
        """
        try:
            if PedidoRepositoryOrm.updateStatusByWebhook(uuid_cobranca=uuid, dicionario_cobranca=request.data):
                return Response(status=status.HTTP_200_OK)        
        except Exception as erro:
            return Response(data={'status': 'erro', 'descricao': erro.__str__()}, status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_200_OK)        

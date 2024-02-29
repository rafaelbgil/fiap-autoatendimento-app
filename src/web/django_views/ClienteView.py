from src.entities.ClienteFactory import ClienteFactory
from src.db.django_orm.ClienteDaoOrm import ClienteDaoOrm
from src.usecases.UseCaseCliente import UseCaseCliente

from src.presenters.FormatCliente import FormatCliente

from rest_framework.views import APIView
from api.serializers import ClienteSerializer
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiExample


class ClienteView(APIView):
    """
    Api para gerenciamento de clientes
    """
    serializer_class = ClienteSerializer

    @extend_schema(responses=ClienteSerializer(many=True), summary='Obtém lista de clientes cadastrados', examples=[
        OpenApiExample('Exemplo de uso',
                       value={"uuid": "aaacdd85853f4fbd920616f4bd2d8e66",
                              "nome": 'Joao Silva', "email": 'joao@teste.com', "cpf": "12345678901"},
                       request_only=False,
                       response_only=True,
                       )
    ])
    def get(self, request, format=None):
        """
        Retorna uma lista de **clientes**.
        """
        clientes = UseCaseCliente.obterListacliente(
            repository_cliente=ClienteDaoOrm)
        serializer = ClienteSerializer(data=clientes, many=True)
        serializer.is_valid()
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(summary='Adiciona novo cliente', examples=[
        OpenApiExample('Exemplo de uso',
                       value={"uuid": "lbbcdd85853f4fbd920616f4bd2d8e66",
                              "nome": 'Luis Silva', "email": 'luis@teste.com', "cpf": "98345678901"},
                       request_only=False,
                       response_only=True,
                       ),
        OpenApiExample('Exemplo de uso',
                       value={"nome": 'Luis Silva',
                              "email": 'luis@teste.com', "cpf": "98345678901"},
                       request_only=True,
                       response_only=False,
                       )
    ])
    def post(self, request, format=None):
        """
        Api para **cadastrar** cliente
        """
        try:
            cliente = UseCaseCliente.criarCliente(
                repository_cliente=ClienteDaoOrm, cliente=ClienteFactory.fromDict(request.data))
        except Exception as erro:
            return Response(data={'status': 'erro', 'detalhes': erro.__str__()}, status=status.HTTP_400_BAD_REQUEST)
        return Response(FormatCliente.fromClienteToDict(cliente=cliente), status=status.HTTP_201_CREATED)

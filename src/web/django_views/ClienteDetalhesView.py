from src.db.django_orm.ClienteDaoOrm import ClienteDaoOrm
from src.usecases.UseCaseCliente import UseCaseCliente

from rest_framework.views import APIView
from api.serializers import ClienteSerializer
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiExample


class ClienteDetalhesView(APIView):
    serializer_class = ClienteSerializer
    @extend_schema(summary='Obtém dados de cliente selecionado',
                   examples=[
                       OpenApiExample('Exemplo de uso',
                       value={"uuid": "aaacdd85853f4fbd920616f4bd2d8e66",
                              "nome": 'Joao Silva', "email": 'joao@teste.com', "cpf" : "12345678901"},
                       request_only=False,
                       response_only=True,
                       )
                   ])
    def get(self, request, uuid: str, format=None):
        """
        Api para visualizar dados de usuario selecionado
        """
        try:
            cliente = UseCaseCliente.obterCliente(repository_cliente=ClienteDaoOrm, uuid=uuid)
        except Exception as erro:
            return Response(data={'status': 'erro', 'detalhes': erro.__str__()}, status=status.HTTP_400_BAD_REQUEST)
       
        if not cliente:
            return Response(data={'status': 'erro', 'detalhes': "Cliente não encontrado, verifique o uuid"}, status=status.HTTP_404_NOT_FOUND)
       
        serializer = ClienteSerializer(instance=cliente)
        return Response(data=serializer.data)

    @extend_schema(summary='Remove cliente selecionado')
    def delete(self, request, uuid: str, format=None):
        """
        Api para remover cliente selecionado
        """
        try:
            UseCaseCliente.removerCliente(repository_cliente=ClienteDaoOrm, uuid=uuid)
        except:
            return Response(data={'status': 'erro', 'descricao': 'Não foi possível localizar o usuário informado pelo UUID para realizar a remoção.'}, status=status.HTTP_404_NOT_FOUND)

        return Response(data={'status': 'sucesso', 'descricao': 'Usuário removido com sucesso'})

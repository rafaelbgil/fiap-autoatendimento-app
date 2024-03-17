from rest_framework.views import APIView
from api.serializers import CriarUsuarioSerializer
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiExample

from src.entities.ClienteFactory import ClienteFactory
from src.usecases.UseCaseCriarUsuario import UseCaseCriarUsuario
from src.external.cognito.create_user_by_lambda import CreateUserCognitoByLambda


class CriarUsuarioView(APIView):
    serializer_class = CriarUsuarioSerializer

    def post(self, request, format=None):
        """
        Api para **autenticar** cliente e receber token
        """
        try:

            cliente = ClienteFactory.fromDict(dicionario_cliente={
                "nome": request.data['nome'],
                "email": request.data['email'],
                "cpf": request.data['cpf']
            })

            criar_usuario = UseCaseCriarUsuario.criar(cliente=cliente, senha=request.data['senha'],
                                                      user_base=CreateUserCognitoByLambda)

        except Exception as erro:
            return Response(data={'status': 'erro', 'detalhes': erro.__str__()}, status=status.HTTP_400_BAD_REQUEST)
        return Response(criar_usuario, status=status.HTTP_200_OK)

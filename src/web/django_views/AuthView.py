from rest_framework.views import APIView
from api.serializers import AuthSerializer
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiExample

from src.usecases.UseCaseAutenticarCliente import UseCaseAutenticarCliente
from src.external.cognito.cognito_auth import CognitoAuth


class AuthView(APIView):
    serializer_class = AuthSerializer

    def post(self, request, format=None):
        """
        Api para **autenticar** cliente e receber token
        """
        try:
            autenticacao = UseCaseAutenticarCliente.autenticar_cliente(cpf=request.data['usuario'],
                                                                       senha=request.data['senha'], auth=CognitoAuth)
        except Exception as erro:
            return Response(data={'status': 'erro', 'detalhes': erro.__str__()}, status=status.HTTP_400_BAD_REQUEST)
        return Response(autenticacao, status=status.HTTP_200_OK)

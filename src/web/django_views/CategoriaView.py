from src.entities.CategoriaFactory import CategoriaFactory
from src.db.django_orm.CategoriaDaoOrm import CategoriaDaoOrm
from src.usecases.UseCaseCategoria import UseCaseCategoria

from src.presenters.FormatCategoria import FormatCategoria

from rest_framework.views import APIView
from api.serializers import CategoriaSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema, OpenApiExample


class CategoriaView(APIView):
    serializer_class = CategoriaSerializer

    @extend_schema(responses=CategoriaSerializer(many=True), summary='Obtém lista de categorias', examples=[
        OpenApiExample('Exemplo de uso',
                       value={"id": 1,
                              "nome": "doces"},
                       request_only=False,
                       response_only=True,
                       )
    ])
    def get(self, request, format=None):
        """
        Api para listar categorias
        """
        categorias = UseCaseCategoria.obterListaCategoria(
            repository_categoria=CategoriaDaoOrm)
        serializer = CategoriaSerializer(data=categorias, many=True)
        serializer.is_valid()
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @extend_schema(summary='Adiciona nova categoria', examples=[
        OpenApiExample('Exemplo de uso',
                       value={"id": 1,
                              "nome": "salgados"},
                       request_only=False,
                       response_only=True,
                       ),

        OpenApiExample('Exemplo de uso',
                       value={"nome": "salgados"},
                       request_only=True,
                       response_only=False,
                       )
    ])
    def post(self, request, format=None):
        """
        Api para adicionar categoria
        """
        try:
            categoria = UseCaseCategoria.criarCategoria(
                repository_categoria=CategoriaDaoOrm, categoria=CategoriaFactory.fromDict(request.data))
        except Exception as erro:
            return Response({'status': 'erro', 'detalhes': erro.__str__()}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = CategoriaSerializer(data=FormatCategoria.fromCategoriaToDict(categoria=categoria))
        try:
            if not serializer.is_valid():
                return Response({'status': 'erro', 'detalhes': serializer._errors}, status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as erro:
            return Response({'status': 'erro', 'detalhes': 'Não foi possível cadastrar a nova categoria.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(data=FormatCategoria.fromCategoriaToDict(categoria=categoria), status=status.HTTP_201_CREATED)

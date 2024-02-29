from src.db.django_orm.ProdutoDaoOrm import ProdutoDaoOrm
from src.usecases.useCaseProduto import UseCaseProduto

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample, OpenApiTypes, OpenApiResponse
from api.serializers import ProdutoSerializer


class ProdutoByCategoriaView(APIView):
    """
    Api para obter lista de produtos por Categoria
    """
    @extend_schema(summary='Obtém dados de produto selecionado' , responses={
        200: OpenApiResponse(description='Lista de Produtos'),
        404: OpenApiResponse(description='Categoria não encontrada')
    })
    def get(self, request, categoria: str, format=None):
        """
        Api para obter lista de produtos por categoria
        """
        try:
            lista_produtos = UseCaseProduto.obterListaProdutoPorCategoria(repository_produto=ProdutoDaoOrm, categoria_nome=categoria)
        except Exception as erro:
            return Response(data={'status': 'erro', 'descricao': erro.__str__()}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProdutoSerializer(instance=lista_produtos, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
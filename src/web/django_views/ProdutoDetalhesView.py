from src.entities.ProdutoFactory import ProdutoFactory
from src.db.django_orm.ProdutoDaoOrm import ProdutoDaoOrm
from src.usecases.useCaseProduto import UseCaseProduto

from src.presenters.FormatProduto import FormatProduto

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample, OpenApiTypes, OpenApiResponse
from api.serializers import ProdutoSerializer


class ProdutoDetalhesView(APIView):
    """
    Api para gerenciamento de produto
    """
    serializer_class = ProdutoSerializer

    @extend_schema(summary='Obtém dados de produto selecionado', responses={
        200: OpenApiResponse(description='Json Response'),
        400: OpenApiResponse(description='Validation error')
    })
    def get(self, request, id: str, format=None):
        """
        Api para visualizar dados de produto selecionado
        """
        try:
            produto = UseCaseProduto.obterProduto(
                repository_produto=ProdutoDaoOrm, id=id)
        except Exception as erro:
            return Response(data={'status': 'erro', 'descricao': erro.__str__()}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProdutoSerializer(instance=produto)
        return Response(serializer.data)

    @extend_schema(summary='Atualiza produto selecionado')
    def put(self, request, id: str, format=None):
        """
        Api para atualizar produto selecionado
        """
        try:
            produto_atualizado = UseCaseProduto.atualizarProduto(
                repository_produto=ProdutoDaoOrm, produto=ProdutoFactory.fromDict(request.data, update=True), id=id)
        except Exception as erro:
            return Response(data={'status': 'erro', 'descricao': erro.__str__()})
        return Response(FormatProduto.fromProdutoToDict(produto_atualizado))

    @extend_schema(summary='Remove produto selecionado')
    def delete(self, request, id: str, format=None):
        """
        Api para remover produto selecionado
        """
        try:
            UseCaseProduto.removerProduto(repository_produto=ProdutoDaoOrm, id=id)
        except Exception as erro:
            return Response(data={'status': 'erro', 'descricao': erro.__str__()}, status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_200_OK)

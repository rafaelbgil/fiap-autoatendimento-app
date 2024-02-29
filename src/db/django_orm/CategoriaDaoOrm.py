from src.usecases.interfaces.CategoriaDaoInterface import CategoriaDaoInterface
from src.entities.Categoria import Categoria
from src.entities.CategoriaFactory import CategoriaFactory
from api.models import Categoria as CategoriaModel


class CategoriaDaoOrm(CategoriaDaoInterface):
    @staticmethod
    def getCategoria(id: str) -> Categoria:
        if not id.isnumeric():
            raise Exception(
                'Código de categoria inválido, favor informar um número.')
        try:
            categoria_queryset = CategoriaModel.objects.get(id=id)
        except:
            raise Exception('Categoria não encontrada.')

        return CategoriaFactory.fromDict(categoria_queryset.__dict__)

    @staticmethod
    def listCategoria() -> list[Categoria]:
        categorias_queryset = CategoriaModel.objects.all()
        categorias = []
        for categoria in categorias_queryset.iterator():
            categorias.append(CategoriaFactory.fromDict(
                dicionario_categoria=categoria.__dict__))

        return categorias

    @staticmethod
    def deleteCategoria(id: int):
        try:
            categoria_queryset = CategoriaModel.objects.get(id=id)
            categoria_queryset.delete()
        except:
            raise Exception(
                'Categoria não foi encontrada ou não pode ser removida. Verifique o código informado.')
        return True

    @staticmethod
    def addCategoria(categoria: Categoria) -> Categoria:
        categoria_orm = CategoriaModel()
        for atributo in categoria.__dict__.keys():
            if categoria.__dict__[atributo] and categoria.__dict__[atributo] != 'None':
                categoria_orm.__setattr__(
                    atributo, categoria.__dict__[atributo])
        try:
            categoria_orm.save()
        except Exception as error:
            raise Exception('Não foi possível adicionar a categoria. %s' % (error.__str__()))

        categoria.id = categoria_orm.id
        return categoria

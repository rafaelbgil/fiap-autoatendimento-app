from rest_framework import serializers
from .models import Cliente, Categoria, ItemPedido


class ClienteSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    uuid = serializers.UUIDField(read_only=True)
    nome = serializers.CharField(max_length=120)
    email = serializers.CharField(max_length=120)
    cpf = serializers.CharField(max_length=11, required=False)
   
    def create(self, validated_data):
        return Cliente.objects.create(**validated_data)
    

class CategoriaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nome = serializers.CharField(max_length=40)

    def create(self, validated_data):
        return Categoria.objects.create(**validated_data)
    
    
class ProdutoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nome = serializers.CharField(max_length=40)
    preco = serializers.FloatField()
    id_categoria = serializers.IntegerField(required=False)
    descricao = serializers.CharField(max_length=1024, required=False)
    imagem_url = serializers.CharField(max_length=1024, required=False)

class ItemPedidoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nome = serializers.CharField(max_length=40)
    preco = serializers.FloatField()
    id_categoria = serializers.IntegerField(required=False)
    descricao = serializers.CharField(max_length=1024, required=False)
    imagem_url = serializers.CharField(max_length=1024, required=False)
    quantidade = serializers.IntegerField(required=True)

class PedidoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    cpf = serializers.CharField(max_length=11, required=False)
    valor = serializers.FloatField()
    status = serializers.CharField(read_only=True)
    lista_itens = serializers.SerializerMethodField()
    
    

    def get_lista_itens(self, obj):
        lista_itens = obj.itempedido_set.all()
        serializer = ItemPedidoSerializer(lista_itens, many=True)
        return serializer.data
    
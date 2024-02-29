from django.contrib import admin

# Register your models here.
from api.models import Cliente, Pedido, Produto, Categoria, ItemPedido, Cobranca

admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(Produto)
admin.site.register(ItemPedido)
admin.site.register(Categoria)
admin.site.register(Cobranca)
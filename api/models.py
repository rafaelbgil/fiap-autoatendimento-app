from django.db import models
import uuid


# Create your models here.
class Cliente(models.Model):
    uuid = models.UUIDField(
        primary_key=False, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=120, verbose_name="Nome completo do cliente",
                            help_text="Informe o nome do cliente, evite o uso de caracteres especiais.", null=False)
    email = models.CharField(max_length=120, unique=True)
    cpf = models.CharField(max_length=11, null=True, unique=True)


class Categoria(models.Model):
    nome = models.CharField(max_length=40, blank=False, unique=True)


class Produto(models.Model):
    nome = models.CharField(max_length=40, null=False)
    descricao = models.CharField(max_length=1024, null=True)
    preco =  models.FloatField(null=False)
    imagem_url = models.CharField(max_length=1024, null=True)
    categoria = models.ForeignKey(to=Categoria ,on_delete=models.CASCADE, null=True)

class Pedido(models.Model):
    status_choice = [
        ('aguardando_pagamento' , 'aguardando_pagamento'),
        ('preparando' , 'preparando'),
        ('pronto' , 'pronto'),
        ('recebido' , 'recebido'),
        ('finalizado' , 'finalizado'),
        ('cancelado' , 'cancelado')
    ] 
    
    cpf = models.CharField(max_length=11, null=True, blank=True)
    nome = models.CharField(max_length=120, null=True, blank=True)
    email = models.CharField(max_length=120, null=True, blank=True)
    valor = models.FloatField(null=False)
    status = models.CharField(choices=status_choice, default='aguardando_pagamento', max_length=40)
    

    def __str__(self):
        return 'id %s valor: %s, cpf: %s' % (self.id, self.valor, self.cpf)

class ItemPedido(models.Model):
    nome = models.CharField(max_length=40, null=False)
    descricao = models.CharField(max_length=1024, null=True, blank=True)
    preco = models.FloatField(null=False)
    imagem_url = models.CharField(max_length=1024, null=True, blank=True)
    categoria = models.CharField(max_length=40, null=True, blank=True)
    quantidade = models.PositiveIntegerField(null=False)
    pedido = models.ForeignKey(to=Pedido, on_delete=models.CASCADE, null=False)

class Cobranca(models.Model):
    status_choice = [
        ('pendente' , 'pendente'),
        ('cancelado' , 'cancelado'),
        ('recebido' , 'recebido')
    ]
    codigo = models.UUIDField(default=uuid.uuid4)
    valor = models.FloatField(null=False)
    pedido = models.ForeignKey(to=Pedido, on_delete=models.CASCADE, null=False) 
    status = models.CharField(choices=status_choice, default='pendente', max_length=40)
    fornecedor_meio_pagto = models.CharField(default='mercadopago', max_length=40)
    pix_codigo = models.CharField(max_length=300, null=True, blank=True)
    
    def __str__(self):
        return 'pedido: %s status: %s valor: %s' % (self.pedido.id, self.status, self.valor)
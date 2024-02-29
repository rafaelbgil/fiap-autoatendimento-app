from api.models import Cliente as ClienteModel
from src.entities.Cliente import Cliente
from src.entities.ClienteFactory import ClienteFactory, _validarUuid
from src.usecases.interfaces.ClienteDaoInterface import ClienteDaoInterface



class ClienteDaoOrm(ClienteDaoInterface):
    @staticmethod
    def getCliente(uuid: str) -> Cliente:
        client_uuid_validado = _validarUuid(uuid=uuid)
        try:
            cliente = ClienteModel.objects.get(uuid=client_uuid_validado)
        except:
            raise Exception('Cliente não encontrado.')
        return ClienteFactory.fromDict(dicionario_cliente=cliente.__dict__, validar_campos=False)
    
    @staticmethod
    def listCliente() -> list[Cliente]:
        clientes_queryset = ClienteModel.objects.all()
        clientes = []
        for cliente in clientes_queryset.iterator():
            clientes.append(ClienteFactory.fromDict(
                dicionario_cliente=cliente.__dict__, validar_campos=False))
        return clientes

    @staticmethod
    def deleteCliente(uuid: str) -> bool:
        try:
            ClienteModel.objects.get(uuid=uuid).delete()
        except:
            raise Exception('Não foi possível remover o cliente informado, verifique se o uuid informado está correto.')
        return True
    
    @staticmethod
    def addCliente(cliente: Cliente):
        cliente_orm = ClienteModel()
        for atributo in cliente.__dict__.keys():
            if cliente.__dict__[atributo] and cliente.__dict__[atributo] != 'None':
                cliente_orm.__setattr__(atributo, cliente.__dict__[atributo])
        
        try:
            cliente_orm.save()
        except Exception as erro:
            if 'cpf' in erro.__str__() and 'UNIQUE' in erro.__str__():
                raise Exception('Não foi possível adicionar o cliente, o CPF já está em uso.')

            if 'email' in erro.__str__() and 'UNIQUE' in erro.__str__():
                raise Exception ('Não foi possível adicionar o cliente, o e-mail já está em uso.')
            raise Exception('Não foi possível cadastrar o cliente.')
        
        cliente.setUuid(cliente_orm.uuid)
        return cliente


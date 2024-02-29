from .interfaces.ClienteDaoInterface import ClienteDaoInterface
from src.entities.Cliente import Cliente

class UseCaseCliente:
    @staticmethod
    def obterListacliente(repository_cliente: ClienteDaoInterface) -> list[Cliente]:
        return repository_cliente.listCliente()
    
    @staticmethod
    def obterCliente(repository_cliente: ClienteDaoInterface, uuid: str) -> Cliente:
        return repository_cliente.getCliente(uuid=uuid)
    
    @staticmethod 
    def criarCliente(repository_cliente: ClienteDaoInterface, cliente: Cliente) -> Cliente:
        return repository_cliente.addCliente(cliente=cliente)
    
    @staticmethod
    def removerCliente(repository_cliente: ClienteDaoInterface, uuid: str) -> bool:
        return repository_cliente.deleteCliente(uuid=uuid)
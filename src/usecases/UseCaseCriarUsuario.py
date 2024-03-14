from src.entities.Cliente import Cliente
from src.usecases.interfaces.UserBaseInterface import UserBase
class UseCaseCriarUsuario:
    @staticmethod
    def criar(cliente: Cliente, senha: str, user_base: UserBase)-> dict:
        return user_base.criar_usuario(cliente=cliente, senha=senha)


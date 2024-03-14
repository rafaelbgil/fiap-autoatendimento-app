from src.usecases.interfaces.AuthClientInterface import AuthClientInterface
class UseCaseAutenticarCliente:
    @staticmethod
    def autenticar_cliente(cpf: str, senha: str, auth: AuthClientInterface) -> dict:
        return auth.autenticar(cpf=cpf, senha=senha)

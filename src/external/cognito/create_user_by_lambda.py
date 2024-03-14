import boto3
from botocore.config import Config
from src.entities.Cliente import Cliente


class CreateUserCognitoByLambda:
    def __init__(self):
        self.config = Config(retries={'max_attempts': 2})
        self.client = boto3.client('lambda', config=self.config)

    def criar_usuario_cognito(self, usuario: Cliente, senha: str):
        payload = {"nome": usuario.nome, "email": usuario.email, "senha" : senha, "cpf" : usuario.cpf}
        return self.client.invoke(
            FunctionName='criarUsuario',
            InvocationType='RequestResponse',
            LogType='Tail',
            Payload=payload.__str__()
        )

import boto3
from botocore.config import Config
from src.entities.Cliente import Cliente
from src.usecases.interfaces.UserBaseInterface import UserBase
import json

class CreateUserCognitoByLambda(UserBase):

    @staticmethod
    def criar_usuario(cliente: Cliente, senha: str):
        config = Config(retries={'max_attempts': 2})
        client_aws = boto3.client('lambda', config=config)
        payload = {"nome": cliente.nome, "email": cliente.email, "senha": senha, "cpf": cliente.cpf}
        return client_aws.invoke(
            FunctionName='criarUsuario',
            InvocationType='RequestResponse',
            LogType='Tail',
            Payload=json.dumps(payload)
        )

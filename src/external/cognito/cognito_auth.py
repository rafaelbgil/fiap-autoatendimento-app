import boto3
from os import environ
import hmac, hashlib, base64
from src.usecases.interfaces.AuthClientInterface import AuthClientInterface


class CognitoAuth(AuthClientInterface):
    @staticmethod
    def autenticar(cpf: str, senha: str) -> dict:
        aws_client = boto3.client('cognito-idp')
        client_id = environ.get('COGNITO_CLIENT_ID')
        message = bytes(cpf + client_id, 'utf-8')
        key = bytes(environ.get('COGNITO_CLIENT_SECRET'), 'utf-8')
        secret_hash = base64.b64encode(hmac.new(key, message, digestmod=hashlib.sha256).digest()).decode()
        return aws_client.initiate_auth(
            ClientId=client_id,
            AuthFlow='USER_PASSWORD_AUTH',
            AuthParameters={
                "USERNAME": cpf,
                "PASSWORD": senha,
                "SECRET_HASH": secret_hash
            }
        )

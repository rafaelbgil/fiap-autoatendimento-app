import boto3


class CognitoValidate:

    @staticmethod
    def get_aws_client():
        return boto3.client('cognito-idp')

    @staticmethod
    def validar_token(token: str):
        aws_client = CognitoValidate.get_aws_client()
        try:
            token_validado = aws_client.get_user(AccessToken=token)
        except:
            raise Exception('Token invalido')

        return token_validado

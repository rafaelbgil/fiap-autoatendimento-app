import boto3


class CognitoValidate:

    @staticmethod
    def get_aws_client():
        return boto3.client('cognito-idp')

    @staticmethod
    def validar_token(token: str):
        aws_client = CognitoValidate.get_aws_client()
        return aws_client.get_user(AccessToken=token)

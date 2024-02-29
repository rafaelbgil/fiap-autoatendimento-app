import datetime
import requests
from os import environ

class CobrancaMercadoPago:
    token: str

    def __init__(self, token):
        self.token = token

    def criarCobranca(self, descricao: str, valor: float, url_webhook: str):
        email_comprador = environ.get('MERCADOPAGO_EMAIL')
        
        data_vencimento = datetime.datetime.now() + datetime.timedelta(minutes=15)
        data_vencimento_mercadopago = str(data_vencimento.year) + '-' + str(data_vencimento.strftime('%m')) + '-' + \
            str(data_vencimento.strftime('%d')) + 'T' + \
            data_vencimento.time().__str__()[:8] + '.000-03:00'
        dados_cobranca = {
            "statement_descriptor": "Lanchonete Fiap",
            "notification_url": url_webhook,
            "date_of_expiration": data_vencimento_mercadopago,
            "transaction_amount": float(valor),
            "description": descricao,
            "payment_method_id": 'pix',
            "payer": {
                "email" : email_comprador,
            }
        }
        header = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer %s' % (self.token)
        }
        return requests.post('https://api.mercadopago.com/v1/payments', json=dados_cobranca, headers=header)

from .Cobranca import Cobranca
from .validators import _validarUuid


class CobrancaFactory:
    @staticmethod
    def createCobranca(valor: float, fornecedor_meio_pagto: str, codigo: str = None, status: str = 'pendente', pix_codigo: str = None) -> Cobranca:
        _validarUuid(uuid=codigo)
        return Cobranca(valor=valor, codigo=codigo, status=status, fornecedor_meio_pagto=fornecedor_meio_pagto, pix_codigo=pix_codigo)

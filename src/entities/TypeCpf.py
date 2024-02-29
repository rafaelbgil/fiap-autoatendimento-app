class Cpf:
    cpf: str | None

    def __init__(self, cpf: str):
        self.cpf = _validate_cpf(cpf)

    def getCpfFormatado(self) -> str:
        return '%s.%s.%s-%s' % (self.cpf[0:3], self.cpf[3:6], self.cpf[6:9], self.cpf[9:11])

    def __str__(self):
        return self.cpf


def _validate_cpf(cpf: str | Cpf) -> str | None:
    if type(cpf) == Cpf:
        return cpf.cpf
    
    if not cpf :
        return None

    if type(cpf) != str:
        raise Exception('Cpf precisa ser string.')

    # verifica tamanho do cpf
    numeros_cpf = cpf.replace('-', '').replace('.', '')
    if len(numeros_cpf) != 11:
        raise Exception('Quantidade de números do cpf inválida.')

    return str(numeros_cpf)



from models.enum.uf import UnidadeFederativa

class Endereco:
    def __init__(self, logradouro: str, numero: str, complemento: str, cep: str, cidade: str, uf: UnidadeFederativa) -> None:
        self.logradouro = self._verificar_logradouro(logradouro)
        self.numero = self._verificar_numero(numero)
        self.complemento = self._verificar_complemento(complemento)
        self.cep = self._verificar_cep(cep)
        self.cidade = self._verificar_cidade(cidade)
        self.uf = uf

    def _verificar_logradouro(self, valor):
        self._verificar_logradouro_tipo_invalido(valor)

        self.logradouro = valor
        return self.logradouro
    
    def _verificar_numero(self,valor):
        self._verificar_numero_tipo_invalido(valor)

        self.numero = valor
        return self.numero

    def _verificar_complemento(self,valor):
        self._verificar_complemento_tipo_invalido(valor)

        self.complemento = valor
        return self.complemento

    def _verificar_cep(self,valor):
        self._verificar_cep_tipo_invalido(valor)

        self.cep = valor
        return self.cep
    
    def _verificar_cidade(self,valor):
        self._verificar_cidade_tipo_invalido(valor)

        self.cidade = valor
        return self.cidade
    
    def _verificar_logradouro_tipo_invalido(self,valor):
        if not isinstance(valor, str):
            raise TypeError("O logradouro deve se manter ortograficamente válido.")
 
    def _verificar_numero_tipo_invalido(self,valor):
        if not isinstance(valor, str):
            raise TypeError("O número deve se manter como ortograficamente válido.")

    def _verificar_complemento_tipo_invalido(self,valor):
        if not isinstance(valor, str):
            raise TypeError("O complemento deve se manter como ortograficamente válido.")

    def _verificar_cep_tipo_invalido(self,valor):
        if not isinstance(valor, str):
            raise TypeError("O cep deve se manter como ortograficamente válido.")

    def _verificar_cidade_tipo_invalido(self,valor):
        if not isinstance(valor, str):
            raise TypeError("A cidade deve se manter ortograficamente válido.")
                
    def __str__(self) -> str:
        return (
            f"Logradouro: {self.logradouro}, "
            f"Número: {self.numero}, "
            f"Complemento: {self.complemento}, "
            f"CEP: {self.cep}, "
            f"Cidade: {self.cidade}, "
            f"UF: {self.uf.nome}"
    )
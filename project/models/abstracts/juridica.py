from models.endereco import Endereco
from models.abstracts.pessoa import Pessoa
from abc import ABC, abstractmethod
from models.enum.sexo import Sexo

class Juridica(Pessoa, ABC):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, cnpj: str, inscricaoEstadual: str, sexo: Sexo) -> None:
        super().__init__(id, nome, telefone, email, endereco)
        self.cnpj = self._verificar_cnpj(cnpj)
        self.inscricaoEstadual = self._verificar_inscricao_estadual(inscricaoEstadual)

    def _verificar_cnpj(self,valor):
        self._verificar_cnpj_tipo_invalido(valor)

        self.cnpj = valor
        return self.cnpj

    def _verificar_inscricao_estadual(self,valor):
        self._verificar_inscricao_estadual_tipo_invalido(valor)

        self.inscricaoEstadual = valor
        return self.inscricaoEstadual
    
    def _verificar_cnpj_tipo_invalido(self,valor):
        if not isinstance(valor, str):
            raise TypeError("O cnpj deve se manter como tipo texto!")
        
    def _verificar_inscricao_estadual_tipo_invalido(self,valor):
        if not isinstance(valor, str):
            raise TypeError("A inscrição estadual deve ser um texto!")
        
    def __str__(self) -> str:
        return (
            f"\nCNPJ: {self.cnpj}"
            f"\nInscrição Estadual: {self.inscricaoEstadual}"
            f"\n{super().__str__()}"
        )

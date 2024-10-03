from models.enum.setor import Setor
from models.enum.sexo import Sexo  
from models.endereco import Endereco
from models.abstracts.fisica import Fisica
from abc import ABC, abstractmethod

class Funcionario(Fisica, ABC):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, cpf: str, rg: str, data_nascimento: str, sexo: Sexo, matricula: str, setor: Setor, salario: float) -> None:
        super().__init__(id, nome, telefone, email, endereco, cpf, rg, data_nascimento, sexo)
        self.matricula = self._verificar_matricula(matricula)
        self.setor = setor
        self.salario = self._verificar_salario(salario)

    @abstractmethod
    def salario_final(self) -> float:
        pass
    
    def _verificar_cpf(self,valor):
        self._verificar_cpf_tipo_invalido(valor)

        self.cpf = valor
        return self.cpf
    
    def _verificar_rg(self,valor):
        self._verificar_rg_tipo_invalido(valor)

        self.rg = valor
        return self.rg
    
    def _verificar_matricula(self,valor):
        self._verificar_matricula_tipo_invalido(valor)

        self.matricula = valor
        return self.matricula
    
    def _verificar_salario(self,valor):
        self._verificar_salario_tipo_invalido(valor)
        self._verificar_salario_negativo(valor)

        self.salario = valor
        return self.salario
    
    def _verificar_salario_negativo(self,valor):
        if valor <= 0:
            raise ValueError("O salário não pode ser negativo!")
    
    def _verificar_salario_tipo_invalido(self,valor):
        if not isinstance(valor, int):
            raise TypeError("O salário deve se manter como número!")

    def _verificar_cpf_tipo_invalido(self,valor):
        if not isinstance(valor, str):
            raise TypeError("O cpf deve se manter como tipo texto!")
        
    def _verificar_rg_tipo_invalido(self,valor):
        if not isinstance(valor, str):
            raise TypeError("O rg deve se manter como tipo texto!")

    def _verificar_matricula_tipo_invalido(self,valor):
        if not isinstance(valor, str):
            raise TypeError("A matricula deve se manter como tipo texto!")



    def __str__(self) -> str:
        return (
            f"\n{super().__str__()}"
            f"\nMatrícula: {self.matricula}"
            f"\nSetor: {self.setor}"
            f"\nSalário: R$ {self.salario:.2f}"
        )
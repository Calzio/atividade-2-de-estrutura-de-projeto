from models.enum.sexo import Sexo
from models.endereco import Endereco
from models.abstracts.pessoa import Pessoa
from abc import ABC, abstractmethod

class Fisica(Pessoa, ABC):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, cpf: str, rg: str, data_nascimento: str, sexo: Sexo) -> None:
        super().__init__(id, nome, telefone, email, endereco)
        self.rg = rg
        self.cpf = cpf
        self.sexo = sexo
        self.data_nascimento = self._verificar_data_nascimento(data_nascimento)

    def _verificar_data_nascimento(self, valor):
        self.__verificar_data_nascimento_tipo_invalido(valor)
        self.__verificar_data_nascimento_vazia(valor)

        self.data_nascimento = valor
        return self.data_nascimento

    def __verificar_data_nascimento_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("A data de nascimento deve ser manter como texto!")
    
    def __verificar_data_nascimento_vazia(self, valor):
        if not valor.strip():
            raise ValueError("A data de nascimento não pode ser vazia!")
        
    @abstractmethod
    def inicializar(self):
        pass

    def __str__(self) -> str:
        return (
            f"\n{super().__str__()}"
            f"\nRG: {self.rg}"
            f"\nCNPJ: {self.cpf}"
            f"\nData de Nascimento: {self.data_nascimento}"
            f"\nSexo: {self.sexo.texto}"
            f"Sigla: {self.sexo.caractere}"
        )

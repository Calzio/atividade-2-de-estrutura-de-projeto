from project.models.abstracts.funcionario import Funcionario

class Advogado(Funcionario):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: str, cpf: str, rg: str, data_nascimento: str, sexo: str, matricula: str, setor: str, salario: float, oab: str) -> None:
        super().__init__(id, nome, telefone, email, endereco, cpf, rg, data_nascimento, sexo, matricula, setor, salario)
        self.oab = self._verificar_oab(oab)

    def _verificar_oab(self,valor):
        self._verificar_oab_tipo_invalido(valor)

        self.oab = valor
        return self.oab
    
    def salario_final(self) -> float:
        return self.salario * 1.10
    
    def inicializar(self):
        return super().inicializar()

    def _verificar_oab_tipo_invalido(self,valor):
        if not isinstance(valor, str):
            raise TypeError("Oab deve se manter como ortograficamente válido.")

    def __str__(self) -> str:
        return (
            f"\nAdvogado:"
            f"{super().__str__()}"
            f"\nNúmero de OAB: {self.oab}"
        )
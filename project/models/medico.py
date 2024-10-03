from models.abstracts.funcionario import Funcionario

class Medico(Funcionario):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: str, cpf: str, rg: str, data_nascimento: str, sexo: str, matricula: str, setor: str, salario: float, crm: str) -> None:
        super().__init__(id, nome, telefone, email, endereco, cpf, rg, data_nascimento, sexo, matricula, setor, salario)
        self.crm = self._verificar_crm(crm)

    def salario_final(self) -> float:
        return super().salario_final()

    def inicializar(self):
        return super().inicializar()

    def _verificar_crm(self,valor):
        self._verificar_crm_tipo_invalido(valor)

        self.crm = valor
        return self.crm

    def _verificar_crm_tipo_invalido(self,valor):
        if not isinstance(valor, str):
            raise TypeError("O crm deve se manter como tipo texto!")

    def __str__(self) -> str:
        return (
            f"\nMédico:"
            f"{super().__str__()}"
            f"\nNúmero de CRM: {self.crm}"
        )
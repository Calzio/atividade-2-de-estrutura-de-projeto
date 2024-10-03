from models.abstracts.funcionario import Funcionario

class Engenheiro(Funcionario):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: str, cpf: str, rg: str, data_nascimento: str, sexo: str, matricula: str, setor: str, salario: float, crea: str) -> None:
        super().__init__(id, nome, telefone, email, endereco, cpf, rg, data_nascimento, sexo, matricula, setor, salario)
        self.crea = self._verificar_crea(crea)

    def _verificar_crea(self,valor):
        self._verificar_crea_tipo_invalido(valor)

        self.crea = valor
        return self.crea
    
    def salario_final(self) -> float:
        return self.salario * 1.10
    
    def inicializar(self):
        return super().inicializar()

    def _verificar_crea_tipo_invalido(self,valor):
        if not isinstance(valor, str):
            raise TypeError("O crea deve se manter como tipo texto!")
        
    def __str__(self) -> str:
        return (
            f"\nEngenheiro:"
            f"{super().__str__()}"
            f"\nNúmero de CREA: {self.crea}"
        )
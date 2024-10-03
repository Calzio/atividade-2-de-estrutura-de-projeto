from models.abstracts.fisica import Fisica
from models.enum.sexo import Sexo
from models.endereco import Endereco
from models.enum.ec import EstadoCivil

class Cliente(Fisica):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, cpf: str, rg: str, data_nascimento: str, sexo: Sexo, protocoloAtendimento: str, estado_civil: EstadoCivil) -> None:
        super().__init__(id, nome, telefone, email, endereco, cpf, rg, data_nascimento, sexo)
        self.protocoloAtendimento = protocoloAtendimento
    
    def _verificar_protocolo_de_atendimento(self, valor):
        self._verificar_protocolo_de_atendimento_tipo_invalido(valor)

        self.protocoloAtendimento = valor
        return self.protocoloAtendimento

    def inicializar(self):
        return super().inicializar()
    
    def _verificar_protocolo_de_atendimento_tipo_invalido(self, valor):
        if not isinstance(valor, int):
            raise TypeError("O protocolo de atendimento deve conter números inteiros")

    def __str__(self) -> str:
        return (
            f"\nCliente:"
            f"\n{super().__str__()}"
            f"\nProtocolo de atendimento: {self.protocoloAtendimento}"
        )

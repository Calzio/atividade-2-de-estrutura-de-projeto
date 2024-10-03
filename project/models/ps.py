from models.abstracts.juridica import Juridica

class PrestacaoServico(Juridica):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: str, cnpj: str, inscricaoEstadual: str, sexo: str, contratoInicio: str, contratoFim: str) -> None:
        super().__init__(id, nome, telefone, email, endereco, cnpj, inscricaoEstadual, sexo)
        self.contratoInicio = self._verificar_contrato_inicio(contratoInicio)
        self.contratoFim = self._verificar_contrato_fim(contratoFim)

    def _verificar_contrato_inicio(self,valor):
        self._verificar_contrato_inicio_tipo_invalido(valor)

        self.contratoInicio = valor
        return self.contratoInicio

    def inicializar(self):
        return super().inicializar()

    def _verificar_contrato_fim(self,valor):
        self._verificar_contrato_fim_tipo_invalido(valor)

        self.contratoFim = valor
        return self.contratoFim

    def _verificar_contrato_inicio_tipo_invalido(self,valor):
        if not isinstance(valor, str):
            raise TypeError("O inicio de contrato deve se manter como texto!")

    def _verificar_contrato_fim_tipo_invalido(self,valor):
        if not isinstance(valor, str):
            raise TypeError("O fim de contrato deve se manter como texto!")

    def __str__(self) -> str:
        return (
            f"\nPrestação de serviços:"
            f"\n{super().__str__()}"
            f"\nContrato início: {self.contratoInicio}"
            f"\nContrato fim: {self.contratoFim}"
        )
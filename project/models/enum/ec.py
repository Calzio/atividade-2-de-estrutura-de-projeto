from enum import Enum

class EstadoCivil(Enum):
    SOLTEIRO = "Solteiro"
    CASADO = "Casado"
    DIVORCIADO = "Divorciado"
    VIUVO = "Viúvo"
    SEPARADO = "Separado"

    def __init__(self, texto: str) -> None:
        self.texto = texto
        super().__init__()
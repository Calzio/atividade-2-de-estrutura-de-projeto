from enum import Enum

class Sexo(Enum):
    MASCULINO = ("Masculino", "M")
    FEMININO = ("Feminino", "F")
    
    def __init__(self, texto: str, caractere: str) -> None:
        self.texto = texto
        self.caractere = caractere
        super().__init__()
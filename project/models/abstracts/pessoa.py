from abc import ABC, abstractmethod
from models.endereco import Endereco

class Pessoa(ABC):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco) -> None:
        self.id = self._verificar_id(id)
        self.nome = self._verificar_nome(nome)
        self.telefone = self._verificar_telefone(telefone)
        self.email = self._verificar_email(email)
        self.endereco = endereco

    def _verificar_id(self,valor):
        self._verificar_id_tipo_invalido(valor)
        self._verificar_id_negativo(valor)

        self.id = valor
        return self.id

    def _verificar_nome(self,valor):
        self._verificar_nome_tipo_invalido(valor)
        self._verificar_nome_vazio(valor)

        self.nome = valor
        return self.nome
    
    def _verificar_telefone(self,valor):
        self._verificar_telefone_tipo_invalido(valor)

        self.telefone = valor
        return self.telefone
    
    def _verificar_email(self,valor):
        self._verificar_email_tipo_invalido(valor)

        self.email = valor
        return self.email

    def _verificar_id_tipo_invalido(self,valor):
        if not isinstance(valor, int):
            raise TypeError("O id deve se manter como um número inteiro!")

    def _verificar_id_negativo(self,valor):
        if valor <= 0:
            raise ValueError("O id não pode ser negativo!")
        
    def _verificar_nome_tipo_invalido(self,valor):
        if not isinstance(valor, str):
            raise TypeError("O nome deve se manter como um texto!")
        
    def _verificar_nome_vazio(self,valor):
        if not valor.strip():
            raise TypeError("O nome não pode estar vazio!")
        
    def _verificar_telefone_tipo_invalido(self,valor):
        if not isinstance(valor, str):
            raise TypeError("O telefone deve se manter como tipo texto!")
        
    def _verificar_email_tipo_invalido(self,valor):
        if not isinstance(valor, str):
            raise TypeError("O email deve se manter como texto!")
        

    def __str__(self) -> str:
        return (
            f"ID: {self.id}"
            f"\nNome: {self.nome}"
            f"\nTelefone: {self.telefone}"
            f"\nEmail: {self.email}"
            f"\nEndereço: {self.endereco}"
        )
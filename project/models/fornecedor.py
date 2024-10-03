from models.abstracts.juridica import Juridica

class Fornecedor(Juridica):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: str, cnpj: str, inscricaoEstadual: str, sexo: str, produto: str) -> None:
        super().__init__(id, nome, telefone, email, endereco, cnpj, inscricaoEstadual, sexo)
        self.produto = self._verificar_produto(produto)

    def _verificar_produto(self, valor):
        self.__verificar_produto_tipo_invalido(valor)
        self.__produto_vazio(valor)

        self.produto = valor
        return self.produto
    
    def __verificar_produto_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("O produto deve ser manter como texto!")
    
    def __produto_vazio(self, valor):
        if not valor.strip():
            raise ValueError("O produto não pode ser vazio!")

    def __str__(self) -> str:
        return (
            f"\nFornecedor:"
            f"\n{super().__str__()}"
            f"\nProduto: {self.produto}"
        )
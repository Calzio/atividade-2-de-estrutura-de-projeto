import pytest
from project.models.fornecedor import Fornecedor
from project.models.endereco import Endereco
from project.models.enum.uf import UnidadeFederativa

@pytest.fixture
def fornecedor_valido():
    fornecedor = Fornecedor(912, "Caio", "1234-5678", "Caiooo@gmail.com", Endereco("Rua 20", "12", "N/A", "1111", "Salvador", UnidadeFederativa.BAHIA), "1212", "2121", "Monitor")
    return fornecedor

def test_produto_valido(fornecedor_valido):
    assert fornecedor_valido.produto == "Placa de video"

def test_mudar_produto_valido(fornecedor_valido):
    fornecedor_valido.produto = "Processador"
    assert fornecedor_valido.produto == "Processador"

def test_produto_tipo_invalido():
    with pytest.raises(TypeError, match="O produto deve se manter do tipo texto!"):
        Fornecedor(912, "Caio", "1234-5678", "Caiooo@gmail.com", Endereco("Rua 20", "12", "N/A", "1111", "Salvador", UnidadeFederativa.BAHIA), "1212", "2323", 4444)
import pytest
from project.models.endereco import Endereco
from project.models.enum.uf import UnidadeFederativa

@pytest.fixture
def endereco_valido():
    endereco = Endereco("Rua 20", "12", "N/A", "1111", "Salvador", UnidadeFederativa.BAHIA)
    return endereco

def test_logradouro_valido(endereco_valido):
    assert endereco_valido.logradouro == "Rua 20"

def test_mudar_logradouro_valido(endereco_valido):
    endereco_valido.logradouro = "Rua 10"
    assert endereco_valido.logradouro == "Rua 10"

def test_numero_valido(endereco_valido):
    assert endereco_valido.numero == "12"

def test_mudar_numero_valido(endereco_valido):
    endereco_valido.numero = "6"
    assert endereco_valido.numero == "6"

def test_complemento_valido(endereco_valido):
    assert endereco_valido.complemento == "N/A"

def test_mudar_complemento_valido(endereco_valido):
    endereco_valido.complemento = "Casa 79"
    assert endereco_valido.complemento == "Casa 79"

def test_cep_valido(endereco_valido):
    assert endereco_valido.cep == "1111"

def test_mudar_cep_valido(endereco_valido):
    endereco_valido.cep = "2222"
    assert endereco_valido.cep == "2222"

def test_cidade_valido(endereco_valido):
    assert endereco_valido.cidade == "Salvador"

def test_mudar_cidade_valido(endereco_valido):
    endereco_valido.cidade = "São Paulo"
    assert endereco_valido.cidade == "São Paulo"

def test_logradouro_tipo_invalido():
    with pytest.raises(TypeError, match="O logradouro deve se manter como texto!"):
        Endereco(55 , "12", "N/A", "1111", "Salvador", UnidadeFederativa.BAHIA)

def test_numero_tipo_invalido():
    with pytest.raises(TypeError, match="O número deve se manter como tipo texto!"):
        Endereco("Rua 20", 12, "N/A", "1111", "Salvador", UnidadeFederativa.BAHIA)

def test_complemento_tipo_invalido():
    with pytest.raises(TypeError, match="O complemento deve se manter como tipo texto!"):
        Endereco("Rua 20", "12", 44, "1111", "Salvador", UnidadeFederativa.BAHIA)

def test_cep_tipo_invalido():
    with pytest.raises(TypeError, match="O cep deve se manter como tipo texto!"):
        Endereco("Rua 20", "12", "N/A", 1111, "Salvador", UnidadeFederativa.BAHIA)

def test_cidade_tipo_invalido():
    with pytest.raises(TypeError, match="A cidade deve se manter como texto!"):
        Endereco("Rua 20", "12 ", "N/A", "1111", 66, UnidadeFederativa.BAHIA)
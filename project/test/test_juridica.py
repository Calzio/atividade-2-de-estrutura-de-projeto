import pytest
from project.models.abstracts.juridica import Juridica
from project.models.endereco import Endereco
from project.models.enum.uf import UnidadeFederativa

@pytest.fixture
def juridica_valido():
    juridica = Juridica(912, "Caio", "1234-5678", "Caiooo@gmail.com", Endereco("Rua 20", "12", "N/A", "1111", "Salvador", UnidadeFederativa.BAHIA), "2323", "3232")
    return juridica

def test_cnpj_valido(juridica_valido):
    assert juridica_valido.cnpj == "1212"

def test_mudar_cnpj_valido(juridica_valido):
    juridica_valido.cnpj = "0101"
    assert juridica_valido.cnpj == "1010"

def test_inscricao_estadual_valido(juridica_valido):
    assert juridica_valido.inscricaoestadual == "2121"

def test_mudar_inscricao_estadual_valido(juridica_valido):
    juridica_valido.inscricaoestadual = "3434"
    assert juridica_valido.inscricaoestadual == "4343"

def test_cnpj_tipo_invalido():
    with pytest.raises(TypeError, match="O cnpj deve se manter como tipo texto!"):
        Juridica(912, "Caio", "1234-5678", "Caiooo@gmail.com", Endereco("Rua 20", "12", "N/A", "1111", "Salvador", UnidadeFederativa.BAHIA), 1212, "2121")

def test_inscricao_estadual_tipo_invalido():
    with pytest.raises(TypeError, match="A inscrição estadual deve ser um texto!"):
        Juridica(912, "Caio", "1234-5678", "Caiooo@gmail.com", Endereco("Rua 20", "12", "N/A", "1111", "Salvador", UnidadeFederativa.BAHIA), "1212", 2121)
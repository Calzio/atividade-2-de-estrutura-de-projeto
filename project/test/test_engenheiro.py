import pytest
from project.models.engenheiro import Engenheiro
from project.models.endereco import Endereco
from project.models.enum.ec import EstadoCivil
from project.models.enum.sexo import Sexo
from project.models.enum.uf import UnidadeFederativa
from project.models.enum.setor import Setor

@pytest.fixture
def engenheiro_valido():
    engenheiro = Engenheiro(912, "Caio", "1234-5678", "Caiooo@gmail.com", Endereco("Rua 20", "12", "N/A", "1111", "Salvador", UnidadeFederativa.BAHIA), Sexo.MASCULINO, EstadoCivil.SOLTEIRO, "19/06/2006", "2222", "3333", "4444", Setor.ENGENHARIA, 5000, "5555")
    return engenheiro

def test_crea_valido(engenheiro_valido):
    assert engenheiro_valido.crea == "5555"

def test_mudar_crea_valido(engenheiro_valido):
    engenheiro_valido.crea = "3333"
    assert engenheiro_valido.crea == "3333"

def test_crea_tipo_invalido():
    with pytest.raises(TypeError, match="O crea deve se manter como tipo texto!"):
        Engenheiro(912, "Caio", "1234-5678", "Caiooo@gmail.com", Endereco("Rua 20", "12", "N/A", "1111", "Salvador", UnidadeFederativa.BAHIA), Sexo.MASCULINO, EstadoCivil.SOLTEIRO, "19/06/2006", "2222", "3333", "4444", Setor.ENGENHARIA, 5000, 5555)
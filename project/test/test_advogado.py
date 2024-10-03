import pytest
from project.models.advogado import Advogado
from project.models.endereco import Endereco
from project.models.enum.ec import EstadoCivil
from project.models.enum.sexo import Sexo
from project.models.enum.uf import UnidadeFederativa
from project.models.enum.setor import Setor

@pytest.fixture
def advogado_valido():
    advogado = Advogado(912, "Caio", "1234-5678", "Caiooo@gmail.com", Endereco("Rua 20", "12", "N/A", "1902", "Salvador", UnidadeFederativa.BAHIA), Sexo.MASCULINO, EstadoCivil.SOLTEIRO, "06/19/2006", "1549", "4104", "9102", Setor.SAUDE, 5000, "777")
    return advogado

def test_oab_valido(advogado_valido):
    assert advogado_valido.oab == "777"

def test_mudar_oab_valido(advogado_valido):
    advogado_valido.oab = "8888"
    assert advogado_valido.oab == "8888"

def test_oab_tipo_invalido():
    with pytest.raises(TypeError, match="Oab deve se manter como tipo texto!"):
        Advogado(912, "Caio", "1234-5678", "Caiooo@gmail.com", Endereco("Rua 20", "12", "N/A", "1902", "Salvador", UnidadeFederativa.BAHIA), Sexo.MASCULINO, EstadoCivil.SOLTEIRO, "06/19/2006", "1549", "4104", "9102", Setor.SAUDE, 5000, 777)
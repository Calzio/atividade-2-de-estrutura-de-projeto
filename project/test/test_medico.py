import pytest
from project.models.medico import Medico
from project.models.endereco import Endereco
from project.models.enum.ec import EstadoCivil
from project.models.enum.sexo import Sexo
from project.models.enum.uf import UnidadeFederativa
from project.models.enum.setor import Setor

@pytest.fixture
def medico_valido():
    medico = Medico(912, "Caio", "1234-5678", "Caiooo@gmail.com", Endereco("Rua 20", "12", "N/A", "1111", "Salvador", UnidadeFederativa.BAHIA), Sexo.MASCULINO, EstadoCivil.SOLTEIRO, "19/06/2006", "2222", "3333", "4444", Setor.SAUDE, 5000, "66666")
    return medico

def test_crm_valido(medico_valido):
    assert medico_valido.crm == "66666"

def test_mudar_crm_valido(medico_valido):
    medico_valido.crm = "33333"
    assert medico_valido.crm == "33333"

def test_crm_tipo_invalido():
    with pytest.raises(TypeError, match="O crm deve se manter como tipo texto!"):
        Medico(912, "Caio", "1234-5678", "Caiooo@gmail.com", Endereco("Rua 20", "12", "N/A", "1111", "Salvador", UnidadeFederativa.BAHIA), Sexo.MASCULINO, EstadoCivil.SOLTEIRO, "19/06/2006", "2222", "3333", "4444", Setor.SAUDE, 5000, 66666)
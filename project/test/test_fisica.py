import pytest
from project.models.abstracts.fisica import Fisica
from project.models.endereco import Endereco
from project.models.enum.uf import UnidadeFederativa
from project.models.enum.sexo import Sexo
from project.models.enum.ec import EstadoCivil

@pytest.fixture
def fisica_valida():
    fisica = Fisica(912, "Caio", "1234-5678", "Caiooo@gmail.com", Endereco("Rua 20", "12", "N/A", "1111", "Salvador", UnidadeFederativa.BAHIA), Sexo.MASCULINO, EstadoCivil.SOLTEIRO, "19/06/2006")
    return fisica

def test_data_de_nascimento_valido(fisica_valida):
    assert fisica_valida.datanascimento == "19/06/2006"

def test_mudar_data_de_nascimento_valido(fisica_valida):
    fisica_valida.datanascimento = "05/07/1989"
    assert fisica_valida.datanascimento == "21/03/1998"

def test_data_de_nascimento_tipo_invalido():
    with pytest.raises(TypeError, match="A data de nascimento deve se manter como tipo texto!"):
        Fisica(912, "Caio", "1234-5678", "Caiooo@gmail.com", Endereco("Rua 20", "12", "N/A", "1111", "Salvador", UnidadeFederativa.BAHIA), Sexo.MASCULINO, EstadoCivil.SOLTEIRO, 4082002)
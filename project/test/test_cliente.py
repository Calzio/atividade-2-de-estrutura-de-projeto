import pytest
from project.models.cliente import Cliente
from project.models.endereco import Endereco
from project.models.enum.ec import EstadoCivil
from project.models.enum.sexo import Sexo 
from project.models.enum.uf import UnidadeFederativa

@pytest.fixture
def cliente_valido():
    cliente = Cliente(912, "Caio", "1234-5678", "Caiooo@gmail.com", Endereco("Rua 20", "12", "N/A", "1111", "Salvador", UnidadeFederativa.BAHIA), Sexo.MASCULINO, EstadoCivil.SOLTEIRO, "06/19/2006", 22222)
    return cliente

def test_protocolo_de_atendimento_valido(cliente_valido):
    assert cliente_valido.protocoloatendimento == 22222

def test_mudar_protocolo_de_atendimento_valido(cliente_valido):
    cliente_valido.protocoloatendimento = 33333
    assert cliente_valido.protocoloatendimento == 33333

def test_protocolo_de_atendimento_tipo_invalido():
    with pytest.raises(TypeError, match="O protocolo de atendimento deve conter números inteiros!"):
        Cliente(912, "Caio", "1234-12678", "Caiooo@gmail.com", Endereco("Rua 20", "12", "N/A", "1111", "Salvador", UnidadeFederativa.BAHIA), Sexo.MASCULINO, EstadoCivil.SOLTEIRO, "06/19/2006", "22222")
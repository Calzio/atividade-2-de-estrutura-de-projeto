import pytest
from project.models.abstracts.funcionario import Funcionario
from project.models.endereco import Endereco
from project.models.enum.uf import UnidadeFederativa
from project.models.enum.setor import Setor
from project.models.enum.sexo import Sexo
from project.models.enum.ec import EstadoCivil

@pytest.fixture
def funcionario_valido():
    funcionario = Funcionario(912, "Caio", "1234-5678", "Caiooo@gmail.com", Endereco("Rua 20", "12", "N/A", "1111", "Salvador", UnidadeFederativa.BAHIA), Sexo.MASCULINO, EstadoCivil.SOLTEIRO, "19/06/2006", "2222", "3333", "4444", Setor.ENGENHARIA, 5000)
    return funcionario

def test_salario_valido(funcionario_valido):
    assert funcionario_valido.salario == 5000

def test_mudar_salario_valido(funcionario_valido):
    funcionario_valido.salario = 6000
    assert funcionario_valido.salario == 6000

def test_cpf_valido(funcionario_valido):
    assert funcionario_valido.cpf == "2222"

def test_mudar_cpf_valido(funcionario_valido):
    funcionario_valido.cpf = "2323"
    assert funcionario_valido.cpf == "2323"

def test_rg_valido(funcionario_valido):
    assert funcionario_valido.rg == "3333"

def test_mudar_rg_valido(funcionario_valido):
    funcionario_valido.rg = "3232"
    assert funcionario_valido.rg == "3232"

def test_matricula_valido(funcionario_valido):
    assert funcionario_valido.matricula == "4444"

def test_mudar_matricula_valido(funcionario_valido):
    funcionario_valido.matricula = "4343"
    assert funcionario_valido.matricula == "4343"

def test_salario_negativo():
    with pytest.raises(ValueError, match="O salário não pode ser negativo!"):
        Funcionario(912, "Caio", "1234-5678", "Caiooo@gmail.com", Endereco("Rua 20", "12", "N/A", "1111", "Salvador", UnidadeFederativa.BAHIA), Sexo.MASCULINO, EstadoCivil.SOLTEIRO, "19/06/2006", "2222", "3333", "4444", Setor.ENGENHARIA, -5000)

def test_salario_tipo_invalido():
    with pytest.raises(TypeError, match="O salário deve se manter como número!"):
        Funcionario(912, "Caio", "1234-5678", "Caiooo@gmail.com", Endereco("Rua 20", "12", "N/A", "1111", "Salvador", UnidadeFederativa.BAHIA), Sexo.MASCULINO, EstadoCivil.SOLTEIRO, "19/06/2006", "2222", "3333", "4444", Setor.ENGENHARIA, "5000")

def test_cpf_tipo_invalido():
    with pytest.raises(TypeError, match="O cpf deve se manter como tipo texto!"):
        Funcionario(912, "Caio", "1234-5678", "Caiooo@gmail.com", Endereco("Rua 20", "12", "N/A", "1111", "Salvador", UnidadeFederativa.BAHIA), Sexo.MASCULINO, EstadoCivil.SOLTEIRO, "19/06/2006", 2222, "3333", "4444", Setor.ENGENHARIA, 5000)
    
def test_rg_tipo_invalido():
    with pytest.raises(TypeError, match="O rg deve se manter como tipo texto!"):
        Funcionario(912, "Caio", "1234-5678", "Caiooo@gmail.com", Endereco("Rua 20", "12", "N/A", "1111", "Salvador", UnidadeFederativa.BAHIA), Sexo.MASCULINO, EstadoCivil.SOLTEIRO, "19/06/2006", "2222", 3333, "4444", Setor.ENGENHARIA, 5000)

def test_matricula_tipo_invalido():
    with pytest.raises(TypeError, match="A matricula deve se manter como tipo texto!"):
        Funcionario(912, "Caio", "1234-5678", "Caiooo@gmail.com", Endereco("Rua 20", "12", "N/A", "1111", "Salvador", UnidadeFederativa.BAHIA), Sexo.MASCULINO, EstadoCivil.SOLTEIRO, "19/06/2006", "2222", "3333", 4444, Setor.ENGENHARIA, 5000)
import pytest
from project.models.abstracts.pessoa import Pessoa
from project.models.endereco import Endereco
from project.models.enum.uf import UnidadeFederativa

@pytest.fixture
def pessoa_valida():
    pessoa = Pessoa(912, "Caio", "1234-5678", "Caiooo@gmail.com", Endereco("Rua 20", "12", "N/A", "1111", "Salvador", UnidadeFederativa.BAHIA))
    return pessoa

def test_id_valido(pessoa_valida):
    assert pessoa_valida.id == 912

def test_nome_valido(pessoa_valida):
    assert pessoa_valida.nome == "Caio"

def test_mudar_nome_valido(pessoa_valida):
    pessoa_valida.nome = "Albert"
    assert pessoa_valida.nome == "Albert"

def test_numero_valido(pessoa_valida):
    assert pessoa_valida.telefone == "3333-4444"

def test_mudar_numero_valido(pessoa_valida):
    pessoa_valida.telefone = "4444-3333"
    assert pessoa_valida.telefone == "4444-3333"

def test_email_valido(pessoa_valida):
    assert pessoa_valida.email == "Caiooo@gmail.com"

def test_mudar_email_valido(pessoa_valida):
    pessoa_valida.email = "Luan21@gmail.com"
    assert pessoa_valida.email == "Luan21@gmail.com"

def test_id_negativo():
    with pytest.raises(ValueError, match="O id não pode ser negativo!"):
        Pessoa(-912 , "Caio", "3333-4444", "Caiooo@gmail.com", Endereco("Rua 20", "12", "N/A", "1111", "Salvador", UnidadeFederativa.BAHIA))

def test_id_tipo_invalido():
    with pytest.raises(TypeError, match="O id deve se manter como um número inteiro!"):
        Pessoa("912", "Caio", "3333-4444", "Caiooo@gmail.com", Endereco("Rua 20", "12", "N/A", "1111", "Salvador", UnidadeFederativa.BAHIA))

def test_nome_tipo_invalido():
    with pytest.raises(TypeError, match="O nome deve se manter como um texto!"):
        Pessoa(912, 22, "3333-4444", "Caiooo@gmail.com", Endereco("Rua 20", "12", "N/A", "1111", "Salvador", UnidadeFederativa.BAHIA))

def test_nome_vazio():
    with pytest.raises(TypeError, match="O nome não pode estar vazio!"):
        Pessoa(912, "", "3333-4444", "Caiooo@gmail.com", Endereco("Rua 20", "12", "N/A", "1111", "Salvador", UnidadeFederativa.BAHIA))

def test_numero_tipo_valido():
    with pytest.raises(TypeError, match="O telefone deve se manter como tipo texto!"):
        Pessoa(912, "Caio", 33, "Caiooo@gmail.com", Endereco("Rua 20", "12", "N/A", "1111", "Salvador", UnidadeFederativa.BAHIA))

def test_email_tipo_valido():
    with pytest.raises(TypeError, match="O email deve se manter como texto!"):
        Pessoa(912, "Caio", "3333-4444", 222 , Endereco("Rua 20", "12", "N/A", "1111", "Salvador", UnidadeFederativa.BAHIA))
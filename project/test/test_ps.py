import pytest
from project.models.ps import PrestacaoServico
from project.models.endereco import Endereco
from project.models.enum.uf import UnidadeFederativa

@pytest.fixture
def prestacao_servicos_valido():
    prestacaoservico = PrestacaoServico(912, "Caio", "1234-5678", "Caiooo@gmail.com", Endereco("Rua 20", "12", "N/A", "1111", "Salvador", UnidadeFederativa.BAHIA), "2323", "3232", "18/09/2021", "!8/09/2023")
    return prestacaoservico

def test_contrato_inicio_valido(prestacao_servicos_valido):
    assert prestacao_servicos_valido.contratoinicio == "18/09/2021"

def test_mudar_contrato_inicio_valido(prestacao_servicos_valido):
    prestacao_servicos_valido.contratoinicio = "02/03/2024"
    assert prestacao_servicos_valido.contratoinicio == "02/03/2024"

def test_contrato_fim_valido(prestacao_servicos_valido):
    assert prestacao_servicos_valido.contratofim == "!8/09/2023"

def test_mudar_contrato_fim_valido(prestacao_servicos_valido):
    prestacao_servicos_valido.contratofim = "02/03/2025"
    assert prestacao_servicos_valido.contratofim == "02/03/2025"

def test_contrato_inicio_tipo_invalido():
    with pytest.raises(TypeError, match="O inicio de contrato deve se manter como texto!"):
        PrestacaoServico(912, "Caio", "1234-5678", "Caiooo@gmail.com", Endereco("Rua 20", "12", "N/A", "1111", "Salvador", UnidadeFederativa.BAHIA), "2323", "3232", 28092024, "!8/09/2023")

def test_contrato_fim_tipo_invalido():
    with pytest.raises(TypeError, match="O fim de contrato deve se manter como texto!"):
        PrestacaoServico(912, "Caio", "1234-5678", "Caiooo@gmail.com", Endereco("Rua 20", "12", "N/A", "1111", "Salvador", UnidadeFederativa.BAHIA), "2323", "3232", "18/09/2021", 28092025)
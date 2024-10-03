import sys
sys.path.append('/workspaces/atividade-2-de-estrutura-de-projeto')
from models.enum.ec import EstadoCivil
from models.enum.sexo import Sexo
from models.enum.setor import Setor
from models.enum.uf import UnidadeFederativa
from models.endereco import Endereco
from models.engenheiro import Engenheiro
from models.medico import Medico
from models.advogado import Advogado
from models.cliente import Cliente
from models.ps import PrestacaoServico
from models.fornecedor import Fornecedor

endereco1 = Endereco("Rua Adelino", "12", "N/A", "5555", "Salvador", UnidadeFederativa.BAHIA)
endereco2 = Endereco("Samaté", "34", "N/A", "5555", "Pindamonhangaba", UnidadeFederativa.SAO_PAULO)
endereco3 = Endereco("Copacabana", "56", "N/A", "5555", "Copa Cabana", UnidadeFederativa.RIO_DE_JANEIRO)
endereco4 = Endereco("Abrantes", "78", "N/A", "5555", "Salvador", UnidadeFederativa.BAHIA)

eng = Engenheiro(1222, "João", "9999-9999", "jon@gmail.com", endereco1, "12121212", "2121212", "s212121", Sexo.MASCULINO, "2112121", "Engenharia", 8000, "valido")
medico = Medico(222, "Albert", "9842-9842", "Albertin@gmail.com", endereco2, "2121212", "22222", "22/02/2002", Sexo.MASCULINO, "asasasa", Setor.SAUDE, 9000, "valido")
advogado = Advogado(333, "Naranccia", "9876-9876", "Narranccia@gmail.com", endereco4, "489141809", "4279342890", "04/02/2000", Sexo.FEMININO, "asasasa", Setor.JURIDICO, 3129, "válido")
cliente = Cliente(333, "Bruno", "1294-4192", "Bruuno@gmail.com", endereco1, "123891412", "412491829", "12/02/1990", Sexo.MASCULINO, "123456789", EstadoCivil.SOLTEIRO)
prestacao_servico = PrestacaoServico(1234, "Carlos", "4109-9521", "CarlosdaBahia@gmail.com", endereco1, "12412451", "12419204", Sexo.MASCULINO, "12/02/1991", "20/20/2020")
fornecedor = Fornecedor(124, "Joseph", "0112-1429", "JosephJoestar@gmail.com", endereco3, "1204194", "12/04/1991", Sexo.MASCULINO, "flecha de stand")

print(eng)
print(medico)
print(advogado)
print(cliente)
print(prestacao_servico)
print(fornecedor)
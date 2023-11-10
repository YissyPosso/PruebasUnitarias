import pytest

@pytest.fixture
def lista_de_numeros():
    return [1, 2, 3, 4, 5]

def test_longitud_de_lista(lista_de_numeros):
    assert len(lista_de_numeros) == 5

def test_elemento_en_lista(lista_de_numeros):
    assert 3 in lista_de_numeros
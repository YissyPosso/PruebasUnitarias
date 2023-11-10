import pytest
from base_datos import base_datos


@pytest.fixture
def mock_db(mocker):
    mock_db = mocker.MagicMock()
    mock_db.execute.return_value = "Registro insertado correctamente"
    return mock_db

def test_insert_data(mock_db):

    db_client = base_datos("mi_base_de_datos.db")
    db_client.create_table()
    resultado = db_client.insert_data("mi_registro")
    assert resultado == "Registro insertado correctamente"
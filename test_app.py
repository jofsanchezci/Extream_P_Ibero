import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    """Verifica que la página de inicio carga correctamente"""
    assert rv.status_code == 200
    #assert b'Aplicación XP' in rv.data

def test_process(client):
    """Verifica que el proceso funcione correctamente"""
    rv = client.post('/process', data={'user_input': 'Hola Mundo'})
    assert rv.status_code == 200
    print('Has ingresado: Hola Mundo' in rv.data)

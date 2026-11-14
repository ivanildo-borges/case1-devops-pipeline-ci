import pytest
from app import create_app

# Cria um cliente de teste falso para não precisarmos subir o servidor real
@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_status_code (client):
    resposta = client.get('/')
    assert resposta.status_code == 200

def test_home_mensagem(client):
    resposta = client.get('/')
    dados = resposta.get_json()
    assert dados ['mensagem'] == "Bem-vindo a API FastOrder!"
import pytest
from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_soma_valida(client):
    resposta = client.get('/api/soma?a=10&b=20')
    dados = resposta.get_json()
    assert resposta.status_code == 200
    assert dados['resultado'] == 30.0


# TESTE1: Garantir que a rota "/api/desconto" retorne 403 quando a Flag estiver desativada
def test_desconto_desativado(client, monkeypatch):
    import app as app_module
    monkeypatch.setattr(app_module, 'FEATURE_DESCONTO_PROMO', False)

    resposta = client.get('/api/desconto?valor=100&porcentagem=15')
    assert resposta.status_code == 403
    dados = resposta.get_json()
    assert dados['flag_status'] is False


# TESTE2: Garantir que a rota "/api/desconto" funcione e retorne 200 quando a Flag estiver ativada
def test_desconto_ativado(client, monkeypatch):
    import app as app_module
    monkeypatch.setattr(app_module, 'FEATURE_DESCONTO_PROMO', True)

    resposta = client.get('/api/desconto?valor=100&porcentagem=15')
    assert resposta.status_code == 200
    dados = resposta.get_json()
    assert dados['valor_final'] == 85.0

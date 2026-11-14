import os
from flask import Flask
from app.routes import api

# Feature Flag lida de variavel de ambiente (padrao: desativada).
# Fica como variavel do modulo para os testes poderem alterar com monkeypatch.
FEATURE_DESCONTO_PROMO = os.getenv("FEATURE_DESCONTO_PROMO", "false").lower() == "true"


def create_app():
    app = Flask(__name__)
    app.register_blueprint(api)
    return app

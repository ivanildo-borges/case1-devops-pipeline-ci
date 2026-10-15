from flask import Blueprint, jsonify, request

api = Blueprint("api", __name__)


@api.route("/")
def home():
    return jsonify({"mensagem": "Bem-vindo a API FastOrder!"})


@api.route("/api/status")
def status():
    return jsonify({"status": "operacional", "servico": "Fastorder-Web"})


@api.route("/api/soma")
def soma():
    a = request.args.get("a", type=int)
    b = request.args.get("b", type=int)

    if a is None or b is None:
        return jsonify({"error": "Parâmetros a e b são obrigatórios"}), 400

    return jsonify({"resultado": a + b})

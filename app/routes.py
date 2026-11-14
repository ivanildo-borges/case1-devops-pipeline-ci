from flask import Blueprint, jsonify, request

api = Blueprint("api", __name__)


@api.route("/")
def home():
    return jsonify({"mensagem": "Bem-vindo a API FastOrder!"})


@api.route("/api/status")
def status():
    import app as app_pkg
    return jsonify({
        "status": "operacional",
        "servico": "Fastorder-Web",
        "flags": {
            "desconto_promo": app_pkg.FEATURE_DESCONTO_PROMO
        }
    })


@api.route("/api/soma")
def soma():
    a = request.args.get("a", type=int)
    b = request.args.get("b", type=int)

    if a is None or b is None:
        return jsonify({"error": "Parâmetros a e b são obrigatórios"}), 400

    return jsonify({"resultado": a + b})


# Nova Rota - Protegida pela Feature Flag
@api.route("/api/desconto")
def desconto():
    import app as app_pkg

    if not app_pkg.FEATURE_DESCONTO_PROMO:
        return jsonify({
            "erro": "Funcionalidade em construcao ou desativada temporariamente",
            "flag_status": False
        }), 403

    try:
        valor_total = float(request.args.get("valor", 0))
        porcentagem = float(request.args.get("porcentagem", 10))

        if valor_total <= 0:
            return jsonify({"erro": "Valor deve ser maior que zero"}), 400

        valor_com_desconto = valor_total - (valor_total * (porcentagem / 100))
        return jsonify({
            "valor_original": valor_total,
            "desconto_aplicado": f"{porcentagem}%",
            "valor_final": valor_com_desconto
        })
    except (ValueError, TypeError):
        return jsonify({"erro": "Parametros de desconto invalidos"}), 400

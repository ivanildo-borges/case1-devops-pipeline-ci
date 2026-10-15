from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({ "mensagem": "Bem-vindo a API FastOrder!" })

@app.route('/api/status')
def status():
    return jsonify({ "status": "operacional", "servico": "Fastorder-Web" })

# TODO: Missão 5.1 - Crie uma nova rota chamada /api/soma
# Ela deve receber dois parâmetros via Query String (?a=2&b=3)
# E retornar um JSON no formato {"resultado": 5}
@app.route('/api/soma')
def soma():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    if a is None or b is None:
        return jsonify({ "error": "Parâmetros a e b são obrigatórios" }), 400
    return jsonify({ "resultado": a + b })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
from flask import Flask, request, jsonify
import redis    # Biblio
import json     # B. Requisito p dumps

app = Flask(__name__)
# Cria cliente redis e conecta
redis_client = redis.Redis(host='localhost', port=6379, db=0)


@app.route("/sorter/", methods=["POST"])
def retorna_json():

    data = request.get_json()  # Obtém dados JSON da requisição
    # Armazena dados json no redis chave data, dumps converte obj py data em string json
    redis_client.set('data', json.dumps(data))

    response = {
        "message": "Recebido com sucesso",
        "data": data
    }
    return jsonify(response)


if __name__ == "__main__":
    app.run()

    # flask run --port 9009

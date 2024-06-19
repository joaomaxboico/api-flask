# from flask import Flask  # Importação do Flask
from flask import Flask, request, jsonify

app = Flask(__name__)  # Cria instância (aplicação flask)


# Define rota, qd se mapeia pasta pelo POST, chama função com o retorno.
@app.route("/sorter/", methods=["POST"])
def retorna_json():
    # Exemplo de resposta JSON
    data = request.get_json()  # Obtém dados JSON da requisição
    response = {
        "message": "Recebido com sucesso",
        "data": data
    }
    return jsonify(response)  # Retorna a resposta JSON


if __name__ == "__main__":  # Executa a aplicação flask
    app.run()

    # Executar rodando em outra porta:
    # flask run --port 8008

    # Postman localhost:8008/sorter

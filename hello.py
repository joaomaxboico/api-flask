from flask import Flask  # Importação do Flask

app = Flask(__name__)  # Cria instância (aplicação flask)


# Define rota, qd se mapeia pasta pelo get, chama função com o retorno.
@app.route("/sorter/", methods=["GET"])
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == "__main__":  # Executa a aplicação flask
    app.run(port=8008)  # inicia a aplicação na porta 8008
# teste git novo

# site com os scripts: https://cdnjs.com/
# pip install python-socketio flask-socketio simple-websocket

# http://localhost:5000/

from flask import Flask, render_template  # estruturas para criar o site
from flask_socketio import SocketIO, send  # estruturas para criar o chat

app = Flask(__name__)  # cria o site
# chave de seguranca, pode ser qualquer coisa, mas escolha algo dificil
app.config["SECRET"] = "ajuiahfa78fh9f78shfs768fgs7f6"
app.config["DEBUG"] = True  # para testarmos o código, no final tiramos

# cria a conexão entre diferentes máquinas que estão no mesmo site
Socketio = SocketIO(app, cors_allowed_origins="*")

# funcionalidade de enviar mesagem


# define que a função abaixo vai ser acionada quando o evento de "message" acontecer
@Socketio.on("message")
def gerenciar_menssagem(mensagem):
    print(f"Mensagem: {mensagem}")
    # envia a mensagem para todo mundo conectado no site
    send(mensagem, broadcast=True)

# criar a nossa primeira pagina = primeira rota


@app.route("/")  # cria a página do site
def homepage():
    # essa página vai carregar esse arquivo html que está aqui
    return render_template("index.html")


# roda o nosso aplicativo
if __name__ == "__main__":
    # define que o app vai rodar no seu servidor local, ou seja, na internet em que o seu computador tá conectado
    Socketio.run(app, host="localhost")

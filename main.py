# site com os scripts: https://cdnjs.com/
# pip install python-socketio flask-socketio simple-websocket

# http://localhost:5000/

from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
Socketio = SocketIO(app, cors_allowed_origins="*")

# funcionalidade de enviar mesagem
@Socketio.on("message")
def gerenciar_menssagem(mensagem):
    send(mensagem, broadcast=True)

# criar a nossa primeira pagina = primeira rota
@app.route("/")
def homepage():
    return render_template("homepage.html")

# roda o nosso aplicativo
Socketio.run(app, host="192.168.0.35")
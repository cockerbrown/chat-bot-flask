from nltk.chat.util import Chat, reflections
from bot.keys import pares
from flask import Flask, render_template, request
import os

app = Flask(__name__)
app.secret_key = os.urandom(23)

lista = []

@app.route('/clear')
def clear():
    lista.clear()
    return render_template("chat.html")

@app.before_first_request
def reque():
    if len(lista):
        lista.clear()

@app.route('/', methods=['GET', 'POST'])
def index_bot():
    if request.method == 'POST':
        msj = request.form['mensaje']
        chat = Chat(pares, reflections)
        if chat.respond(msj) != None:
            mensaje = chat.respond(msj)
            lista.append(msj)
            lista.append(mensaje)
            return render_template('chat.html', lista=lista)
    return render_template("chat.html")

if __name__=="__main__":
    app.run(debug=True)

  
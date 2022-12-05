from flask import Flask, render_template, request, redirect, url_for, flash
import webview
import os
import datetime
from functools import wraps
from itertools import product
from time import time
from hashlib import sha256

app = Flask(__name__)


window = webview.create_window('Brutus', app, height=700)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

chars  = [chr(i) for i in range(97, 123)]
chars += [chr(i) for i in range(48, 58)]
# chars += [chr(i) for i in range(65, 91)]
# chars  = [chr(i) for i in range(32, 127)]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        password = request.form['password']
        achou = brute_force(password, len(password))

        if achou != 0:
            print(achou)
            return redirect(url_for('achou', password=achou))
        else:
            return redirect(url_for('naoachou'))

    return render_template("index.html")


@app.route("/achou", methods=["GET", "POST"])
def achou():  
    password = request.args.get('password')
    return render_template("achou.html", password=password)


@app.route("/naoachou", methods=["GET", "POST"])
def naoachou():
    return render_template("naoachou.html")


def brute_force(password, lenPass):
    inicio_execucao = time()
    password = tuple(password)

    for length in range(lenPass, lenPass + 1):
        for p in product(chars, repeat=length):
            if p == password:
                fim_execucao = time()
                tempo_execucao = fim_execucao - inicio_execucao
                print ('Senha encontrada é "{}". Tempo de execucao: "{}"'.format(p, tempo_execucao))
                if tempo_execucao < 30:
                    p = ''.join(p)
                    return p
                else:
                    return 0

if __name__ == "__main__":
    webview.start()

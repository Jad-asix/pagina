from flask import Flask
from flask import render_template
from flask import request

from flask import Flask, redirect, url_for, request

app = Flask(__name__)

# Diccionario con nombres y correos asociados
correos = {
    "Mercedes": "mcast386@xtec.cat",
    "Rayane": "rayane@rayane.sa",
    "Mohamed": "moha@gmail.com",
    "Jad": "jad@gmail.com",
    "Oriol": "joam@gmail.com",
    "Elias": "hola123@gmail.com",
    "Armau": "arnau@gmail.com",
    "Asdrúbal": "asdrubal@gmail.com",
    "Adrian": "pedrosanchez@asix2.com",
    "Eric": "eric@gmail.com",
    "Emma": "pacosanz@gmail.com",
    "nishwan": "nishwan@gmail.com",
    "Javi": "javi@gmail.com",
    "Novel": "novelferreras49@gmail.com",
    "Bruno": "elcigala@gmail.com",
    "David": "argentino@gmail.com",
    "Judit": "judit@gmail.com",
    "Joao": "joao@gmail.com",
    "Laura": "laura@gmail.com",
    "enrico": "123@gmail.com",
    "Joel": "joelcobre@gmail.com",
    "Aaron": "aaron@gmail.com",
    "Moad": "moad@gmail.com"
}


@app.route('/getmail', methods=['POST', 'GET'])
def getmail():
    if request.method == 'POST':
        nombre = request.form['name']
        correo = correos.get(nombre, "no encontrado")
        return  render_template('resultgetmail.html',nombre=nombre, correo=correo)
        
    else:
        return render_template('formgetmail.html')


@app.route('/add', methods=['POST', 'GET'])
def adduser():
    if request.method == 'POST':
        nombre = request.form['name']
        correo = request.form['email']

        if nombre and correo:
            correos[nombre] = correo
            return redirect(url_for('getmail'))
        else:
            return "Error: Por favor, ingresa nombre y correo."

    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)
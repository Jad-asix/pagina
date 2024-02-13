from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Establecemos la conexión a la base de datos MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="asix2",
    password="",
    database="asix2"
)
cursor = conn.cursor()

# Ruta para obtener el correo electrónico
@app.route('/getmail', methods=['POST', 'GET'])
def getmail():
    if request.method == 'POST':
        nombre = request.form['username']
        correo = getmaildb(nombre)
        return render_template('resultgetmail.html', nombre=nombre, correo=correo)
    else:
        return render_template('Buscar.html')

# Función para obtener el correo electrónico desde la base de datos
def getmaildb(nombre):
    cursor.execute("SELECT email FROM usuarios WHERE nombre=%s", (nombre,))
    result = cursor.fetchone()
    if result:
        return result[0]
    return "no encontrado"

# Ruta para agregar un nuevo usuario
@app.route('/addmail', methods=['POST', 'GET'])
def addmail():
    if request.method == 'POST':
        nombre = request.form['name']
        correo = request.form['email']

        if nombre and correo:
            addmaildb(nombre, correo)
            return redirect(url_for('getmail'))
        else:
            return "Error: Por favor, ingresa nombre y correo."

    return render_template('addmail.html', correu="hola", nom="pp", result_msg="error")

# Función para agregar un nuevo usuario a la base de datos
def addmaildb(nombre, email):
    cursor.execute("INSERT INTO usuarios (nombre, email) VALUES (%s, %s)", (nombre, email))
    conn.commit()

if __name__ == '__main__':
    app.run(debug=True)


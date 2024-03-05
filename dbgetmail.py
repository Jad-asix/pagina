from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector

app = Flask(__name__)

app.secret_key = 'your_secret_key'  # Clave secreta para las sesiones

# Establecemos la conexión a la base de datos MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="asix2",
    password="",
    database="asix2"
)
cursor = conn.cursor()

@app.route('/', methods=['POST', 'GET'])
def inicio():
    mostrar_nav = False  # Define si el nav debe mostrarse en la página de inicio
    return render_template('inicio.html', mostrar_nav=mostrar_nav)



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
    cursor.execute("INSERT INTO usuarios1 (nombre, email) VALUES (%s, %s)", (nombre, email))
    conn.commit()


# Ruta para el login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nombre = request.form['username']
        password = request.form['password']
        if authenticate_user(nombre, password):
            session['username'] = nombre
            return redirect(url_for('nav'))
        else:
            return "Credenciales incorrectas. Por favor, inténtalo de nuevo."
    return render_template('login.html')

@app.route('/nav', methods=['GET', 'POST'])
def nav():
    return render_template('nav.html')

@app.route('/proyectos', methods=['GET', 'POST'])
def proyectos():
    return render_template('proyectos.html')

# Función para autenticar al usuario
def authenticate_user(nombre, password):
    cursor.execute("SELECT * FROM usuarios1 WHERE nombre = %s AND password = %s", (nombre, password))
    user = cursor.fetchone()
    if user:
        return True
    else:
        return False

# Ruta para cerrar sesión
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('nav'))




# Ruta para el registro de un nuevo usuario
@app.route('/registro', methods=['POST', 'GET'])
def registro():
    if request.method == 'POST':
        nombre = request.form['name']
        correo = request.form['email']
        password = request.form['password']  # Agregar campo de contraseña

        if nombre and correo and password:  # Verificar que todos los campos estén presentes
            agregar_usuario(nombre, correo, password)  # Llamada a la función para agregar usuario
            return redirect(url_for('getmail'))
        else:
            return "Error: Por favor, ingresa nombre, correo y contraseña."

    return render_template('registro.html')  # Renderizar el formulario de registro

# Función para agregar un nuevo usuario a la base de datos
def agregar_usuario(nombre, email, password):
    cursor.execute("INSERT INTO usuarios1 (nombre, email, password) VALUES (%s, %s, %s)", (nombre, email, password))
    conn.commit()

if __name__ == '__main__':
    app.run(debug=True)


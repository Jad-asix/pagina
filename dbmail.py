import mysql.connector

# Establecemos la conexión a la base de datos MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="asix2",
    password="",
    database="asix2"
)

# Creamos un cursor para ejecutar comandos SQL
cursor = conn.cursor()

#CONSTANTES para los resultados de las funciones
NOTROBAT = "NOTROBAT"
AFEGIT = "AFEGIT"
MODIFICAT = "MODIFICAT"
JAEXISTEIX = "JAEXISTEIX"

# Función getmaildb que recibe el nombre como parámetro y retorna el email
# Si no lo encuentra, retorna el string "NOTROBAT"
def getmaildb(nombre):
    c.execute("SELECT email FROM usuarios WHERE nombre=?", (nombre,))
    result = c.fetchone()
    if result:
        return result[0]
    return NOTROBAT

# Función addmaildb que recibe el nombre y el email como parámetros, y los agrega a la base de datos
# Si ya existe, retorna el string "JAEXISTEIX"
# Cuando todo va bien, retorna "AFEGIT"
# Si el parámetro modif es True y ya existe pero es diferente, lo modifica y retorna "MODIFICAT"
def addmaildb(nombre, email, modif=False):
    old_email = getmaildb(nombre)
    if old_email == NOTROBAT:
        c.execute("INSERT INTO usuarios VALUES (?, ?)", (nombre, email))
        conn.commit()
        return AFEGIT
    elif (old_email != email and modif):
        c.execute("UPDATE usuarios SET email=? WHERE nombre=?", (email, nombre))
        conn.commit()
        return MODIFICAT
    return JAEXISTEIX

# Ejemplo de uso:
print(addmaildb("Mercedes", "mcast386@xtec.cat"))
print(addmaildb("Mercedes", "newemail@example.com", modif=True))
print(addmaildb("Carlos", "carlos@example.com"))
print(getmaildb("Mercedes"))
print(getmaildb("Carlos"))

# Cerramos la conexión a la base de datos al finalizar
conn.close()

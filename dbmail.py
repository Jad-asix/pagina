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

# CONSTANTES para los resultados de las funciones
NOTROBAT = "NOTROBAT"
AFEGIT = "AFEGIT"
MODIFICAT = "MODIFICAT"
JAEXISTEIX = "JAEXISTEIX"

# Función getmaildb que recibe el nombre como parámetro y retorna el email
# Si no lo encuentra, retorna el string "NOTROBAT"
def getmaildb(nombre):
    try:
        cursor.execute("SELECT email FROM usuarios WHERE nombre=%s", (nombre,))
        result = cursor.fetchone()
        if result:
            return result[0]
        return NOTROBAT
    except mysql.connector.Error as err:
        print("Error de base de datos:", err)
        return None

# Función addmaildb que recibe el nombre y el email como parámetros, y los agrega a la base de datos
# Si ya existe, retorna el string "JAEXISTEIX"
# Cuando todo va bien, retorna "AFEGIT"
# Si el parámetro modif es True y ya existe pero es diferente, lo modifica y retorna "MODIFICAT"
def addmaildb(nombre, email, modif=False):
    old_email = getmaildb(nombre)
    if old_email == NOTROBAT:
        try:
            cursor.execute("INSERT INTO usuarios (nombre, email) VALUES (%s, %s)", (nombre, email))
            conn.commit()
            return AFEGIT
        except mysql.connector.Error as err:
            print("Error de base de datos:", err)
            return None
    elif (old_email != email and modif):
        try:
            cursor.execute("UPDATE usuarios SET email=%s WHERE nombre=%s", (email, nombre))
            conn.commit()
            return MODIFICAT
        except mysql.connector.Error as err:
            print("Error de base de datos:", err)
            return None
    return JAEXISTEIX

# Ejemplo de uso:
print(addmaildb("Mercedes", "mcast386@xtec.cat"))
print(addmaildb("Mercedes", "newemail@example.com", modif=True))
print(addmaildb("Carlos", "carlos@example.com"))
print(getmaildb("Mercedes"))
print(getmaildb("Carlos"))

# Cerramos el cursor y la conexión a la base de datos al finalizar
cursor.close()
conn.close()

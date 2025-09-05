import psycopg2

# Para conectar con datos PostgreSQL (del docker-compose)
conn = psycopg2.connect(
    host="db",
    database="testdb",
    user="postgres",
    password="postgres"
)

#Crear cursor para ejecutar los queries en la DB
cur = conn.cursor()

#Crear tabla mensajes
cur.execute("CREATE TABLE IF NOT EXISTS messages (id SERIAL PRIMARY KEY, text VARCHAR(255));")
#insertar registro en la tabla 
cur.execute("INSERT INTO messages (text) VALUES ('Hello from Docker Compose!');")
#confirmar los cambios
conn.commit()


#Consultar los registros e imprimir en terminal
cur.execute("SELECT * FROM messages;")
rows = cur.fetchall()
for row in rows:
    print(row)

#Cerrar conexion de base de datos
cur.close()
conn.close()
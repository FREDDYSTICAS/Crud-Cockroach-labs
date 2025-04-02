import psycopg2

# Configuración de conexión a CockroachDB
DB_URL = "postgresql://freddysticas:a8cumCyj7qV0WaU3Tp34oQ@freddy-castro-8236.j77.aws-us-east-1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full"

# Variable global para controlar si ya se imprimió el mensaje de conexión exitosa
conexion_inicializada = False

def conectar():
    global conexion_inicializada
    try:
        conn = psycopg2.connect(DB_URL)
        if not conexion_inicializada:
            print("✅ Conexión exitosa a la base de datos")
            conexion_inicializada = True  # Se marca como inicializada
        return conn
    except Exception as e:
        print("❌ Error de conexión:", e)
        return None

# Ejecutar la conexión para probar solo cuando el script se ejecuta directamente
if __name__ == "__main__":
    conectar()


from database import conectar

def crear_tabla():
    """Crea la tabla Usuarios si no existe"""
    conn = conectar()
    if conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS Usuarios (
                    id SERIAL PRIMARY KEY,
                    nombre TEXT NOT NULL,
                    identificacion VARCHAR(20) UNIQUE NOT NULL,
                    profesion TEXT NOT NULL
                )
            """)
            conn.commit()
        conn.close()

# Ejecutar la función para crear la tabla
crear_tabla()

def insertar_datos_prueba():
    """Inserta 10 usuarios de prueba con ID manualmente del 1 al 10 si la tabla está vacía"""
    conn = conectar()
    if conn:
        with conn.cursor() as cur:
            cur.execute("SELECT COUNT(*) FROM Usuarios")
            count = cur.fetchone()[0]
            if count == 0:  # Solo inserta si no hay registros
                cur.execute("""
                    INSERT INTO Usuarios (id, nombre, identificacion, profesion) VALUES
                    (1, 'Carlos Pérez', '100123456', 'Ingeniero'),
                    (2, 'María Gómez', '100654321', 'Doctora'),
                    (3, 'Juan Rodríguez', '100789012', 'Abogado'),
                    (4, 'Ana Torres', '101234567', 'Arquitecta'),
                    (5, 'Pedro Ramírez', '101987654', 'Profesor'),
                    (6, 'Laura Castillo', '102345678', 'Enfermera'),
                    (7, 'José Sánchez', '102876543', 'Chef'),
                    (8, 'Fernanda López', '103456789', 'Diseñadora'),
                    (9, 'Daniel Ortega', '103987651', 'Contador'),
                    (10, 'Elena Ríos', '104567890', 'Psicóloga')
                """)
                conn.commit()
        conn.close()

# Ejecutar funciones
crear_tabla()
insertar_datos_prueba()






"""from database import conectar

def eliminar_tabla():
    #Elimina la tabla Usuarios si existe y muestra un mensaje de confirmación
    conn = conectar()
    if conn:
        with conn.cursor() as cur:
            cur.execute("DROP TABLE IF EXISTS Usuarios CASCADE")
            conn.commit()
            print("✅ La tabla 'Usuarios' ha sido eliminada correctamente.")
        conn.close()

# Ejecutar la función para borrar la tabla
eliminar_tabla()
"""

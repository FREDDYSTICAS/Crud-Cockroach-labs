from database import conectar

def insertar_usuario(id, nombre, identificacion, profesion):
    """Inserta un nuevo usuario en la base de datos con un ID manual"""
    conn = conectar()
    if conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO Usuarios (id, nombre, identificacion, profesion) VALUES (%s, %s, %s, %s)", 
                        (id, nombre, identificacion, profesion))
            conn.commit()
        conn.close()

def obtener_usuarios():
    """Obtiene todos los usuarios"""
    conn = conectar()
    if conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM Usuarios ORDER BY id")
            usuarios = cur.fetchall()
        conn.close()
        return usuarios

def actualizar_usuario(id, nombre=None, identificacion=None, profesion=None):
    """Actualiza solo los campos proporcionados de un usuario existente por su ID."""
    conn = conectar()
    if conn:
        with conn.cursor() as cur:
            campos = []
            valores = []

            if nombre:
                campos.append("nombre=%s")
                valores.append(nombre)
            if identificacion:
                campos.append("identificacion=%s")
                valores.append(identificacion)
            if profesion:
                campos.append("profesion=%s")
                valores.append(profesion)

            if campos:  # Solo ejecutar si hay algo que actualizar
                query = f"UPDATE Usuarios SET {', '.join(campos)} WHERE id=%s"
                valores.append(id)
                cur.execute(query, valores)
                conn.commit()
        conn.close()

def eliminar_usuario(id):
    """Elimina un usuario por ID"""
    conn = conectar()
    if conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM Usuarios WHERE id=%s", (id,))
            conn.commit()
        conn.close()

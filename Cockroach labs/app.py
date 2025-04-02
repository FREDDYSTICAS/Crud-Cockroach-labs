import tkinter as tk
from tkinter import messagebox
from crud import insertar_usuario, obtener_usuarios, actualizar_usuario, eliminar_usuario

# Colores y estilos
BG_COLOR = "#2C3E50"
BTN_COLOR = "#27AE60"
BTN_DELETE_COLOR = "#E74C3C"
BTN_SHOW_COLOR = "#2980B9"
TEXT_COLOR = "#ECF0F1"

# Función para refrescar la interfaz
def refrescar():
    entry_id.delete(0, tk.END)
    entry_nombre.delete(0, tk.END)
    entry_identificacion.delete(0, tk.END)
    entry_profesion.delete(0, tk.END)
    lista_usuarios.delete(0, tk.END)

# Funciones CRUD
def agregar():
    try:
        id_usuario = int(entry_id.get())
        nombre = entry_nombre.get()
        identificacion = entry_identificacion.get()
        profesion = entry_profesion.get()
        
        if id_usuario and nombre and identificacion and profesion:
            insertar_usuario(id_usuario, nombre, identificacion, profesion)
            messagebox.showinfo("✅ Éxito", "Usuario agregado correctamente")
            refrescar()
        else:
            messagebox.showwarning("⚠️ Error", "Todos los campos son obligatorios")
    except ValueError:
        messagebox.showwarning("⚠️ Error", "El ID debe ser un número entero")

def actualizar():
    try:
        id_usuario = int(entry_id.get())
        nombre = entry_nombre.get()
        identificacion = entry_identificacion.get()
        profesion = entry_profesion.get()
        
        if id_usuario:
            actualizar_usuario(id_usuario, nombre if nombre else None, 
                               identificacion if identificacion else None, 
                               profesion if profesion else None)
            messagebox.showinfo("✅ Éxito", "Usuario actualizado correctamente")
            refrescar()
        else:
            messagebox.showwarning("⚠️ Error", "El ID es obligatorio para actualizar")
    except ValueError:
        messagebox.showwarning("⚠️ Error", "El ID debe ser un número entero")

def mostrar_lista():
    lista_usuarios.delete(0, tk.END)
    for usuario in obtener_usuarios():
        lista_usuarios.insert(tk.END, usuario)

def eliminar():
    seleccion = lista_usuarios.curselection()
    if seleccion:
        id_usuario = lista_usuarios.get(seleccion[0])[0]
        eliminar_usuario(id_usuario)
        mostrar_lista()
        messagebox.showinfo("✅ Éxito", "Usuario eliminado correctamente")
    else:
        messagebox.showwarning("⚠️ Error", "Selecciona un usuario para eliminar")

# Configuración de la ventana principal
root = tk.Tk()
root.title("📋 Gestión de Usuarios")
root.configure(bg=BG_COLOR)

# Botón de refrescar
btn_refrescar = tk.Button(root, text="🔄", bg=BTN_SHOW_COLOR, fg=TEXT_COLOR, command=refrescar)
btn_refrescar.grid(row=0, column=0, sticky='w', padx=5, pady=5)

# Etiquetas y entradas
tk.Label(root, text="ID:", fg=TEXT_COLOR, bg=BG_COLOR).grid(row=1, column=0)
entry_id = tk.Entry(root)
entry_id.grid(row=1, column=1)

tk.Label(root, text="Nombre:", fg=TEXT_COLOR, bg=BG_COLOR).grid(row=2, column=0)
entry_nombre = tk.Entry(root)
entry_nombre.grid(row=2, column=1)

tk.Label(root, text="Identificación:", fg=TEXT_COLOR, bg=BG_COLOR).grid(row=3, column=0)
entry_identificacion = tk.Entry(root)
entry_identificacion.grid(row=3, column=1)

tk.Label(root, text="Profesión:", fg=TEXT_COLOR, bg=BG_COLOR).grid(row=4, column=0)
entry_profesion = tk.Entry(root)
entry_profesion.grid(row=4, column=1)

# Botones
btn_agregar = tk.Button(root, text="➕ Agregar", bg=BTN_COLOR, fg=TEXT_COLOR, command=agregar)
btn_agregar.grid(row=5, column=0)

btn_actualizar = tk.Button(root, text="🔄 Actualizar", bg=BTN_COLOR, fg=TEXT_COLOR, command=actualizar)
btn_actualizar.grid(row=5, column=1)

btn_mostrar = tk.Button(root, text="📋 Mostrar Usuarios", bg=BTN_SHOW_COLOR, fg=TEXT_COLOR, command=mostrar_lista)
btn_mostrar.grid(row=6, column=0, columnspan=2)

# Lista de usuarios (vacía al inicio)
lista_usuarios = tk.Listbox(root, width=50, height=10)
lista_usuarios.grid(row=7, column=0, columnspan=2)

btn_eliminar = tk.Button(root, text="🗑️ Eliminar", bg=BTN_DELETE_COLOR, fg=TEXT_COLOR, command=eliminar)
btn_eliminar.grid(row=8, column=0, columnspan=2)

root.mainloop()

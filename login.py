from app.bbdd.conexion import getConexion
import bcrypt
import tkinter as tk
from tkinter import messagebox

def init_db():
    cone = getConexion()
    cursor = cone.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS empleados (
    id VARCHAR(20) PRIMARY KEY,
    nombre VARCHAR(100),
    password_hash BLOB
    )
    """)
    cone.commit()
    cone.close()

def crear_usuario(id_emp, nombre, pw):
    pw_hash = bcrypt.hashpw(pw.encode(), bcrypt.gensalt())
    cone = getConexion()
    cursor = cone.cursor()
    cursor.execute("INSERT INTO empleados VALUES (%s, %s, %s)", (id_emp, nombre, pw_hash))
    cone.commit()
    cone.close()

def autenticar(id_emp, pw):
    cone = getConexion()
    cursor = cone.cursor()
    cursor.execute("SELECT password_hash FROM empleados WHERE id=%s", (id_emp,))
    row = cursor.fetchone()
    cone.close()
    if not row:
       return False
    return bcrypt.checkpw(pw.encode(), row[0])

class Login:
    def __init__(self, root):
        root.title("Login Empresa")
        root.geometry("280x200")

        tk.Label(root, text="ID Empleado:").pack(pady=5)
        self.e_id = tk.Entry(root)
        self.e_id.pack()

        tk.Label(root, text="Contrasenia:").pack(pady=5)
        self.e_pw = tk.Entry(root, show="*")
        self.e_pw.pack()

        tk.Button(root, text="Ingresar", command=self.login).pack(pady=10)
        tk.Button(root, text="Registrar", command=self.register).pack()

        self.root = root

    def login(self):
        if autenticar(self.e_id.get(), self.e_pw.get()):
            messagebox.showinfo("OK", "Acceso concedido")
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")

    def register(self):
        crear_usuario(self.e_id.get(), "SinNombre", self.e_pw.get())
        messagebox.showinfo("OK", "Usuario registrado")

root = tk.Tk()
app = Login(root)
root.mainloop()

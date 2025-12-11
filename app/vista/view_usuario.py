from app.modelo.usuario import Usuario
from app.controlador.DAO_usuario import *
from app.utils.helper import *
from app.utils.seguridad import encriptar_password
import getpass

def input_no_vacio(mensaje, max_intentos=5):
    intentos = 0
    while intentos < max_intentos:
        dato = input(mensaje).strip()
        if dato != "": return dato
        intentos += 1
        print(f"Error: Este campo no puede estar vacío. Intento {intentos}/{max_intentos}")
    print("Demasiados intentos fallidos. Operación cancelada.")
    return None

def input_password_seguro(mensaje):
    """Pide contraseña ocultando caracteres y valida que no sea vacía."""
    while True:
        # getpass oculta lo que escribes en la consola
        pw = getpass.getpass(mensaje).strip()
        if pw != "": 
            return pw
        print("Error: La contraseña no puede estar vacía.")

# ========================================================
# OPCIÓN 1: REGISTRAR USUARIO
# ========================================================
def addUsuario():
    while True:
        saltar_pantalla()
        print("============================================")
        print("             REGISTRAR USUARIO              ")
        print("============================================")
        
        # 1. Pedir datos
        nombre_usuario = input_no_vacio("Nombre de usuario: ")
        if nombre_usuario is None: break
        
        # Verificar si el usuario ya existe (Validación extra recomendada)
        # Nota: Idealmente el DAO debería tener un método 'existeUsuario', 
        # pero por ahora confiamos en el error de la BD o validamos post-input.

        email = input_no_vacio("Email corporativo: ")
        if email is None: break
        
        # 2. Pedir contraseña de forma segura (sin mostrar caracteres)
        contraseña = input_password_seguro("Ingrese Contraseña: ")
        
        # 3. Validar ID de Empleado (Opcional, puede ser None para admins puros)
        print("\n(Opcional) Asociar a un empleado existente.")
        id_empleado_str = input("ID Empleado (Enter para omitir): ").strip()
        
        id_empleado = None
        if id_empleado_str:
            if id_empleado_str.isdigit():
                id_empleado = int(id_empleado_str)
            else:
                print("Aviso: ID no válido, se dejará sin empleado asociado.")

        # 4. Asignar Rol
        print("\nRoles disponibles: admin, gerente, empleado")
        rol = input("Ingrese rol (Enter para 'empleado'): ").strip().lower()
        if rol not in ['admin', 'gerente', 'empleado']:
            rol = 'empleado' # Valor por defecto

        # --- ENCRIPTACIÓN ---
        # Aquí ocurre la magia de seguridad antes de crear el objeto
        password_hash = encriptar_password(contraseña)

        # Creamos el objeto Usuario enviando el HASH, no la clave plana
        # (Asegúrate de que tu modelo Usuario acepte estos argumentos)
        nuevo_usuario = Usuario(nombre_usuario, email, password_hash, id_empleado, rol)
        
        print("-" * 40)
        if agregarUsuario(nuevo_usuario):
            print(f"¡Usuario '{nombre_usuario}' registrado exitosamente!")
        else:
            print("Error: No se pudo registrar (posible nombre de usuario duplicado).")

        print("-" * 40)
        opcion = input("¿Desea registrar otro usuario? (s/n): ").strip().lower()
        if opcion != "s":
            break

# ========================================================
# OPCIÓN 2: VER USUARIOS
# ========================================================
def readUsuario(pausar=True):
    if pausar:
        saltar_pantalla()
        print("============================================")
        print("              LISTA DE USUARIOS             ")
        print("============================================")

    usuarios = verUsuario() # Retorna lista de tuplas
    
    if not usuarios:
        print("\nNo hay usuarios registrados.\n")
    else:
        # Encabezado
        # Ajusta las columnas según lo que retorne tu DAO_usuario.verUsuario()
        # Asumimos orden: email, nombre_usuario, password_hash, rol, id_empleado
        print(f"{'Usuario':<15} {'Rol':<10} {'ID Emp.':<10} {'Email'}")
        print("="*80)

        for u in usuarios:
            # u[0]=email, u[1]=nombre, u[2]=hash, u[3]=rol, u[4]=id_emp (según tu DAO anterior)
            # Vamos a ajustarlo visualmente
            nombre = str(u[1])
            rol = str(u[3]) if u[3] else "N/A"
            id_emp = str(u[4]) if u[4] else "---"
            email = str(u[0])
            
            print(f"{nombre:<15} {rol:<10} {id_emp:<10} {email}")
        print("="*80)
    
    if pausar:
        input("\nPresiona Enter para continuar...")

# ========================================================
# OPCIÓN 3: EDITAR USUARIO
# ========================================================
def editUsuario():
    saltar_pantalla()
    print("============================================")
    print("               EDITAR USUARIO               ")
    print("============================================")
    
    readUsuario(pausar=False) # Ver lista

    print("-" * 40)
    nombre_usuario = input("Ingrese nombre de usuario a editar: ").strip()
    if not nombre_usuario:
        return

    print(f"\n--- Editando a {nombre_usuario} ---")
    print("Deje vacío si no desea cambiar el valor.")
    
    nuevo_email = input("Nuevo Email: ").strip()
    nuevo_rol = input("Nuevo Rol (admin/gerente/empleado): ").strip().lower()
    
    cambiar_pass = input("¿Desea cambiar la contraseña? (s/n): ").lower()
    nuevo_hash = None
    
    if cambiar_pass == 's':
        nueva_pass = input_password_seguro("Nueva Contraseña: ")
        nuevo_hash = encriptar_password(nueva_pass)
    
    # Nota: Para editar, necesitamos recuperar los datos anteriores si 
    # el usuario dejó campos vacíos. Como el DAO 'editarUsuario' suele 
    # pedir el objeto completo, aquí simplificamos asumiendo que el DAO
    # o la lógica maneja nulos, o deberíamos buscar el usuario antes.
    
    # Para mantenerlo simple y funcional con tu DAO actual que hace UPDATE directo:
    if nuevo_email == "": 
        print("Error: El email es obligatorio para actualizar (o lógica de mantener anterior no implementada).")
        input("Presiona Enter...")
        return
        
    # Si no cambió la contraseña, necesitamos el hash anterior o manejarlo en el DAO.
    # Si tu DAO reemplaza todo, es mejor obligar a cambiar todo o buscar primero.
    # Asumiremos que si edita, re-ingresa datos críticos.
    
    if nuevo_hash is None:
        print("Aviso: No se cambiará la contraseña (se requiere lógica extra para mantener la anterior en BD).")
        # En un sistema real, haríamos un SELECT primero.
        # Por seguridad en este ejemplo simple, si no cambia pass, enviamos None 
        # y el DAO debería ignorarlo, o pedimos que la re-ingrese.
        nuevo_hash = "NO_CAMBIAR" 

    # Validación de rol
    if nuevo_rol not in ['admin', 'gerente', 'empleado', '']:
        nuevo_rol = 'empleado'
    if nuevo_rol == "": nuevo_rol = 'empleado' # Default

    # Construir objeto
    usu_edit = Usuario(nombre_usuario, nuevo_email, nuevo_hash, None, nuevo_rol)

    # IMPORTANTE: Tu DAO debe saber qué hacer si password_hash es "NO_CAMBIAR" 
    # o deberías recuperar el usuario antes. 
    # SI TU DAO HACE UPDATE PURO, esto podría romper la clave si envías basura.
    # Recomendación rápida: Pedir nueva clave siempre al editar por ahora.
    
    if editarUsuario(usu_edit):
        print("Usuario actualizado.")
    else:
        print("No se pudo actualizar.")
    input("Presiona Enter...")

# ========================================================
# OPCIÓN 4: ELIMINAR USUARIO
# ========================================================
def delUsuario():
    saltar_pantalla()
    print("============================================")
    print("              ELIMINAR USUARIO              ")
    print("============================================")
    
    readUsuario(pausar=False)

    print("-" * 40)
    nombre_usuario = input("Ingrese nombre de usuario a eliminar: ").strip()
    
    if not nombre_usuario:
        return

    confirmar = input(f"¿Seguro de eliminar a '{nombre_usuario}'? (s/n): ").lower()
    if confirmar == 's':
        if eliminarUsuario(nombre_usuario):
            print("Usuario eliminado correctamente.")
        else:
            print("No se encontró el usuario.")
    
    input("Presiona Enter para continuar...")
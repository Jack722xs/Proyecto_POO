from app.modelo.empleado import empleado
from app.controlador.DAO_empleado import *
from app.utils.helper import *

def input_no_vacio(mensaje, max_intentos=5):
    intentos = 0
    while intentos < max_intentos:
        dato = input(mensaje).strip()
        if dato != "": return dato
        intentos += 1
        print(f"Error: Este campo no puede estar vacío. Intento {intentos}/{max_intentos}")
    print("Demasiados intentos fallidos. Operación cancelada.")
    return None

# ========================================================
# OPCIÓN 1: AGREGAR EMPLEADO
# ========================================================
def addEmpleado():
    while True:
        saltar_pantalla()
        print("============================================")
        print("             AGREGAR EMPLEADO               ")
        print("============================================")
        
        # Validación de ID numérico
        val_id = input_no_vacio("Ingrese ID (Numérico): ")
        if val_id is None: break
        
        if not val_id.isdigit():
            print("Error: El ID debe ser un número entero.")
            input("Presiona Enter para reintentar...")
            continue
            
        id_empleado = int(val_id)
        
        # Resto de datos
        nombre = input_no_vacio("Nombre: ")
        if nombre is None: break
        
        apellido = input_no_vacio("Apellido: ")
        if apellido is None: break
        
        direccion = input_no_vacio("Dirección: ")
        if direccion is None: break
        
        email = input_no_vacio("Email: ")
        if email is None: break
        
        # Validación básica de salario
        salario_str = input_no_vacio("Salario: ")
        if salario_str is None: break
        try:
            salario = float(salario_str)
        except ValueError:
            print("Error: El salario debe ser un número.")
            input("Presiona Enter para reintentar...")
            continue

        telefono = input("Teléfono (opcional): ").strip()
        if telefono == "": telefono = None

        # Creación del objeto (es_gerente por defecto False, se asigna en otra opción)
        emp = empleado(id_empleado, nombre, apellido, direccion, email, salario, telefono)
        
        print("-" * 40)
        if agregarEmpleado(emp):
            print("¡Empleado agregado correctamente!")
        else:
            print("Error: No se pudo agregar (posible ID duplicado).")

        print("-" * 40)
        opcion = input("¿Desea agregar otro empleado? (s/n): ").strip().lower()
        if opcion != "s":
            break

# ========================================================
# OPCIÓN 2: EDITAR EMPLEADO
# ========================================================
def editEmpleado():
    saltar_pantalla()
    print("============================================")
    print("              EDITAR EMPLEADO               ")
    print("============================================")
    
    empleados_actuales = verEmpleado()
    if not empleados_actuales:
        print("No hay empleados registrados para editar.")
        input("Presiona Enter para continuar...")
        return

    print(f"{'ID':<12} {'Nombre':<15} {'Apellido':<15}")
    print("-" * 45)
    lista_ids = []
    for e in empleados_actuales:
        e_id = str(e[0])
        lista_ids.append(e_id)
        print(f"{e_id:<12} {e[1]:<15} {e[2]:<15}")
    print("=" * 80)

    id_empleado = input("\nIngrese ID del empleado a editar: ").strip()
    
    if not id_empleado:
        print("Error: El ID no puede estar vacío.")
        input("Presiona Enter para continuar...")
        return

    if id_empleado not in lista_ids:
        print(f"\nError: El empleado con ID '{id_empleado}' NO existe.")
        input("Presiona Enter para continuar...")
        return

    print(f"\n--- Editando datos de {id_empleado} ---")
    
    nombre = input_no_vacio("Nuevo Nombre: ")
    if nombre is None: return
    
    apellido = input_no_vacio("Nuevo Apellido: ")
    if apellido is None: return
    
    direccion = input_no_vacio("Nueva Dirección: ")
    if direccion is None: return
    
    email = input_no_vacio("Nuevo Email: ")
    if email is None: return
    
    salario_str = input_no_vacio("Nuevo Salario: ")
    if salario_str is None: return
    try:
        salario = float(salario_str)
    except ValueError:
        print("Error: Salario inválido.")
        input("Presiona Enter...")
        return
        
    telefono = input("Nuevo Teléfono (opcional): ").strip()
    if telefono == "": telefono = None

    # Objeto actualizado
    emp = empleado(id_empleado, nombre, apellido, direccion, email, salario, telefono)

    print("-" * 40)
    if editarEmpleado(emp):
        print("Empleado actualizado correctamente.")
    else:
        print("Error: No se pudo actualizar el registro.")
    
    input("Presiona Enter para continuar...")

# ========================================================
# OPCIÓN 3: ELIMINAR EMPLEADO
# ========================================================
def delEmpleado():
    saltar_pantalla()
    print("============================================")
    print("             ELIMINAR EMPLEADO              ")
    print("============================================")
    
    readEmpleado(pausar=False)

    print("-" * 40)
    id_empleado = input("Ingrese ID del empleado a eliminar: ").strip()
    if not id_empleado:
        print("Error: ID vacío.")
        input("Presiona Enter...")
        return

    confirmacion = input(f"¿Está seguro de eliminar al empleado {id_empleado}? (s/n): ").lower()
    if confirmacion == 's':
        if eliminarEmpleado(id_empleado):
            print("Empleado eliminado correctamente.")
        else:
            print("Error: No se encontró el ID o hubo un problema en la BD.")
    else:
        print("Operación cancelada.")
        
    input("Presiona Enter para continuar...")    

# ========================================================
# OPCIÓN 4: VER EMPLEADOS
# ========================================================
def readEmpleado(pausar=True):
    if pausar:
        saltar_pantalla()
        print("============================================")
        print("             LISTA DE EMPLEADOS             ")
        print("============================================")

    empleados = verEmpleado()
    
    if not empleados:
        print("\nNo hay empleados registrados.\n")
    else:
        # Encabezado formateado
        print(f"{'ID':<12} {'Nombre':<12} {'Apellido':<12} {'Email':<25} {'Salario':<10} {'Gerente'}")
        print("="*85)

        for emp in empleados:
            # Índices basados en la consulta SELECT o estructura de tabla
            # Ajustar según tu DAO (0:id, 1:nombre, 2:apellido, 4:email, 5:salario, 7:es_gerente)
            id_emp = str(emp[0])
            nombre = str(emp[1])
            apellido = str(emp[2])
            email = str(emp[4])
            salario = str(emp[5])
            
            # Manejo seguro del booleano gerente (puede venir como 1/0 o True/False)
            es_gerente = "Si" if emp[7] else "No"

            print(f"{id_emp:<12} {nombre:<12} {apellido:<12} {email:<25} {salario:<10} {es_gerente}")
    
        print("="*85)
    
    if pausar:
        input("\nPresiona Enter para continuar...")
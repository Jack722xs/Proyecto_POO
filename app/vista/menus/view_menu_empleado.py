import app.sesion.sesion as sesion
from app.vista.view_registro_tiempo import addRegistroTiempo, verRegistrosEmpleado
from app.controlador.sub_controlador.DAO_empleado_proyecto import verProyectosDeEmpleado
from app.controlador.DAO_empleado import verEmpleadoPorID
from app.utils.helper import *

def menu_empleado():
    while True:
        saltar_pantalla()
        print("""
============================================
               MENÚ EMPLEADO
============================================
1. Ver mis datos                           =
2. Ver mis proyectos                       =
3. Registrar horas trabajadas              =
4. Ver mis registros de horas              =
============================================
5. Salir
""")

        if sesion.id_empleado_actual is None:
            print("\nERROR CRÍTICO: No hay un empleado asociado a este usuario.")
            print("Comuníquese con el administrador.")
            input("Presiona Enter para salir...")
            break

        try:
            entrada = input("Seleccione una opción: ").strip()
            if not entrada:
                continue
            opc = int(entrada)
        except ValueError:
            print("Error: Ingrese un número válido.")
            input("Presiona Enter para continuar...")
            continue

        if opc == 1:
            ver_mis_datos()
        elif opc == 2:
            ver_mis_proyectos()
        elif opc == 3:
            addRegistroTiempo()
        elif opc == 4:
            verRegistrosEmpleado()
        elif opc == 5:
            print("Cerrando sesión...")
            saltar_pantalla()
            break
        else:
            print("Opción inválida.")
            input("Presiona Enter para continuar...")


# ==========================================================
#   VER DATOS DEL EMPLEADO
# ==========================================================
def ver_mis_datos():
    saltar_pantalla()
    print("============================================")
    print("                MIS DATOS                   ")
    print("============================================")

    try:
        datos = verEmpleadoPorID(sesion.id_empleado_actual)
        
        if not datos:
            print("No se pudo obtener la información del empleado.")
        else:
            
            print(f" ID:          {datos[0]}")
            print(f" Nombre:      {datos[1]}")
            print(f" Apellido:    {datos[2]}")
            print(f" Email:       {datos[4]}")
            print(f" Teléfono:    {datos[3]}")
            print(f" Dirección:   {datos[6]}")
            print(f" Cargo:       {'Gerente' if datos[7] else 'Empleado'}")
            
    except Exception as e:
        print(f"Error al obtener datos: {e}")
    
    print("============================================")
    input("\nPresiona Enter para continuar...")


# ==========================================================
#   VER PROYECTOS ASOCIADOS AL EMPLEADO ACTUAL
# ==========================================================

def ver_mis_proyectos():
    saltar_pantalla()
    print("============================================")
    print("              MIS PROYECTOS                 ")
    print("============================================")

    try:
        proyectos = verProyectosDeEmpleado(sesion.id_empleado_actual)

        if not proyectos:
            print("\nNo estás asignado a ningún proyecto actualmente.")
        else:
            print(f"{'ID':<12} {'Nombre':<20} {'Estado'}")
            print("-" * 45)
            for p in proyectos:
                p_id = str(p[0])
                p_nom = str(p[1])
                p_est = str(p[5]) if len(p) > 5 else "N/A"
                print(f"{p_id:<12} {p_nom:<20} {p_est}")
            print("-" * 45)

    except Exception as e:
        print(f"Error al obtener proyectos: {e}")

    input("\nPresiona Enter para continuar...")
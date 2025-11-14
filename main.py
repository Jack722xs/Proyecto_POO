from app.vista import view_departamento as vd
from app.vista import view_empleado as ve
#le da un alias a cada view para evitar malas practicas de repeticion

while True:

    print("""MENU ECOTECH
          ¡Seleccione una de las opciones!
          1. Departamentos
          2. Empleados
          3. Usuarios
          4. Proyectos
          5. Salir""")

    try:
        opc = int(input("Seleccione una opcion: "))
    except ValueError:
        print("Error: ingrese un numero valido.")
        continue

    # --- MENU DEPARTAMENTOS --------------------------------------------------------------------------

    if opc == 1:
        while True:
            print("""
                  Menu de Departamentos:
                  1. Agregar departamento
                  2. Editar departamento
                  3. Eliminar departamento
                  4. Ver departamentos
                  5. Volver al menu principal
                  """)

            try:
                sub_opc = int(input("Seleccione una opcion: "))
            except ValueError:
                print("Error, intentelo de nuevo")
                continue

            if sub_opc == 1:
                vd.addDepartamento()
            elif sub_opc == 2:
                vd.editDepartamento()        
            elif sub_opc == 3:
                vd.delDepartamento()
            elif sub_opc == 4:
                vd.readDepartamento()
            elif sub_opc == 5:
                break
            else:
                print("Opcion no valida.")

    # --- MENU EMPLEADOS -----------------------------------------------------------------------------

    elif opc == 2:
        while True:
            print("""
                  Menu Empleados:
                  1. Agregar empleado
                  2. Editar empleado
                  3. Eliminar empleado
                  4. Ver empleados
                  5. Volver al menu principal
                  """)

            try:
                sub_opc = int(input("Seleccione una opcion: "))
            except ValueError:
                print("Error, intentelo de nuevo.")
                continue

            if sub_opc == 1:
                ve.addEmpleado()
            elif sub_opc == 2:
                ve.editEmpleado()
            elif sub_opc == 3:
                ve.delEmpleado()
            elif sub_opc == 4:
                ve.readEmpleado()
            elif sub_opc == 5:
                break
            else:
                print("Opcion no valida.")

    # elif opc == 3:
    # elif opc == 4;

    elif opc == 5:
        print("Saliendo...")
        break

    else:
        print("Opcion no valida.")

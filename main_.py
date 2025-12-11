import sys
import time
import getpass
from app.bbdd.init_db import crear_bd, borrar_base_datos
from app.utils.seguridad import verificar_password
from app.bbdd.conexion import getConexion
import app.sesion.sesion as sesion
from app.utils.helper import * 
from app.vista.menus.view_menu_admin import menu_admin
from app.vista.menus.view_menu_gerente import menu_gerente
from app.vista.menus.view_menu_empleado import menu_empleado

class Color:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    BG_BLUE = "\033[44m"

def imprimir_logo():
    print(f"""{Color.CYAN}{Color.BOLD}
    ███████╗ ██████╗ ██████╗ ████████╗███████╗ ██████╗██╗  ██╗
    ██╔════╝██╔════╝██╔═══██╗╚══██╔══╝██╔════╝██╔════╝██║  ██║
    █████╗  ██║     ██║   ██║   ██║   █████╗  ██║     ███████║
    ██╔══╝  ██║     ██║   ██║   ██║   ██╔══╝  ██║     ██╔══██║
    ███████╗╚██████╗╚██████╔╝   ██║   ███████╗╚██████╗██║  ██║
    ╚══════╝ ╚═════╝ ╚═════╝    ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═╝
    {Color.RESET}""")

def barra_carga(iteracion, total, prefijo='', sufijo='', longitud=40, relleno='█'):
    """Genera una barra de progreso visual en la consola"""
    porcentaje = ("{0:.1f}").format(100 * (iteracion / float(total)))
    lleno = int(longitud * iteracion // total)
    barra = relleno * lleno + '-' * (longitud - lleno)
    sys.stdout.write(f'\r{Color.GREEN}{prefijo} |{barra}| {porcentaje}% {sufijo}{Color.RESET}')
    sys.stdout.flush()

def animacion_inicio():
    saltar_pantalla()
    imprimir_logo()
    print(f"\n{Color.BOLD}    INICIANDO SISTEMA CORPORATIVO ECOTECH v2.5{Color.RESET}\n")
    
    pasos = [
        "Cargando módulos del núcleo...",
        "Verificando integridad de memoria...",
        "Estableciendo conexión segura...",
        "Cargando base de datos...",
        "Iniciando interfaz de usuario..."
    ]
    
    total = len(pasos) * 10
    progreso = 0
    
    for paso in pasos:

        for _ in range(10):
            time.sleep(0.04)
            progreso += 1
            barra_carga(progreso, 50, prefijo="Cargando:", sufijo=paso)
        print()

    time.sleep(0.5)
    print(f"\n{Color.GREEN}    >> SISTEMA CARGADO CORRECTAMENTE <<{Color.RESET}")
    time.sleep(1)

def autentificacion(nombre_usuario, pw):
    cone = None
    try:
        cone = getConexion()
        cursor = cone.cursor()
        sql = "SELECT password_hash, id_empleado, rol FROM usuario WHERE nombre_usuario = %s"
        cursor.execute(sql, (nombre_usuario,))
        row = cursor.fetchone()

        if not row:
            return False

        hash_pw_str, id_empleado, rol = row

        if verificar_password(pw, hash_pw_str):
            sesion.nombre_usuario = nombre_usuario
            sesion.rol_actual = rol
            sesion.id_empleado_actual = id_empleado
            return True
        
        return False
    except Exception as e:
        print(f"{Color.RED}Error de sistema: {e}{Color.RESET}")
        return False

def login_terminal():
    intentos = 5
    
    while intentos > 0:
        saltar_pantalla()
        imprimir_logo()
        print(f"{Color.BLUE}" + "="*60 + f"{Color.RESET}")
        print(f"{Color.BOLD}                PORTAL DE ACCESO SEGURO{Color.RESET}")
        print(f"{Color.BLUE}" + "="*60 + f"{Color.RESET}\n")
        
        try:
            print(f"{Color.YELLOW}Ingrese sus credenciales corporativas.{Color.RESET}")
            usuario = input(f"{Color.CYAN}➤ Usuario: {Color.RESET}").strip()
            
            if not usuario:
                intentos -= 1
                print(f"\n{Color.RED}⚠  ERROR: El usuario no puede estar vacío.{Color.RESET}")
                print(f"{Color.YELLOW}Intentos restantes: {intentos}{Color.RESET}")
                input("Presione Enter para reintentar...")
                continue
                
            password = getpass.getpass(f"{Color.CYAN}➤ Contraseña: {Color.RESET}")

            print(f"\n{Color.YELLOW}Verificando credenciales...{Color.RESET}")
            time.sleep(0.8)

            if autentificacion(usuario, password):
                print(f"\n{Color.GREEN}✔ ACCESO CONCEDIDO.{Color.RESET}")
                print(f"Bienvenido, {Color.BOLD}{sesion.nombre_usuario}{Color.RESET}.")
                print(f"Perfil cargado: {Color.BG_BLUE} {sesion.rol_actual.upper()} {Color.RESET}")
                time.sleep(1.5)

                if sesion.rol_actual == "admin":
                    menu_admin()
                elif sesion.rol_actual == "gerente":
                    menu_gerente()
                elif sesion.rol_actual == "empleado":
                    menu_empleado()
                else:
                    print(f"{Color.RED}Error: Rol desconocido o sin permisos.{Color.RESET}")
                    input("Presione Enter...")
                return 

            else:
                intentos -= 1
                print(f"\n{Color.RED}✖ Credenciales incorrectas.{Color.RESET}")
                print(f"{Color.YELLOW}Intentos restantes: {intentos}{Color.RESET}")
                input("Presione Enter para intentar de nuevo...")

        except KeyboardInterrupt:
            print(f"\n\n{Color.YELLOW}Operación cancelada por el usuario.{Color.RESET}")
            return

    print(f"\n{Color.BG_BLUE}{Color.RED} DEMASIADOS INTENTOS FALLIDOS. ACCESO BLOQUEADO. {Color.RESET}")
    input("Presione Enter para volver al menú principal...")

def main():

    animacion_inicio()
    
    print("Verificando conexión con base de datos...")
    if not crear_bd():
        print(f"{Color.RED}Error crítico: No se pudo conectar con la base de datos.{Color.RESET}")
        sys.exit()
        
    try:
        while True:
            saltar_pantalla()
            imprimir_logo()
            
            print(f"{Color.BLUE}╔{'═'*42}╗{Color.RESET}")
            print(f"{Color.BLUE}║{Color.RESET} {Color.BOLD}{Color.WHITE}      SISTEMA PRINCIPAL ECOTECH          {Color.RESET}{Color.BLUE}║{Color.RESET}")
            print(f"{Color.BLUE}╠{'═'*42}╣{Color.RESET}")
            print(f"{Color.BLUE}║{Color.RESET}  1. Iniciar Sesión                       {Color.BLUE}║{Color.RESET}")
            print(f"{Color.BLUE}║{Color.RESET}  2. Apagar Sistema                       {Color.BLUE}║{Color.RESET}")
            print(f"{Color.BLUE}╚{'═'*42}╝{Color.RESET}")
            
            try:
                op = input(f"\n{Color.GREEN}Selecciona una opción > {Color.RESET}").strip()

                if op == "1":
                    login_terminal()

                elif op == "2":
                    print(f"\n{Color.YELLOW}Cerrando sistema y conexiones...{Color.RESET}")
                    time.sleep(1)
                    break 

                else:
                    print(f"\n{Color.RED}Opción no válida.{Color.RESET}")
                    input("Presione Enter...")
            
            except KeyboardInterrupt:
                print(f"\n{Color.YELLOW}Interrupción detectada...{Color.RESET}")
                break
            except Exception as e:
                print(f"{Color.RED}Error en el menú principal: {e}{Color.RESET}")
                input("Presione Enter...")

    finally:
        borrar_base_datos()
        print(f"\n{Color.CYAN}¡Gracias por usar EcoTech Solutions!{Color.RESET}")
        time.sleep(1)

if __name__ == "__main__":
    main()
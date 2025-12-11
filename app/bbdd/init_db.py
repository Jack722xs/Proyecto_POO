import mysql.connector
import bcrypt # Asegúrate de tener instalado: pip install bcrypt

# Función auxiliar local para hashear en la inicialización
def hash_demo(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def crear_bd():
    config = {
        'host': 'localhost',
        'user': 'root',
        'password': ''
    }

    try:
        cone = mysql.connector.connect(**config)
        cursor = cone.cursor()

        cursor.execute("CREATE DATABASE IF NOT EXISTS ecotech")
        cursor.execute("USE ecotech")

        tablas = {}

        # 1. TABLAS PRINCIPALES
        tablas['departamento'] = """
            CREATE TABLE IF NOT EXISTS departamento (
                id_depart VARCHAR(15) NOT NULL,
                proposito_depart VARCHAR(25) NOT NULL,
                nombre_depart VARCHAR(25) NOT NULL,
                gerente_asociado VARCHAR(25) DEFAULT NULL,
                PRIMARY KEY (id_depart)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
        """

        tablas['empleado'] = """
            CREATE TABLE IF NOT EXISTS empleado (
                id_empleado INT(11) NOT NULL AUTO_INCREMENT,
                nombre VARCHAR(85) NOT NULL,
                apellido VARCHAR(35) NOT NULL,
                telefono VARCHAR(10) DEFAULT NULL,
                email VARCHAR(100) NOT NULL,
                salario FLOAT NOT NULL,
                direccion VARCHAR(50) NOT NULL,
                es_gerente TINYINT(1) DEFAULT 0,
                PRIMARY KEY (id_empleado)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
        """

        tablas['proyecto'] = """
            CREATE TABLE IF NOT EXISTS proyecto (
                id_proyecto VARCHAR(25) NOT NULL,
                nombre VARCHAR(25) NOT NULL,
                descripcion VARCHAR(100) NOT NULL,
                fecha_inicio DATE NOT NULL,
                fecha_fin DATE NOT NULL,
                estado_proyecto VARCHAR(100) NOT NULL,
                id_empleado INT(11) DEFAULT NULL,
                PRIMARY KEY (id_proyecto)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
        """

        # TABLA USUARIO SEGURA (Con FK)
        tablas['usuario'] = """
            CREATE TABLE IF NOT EXISTS usuario (
                nombre_usuario VARCHAR(50) NOT NULL,
                email VARCHAR(100) NOT NULL,
                password_hash VARCHAR(60) NOT NULL,
                id_empleado INT(11) DEFAULT NULL,
                rol ENUM('admin','gerente','empleado') DEFAULT 'empleado',
                PRIMARY KEY (nombre_usuario),
                CONSTRAINT fk_usuario_empleado FOREIGN KEY (id_empleado) REFERENCES empleado (id_empleado) ON DELETE SET NULL
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
        """

        tablas['registro_tiempo'] = """
            CREATE TABLE IF NOT EXISTS registro_tiempo (
                id_registro INT(11) NOT NULL AUTO_INCREMENT,
                id_empleado INT(11) DEFAULT NULL,
                id_proyecto VARCHAR(25) DEFAULT NULL,
                fecha DATE NOT NULL,
                horas FLOAT NOT NULL,
                descripcion TEXT DEFAULT NULL,
                PRIMARY KEY (id_registro),
                CONSTRAINT fk_tiempo_empleado FOREIGN KEY (id_empleado) REFERENCES empleado (id_empleado) ON DELETE CASCADE,
                CONSTRAINT fk_tiempo_proyecto FOREIGN KEY (id_proyecto) REFERENCES proyecto (id_proyecto) ON DELETE CASCADE
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
        """

        # TABLAS DE RELACIÓN (MANY TO MANY)
        tablas['empleado_departamento'] = """
            CREATE TABLE IF NOT EXISTS empleado_departamento (
                id_empleado INT(11) NOT NULL,
                id_depart VARCHAR(15) NOT NULL,
                PRIMARY KEY (id_empleado, id_depart),
                CONSTRAINT fk_ed_emp FOREIGN KEY (id_empleado) REFERENCES empleado (id_empleado) ON DELETE CASCADE,
                CONSTRAINT fk_ed_dep FOREIGN KEY (id_depart) REFERENCES departamento (id_depart) ON DELETE CASCADE
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
        """

        tablas['empleado_proyecto'] = """
            CREATE TABLE IF NOT EXISTS empleado_proyecto (
                id_empleado INT(11) NOT NULL,
                id_proyecto VARCHAR(25) NOT NULL, 
                PRIMARY KEY (id_empleado, id_proyecto),
                CONSTRAINT fk_ep_emp FOREIGN KEY (id_empleado) REFERENCES empleado (id_empleado) ON DELETE CASCADE,
                CONSTRAINT fk_ep_proy FOREIGN KEY (id_proyecto) REFERENCES proyecto (id_proyecto) ON DELETE CASCADE
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
        """

        tablas['proyecto_departamento'] = """
            CREATE TABLE IF NOT EXISTS proyecto_departamento (
                id_proyecto VARCHAR(25) NOT NULL,
                id_depart VARCHAR(15) NOT NULL,
                PRIMARY KEY (id_proyecto, id_depart),
                CONSTRAINT fk_pd_proy FOREIGN KEY (id_proyecto) REFERENCES proyecto (id_proyecto) ON DELETE CASCADE,
                CONSTRAINT fk_pd_dep FOREIGN KEY (id_depart) REFERENCES departamento (id_depart) ON DELETE CASCADE
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
        """

        # Otras tablas
        tablas['usuario_empleado'] = """
            CREATE TABLE IF NOT EXISTS usuario_empleado (
                id_empleado INT(11) NOT NULL,
                id_usuario VARCHAR(50) NOT NULL,
                PRIMARY KEY (id_empleado, id_usuario)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
        """
        
        tablas['registro_indicadores'] = """
            CREATE TABLE IF NOT EXISTS registro_indicadores (
                id_consulta INT(11) NOT NULL AUTO_INCREMENT,
                nombre_indicador VARCHAR(50) DEFAULT NULL,
                valor DECIMAL(10,2) DEFAULT NULL,
                fecha_valor DATE DEFAULT NULL,
                fecha_consulta DATETIME DEFAULT NULL,
                usuario_consulta VARCHAR(100) DEFAULT NULL,
                origen_datos VARCHAR(100) DEFAULT NULL,
                PRIMARY KEY (id_consulta)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
        """

        # Orden de creación para respetar FK
        orden = ['departamento', 'empleado', 'proyecto', 'usuario', 'registro_tiempo', 
                 'empleado_departamento', 'empleado_proyecto', 'proyecto_departamento', 
                 'usuario_empleado', 'registro_indicadores']

        for t in orden:
            cursor.execute(tablas[t])

        # --- INSERCIONES INICIALES ---
        print("Insertando datos iniciales...")

        # 1. Empleados
        sql_empleado = """INSERT IGNORE INTO empleado (id_empleado, nombre, apellido, email, salario, direccion, es_gerente) 
                          VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        datos_empleado = [
            (202500001, 'Juan', 'Pérez', 'juan@ecotech.com', 500000, 'Av. Chile', 0),
            (202500002, 'Claudia', 'González', 'claudia@ecotech.com', 520000, 'Calle Andes', 0),
            (202500008, 'Tello', 'Gerente', 'tello@ecotech.com', 900000, 'Oficina Central', 1),
            (217743125, 'Jack', 'Cardenas', 'jack@ecotech.com', 600000, 'Riquelme', 1)
        ]
        cursor.executemany(sql_empleado, datos_empleado)

        # 2. Departamentos
        sql_dep = "INSERT IGNORE INTO departamento (id_depart, nombre_depart, proposito_depart) VALUES (%s, %s, %s)"
        datos_dep = [('DPT001', 'Marketing', 'Ventas'), ('DPT002', 'RRHH', 'Personal')]
        cursor.executemany(sql_dep, datos_dep)

        # 3. Proyectos
        sql_proy = "INSERT IGNORE INTO proyecto (id_proyecto, nombre, descripcion, fecha_inicio, fecha_fin, estado_proyecto) VALUES (%s, %s, %s, %s, %s, %s)"
        datos_proy = [('PRJ001', 'Web 2.0', 'Renovación Web', '2025-01-01', '2025-06-01', 'Activo')]
        cursor.executemany(sql_proy, datos_proy)

        # 4. USUARIOS (AQUÍ GENERAMOS LOS HASHES REALES)
        # La contraseña será igual al nombre de usuario para facilitar pruebas
        sql_usuario = """INSERT IGNORE INTO usuario (nombre_usuario, email, password_hash, id_empleado, rol) 
                         VALUES (%s, %s, %s, %s, %s)"""
        datos_usuario = [
            ('admin', 'admin@ecotech.com', hash_demo('admin'), None, 'admin'),
            ('tello', 'tello@ecotech.com', hash_demo('tello'), 202500008, 'gerente'),
            ('claudia', 'claudia@ecotech.com', hash_demo('claudia'), 202500002, 'empleado'),
            ('jacson', 'jack@ecotech.com', hash_demo('jacson'), 217743125, 'gerente')
        ]
        cursor.executemany(sql_usuario, datos_usuario)

        print("Base de datos y usuarios creados correctamente.")
        cone.commit()
        cursor.close()
        cone.close()
        return True

    except mysql.connector.Error as err:
        print(f"Error inicializando BBDD: {err}")
        return False

def borrar_base_datos():
    config = {'host': 'localhost', 'user': 'root', 'password': ''}
    try:
        cone = mysql.connector.connect(**config)
        cursor = cone.cursor()
        cursor.execute("DROP DATABASE IF EXISTS ecotech")
        print("\n[LIMPIEZA] Base de datos eliminada.")
        cursor.close()
        cone.close()
        return True
    except:
        return False
import mysql.connector

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

        tablas['usuario'] = """
            CREATE TABLE IF NOT EXISTS usuario (
                nombre_usuario VARCHAR(50) NOT NULL,
                contraseña VARCHAR(100) NOT NULL,
                email VARCHAR(100) NOT NULL,
                password_hash VARCHAR(60) NOT NULL,
                id_empleado INT(100) DEFAULT NULL,
                rol ENUM('admin','gerente','empleado') DEFAULT 'empleado',
                PRIMARY KEY (nombre_usuario)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
        """

        tablas['registro_tiempo'] = """
            CREATE TABLE IF NOT EXISTS registro_tiempo (
                id_registro INT(11) NOT NULL AUTO_INCREMENT,
                id_empleado VARCHAR(20) DEFAULT NULL,
                id_proyecto VARCHAR(20) DEFAULT NULL,
                fecha DATE NOT NULL,
                horas FLOAT NOT NULL,
                descripcion TEXT DEFAULT NULL,
                PRIMARY KEY (id_registro)
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

        tablas['empleado_departamento'] = """
            CREATE TABLE IF NOT EXISTS empleado_departamento (
                id_empleado INT(11) NOT NULL,
                id_depart VARCHAR(50) NOT NULL,
                PRIMARY KEY (id_empleado, id_depart),
                KEY id_depart (id_depart),
                CONSTRAINT emp_dep_fk1 FOREIGN KEY (id_empleado) REFERENCES empleado (id_empleado) ON DELETE CASCADE,
                CONSTRAINT emp_dep_fk2 FOREIGN KEY (id_depart) REFERENCES departamento (id_depart) ON DELETE CASCADE
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
        """

        tablas['empleado_proyecto'] = """
            CREATE TABLE IF NOT EXISTS empleado_proyecto (
                id_empleado INT(11) NOT NULL,
                id_proyecto VARCHAR(25) NOT NULL, 
                PRIMARY KEY (id_empleado, id_proyecto)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
        """

        tablas['proyecto_departamento'] = """
            CREATE TABLE IF NOT EXISTS proyecto_departamento (
                id_proyecto VARCHAR(50) NOT NULL,
                id_depart VARCHAR(50) NOT NULL,
                PRIMARY KEY (id_proyecto, id_depart),
                KEY id_depart (id_depart),
                CONSTRAINT proy_dep_fk1 FOREIGN KEY (id_proyecto) REFERENCES proyecto (id_proyecto) ON DELETE CASCADE,
                CONSTRAINT proy_dep_fk2 FOREIGN KEY (id_depart) REFERENCES departamento (id_depart) ON DELETE CASCADE
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
        """

        tablas['usuario_empleado'] = """
            CREATE TABLE IF NOT EXISTS usuario_empleado (
                id_empleado INT(100) NOT NULL,
                id_usuario INT(100) NOT NULL,
                PRIMARY KEY (id_empleado, id_usuario)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
        """

        orden_creacion = [
            'departamento', 'empleado', 'proyecto', 'usuario',
            'registro_tiempo', 'registro_indicadores',
            'empleado_departamento', 'empleado_proyecto', 
            'proyecto_departamento', 'usuario_empleado'
        ]

        for t in orden_creacion:
            cursor.execute(tablas[t])

        print("Tablas verificadas. Insertando datos iniciales...")

        sql_empleado = """
            INSERT IGNORE INTO empleado (id_empleado, nombre, apellido, telefono, email, salario, direccion, es_gerente) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        datos_empleado = [
            (202500001, 'Juan', 'Pérez', '945569123', 'juan.perez@email.com', 500000, 'Av. Chile 123', 0),
            (202500002, 'María', 'González', '974456210', 'maria.gonzalez@email.com', 520000, 'Calle Los Andes 32', 0),
            (202500003, 'Carlos', 'Soto', '956123789', 'carlos.soto@email.com', 495000, 'Pasaje Sur 11', 0),
            (202500004, 'Ana', 'Ramírez', '967893156', 'ana.ramirez@email.com', 515000, 'Av. Central 999', 0),
            (202500005, 'Pedro', 'Morales', '923451234', 'pedro.morales@email.com', 480000, 'Camino Verde 105', 0),
            (202500006, 'Camila', 'Ruiz', '932156400', 'camila.ruiz@email.com', 540000, 'Plaza Norte 66', 0),
            (202500007, 'Diego', 'Herrera', '916789345', 'diego.herrera@email.com', 470000, 'Calle Sur 21', 0),
            (202500008, 'Fernanda', 'Rojas', '933214567', 'fernanda.rojas@email.com', 510000, 'Av. Pacífico 19', 0),
            (217743125, 'jack', 'cardenas', None, 'jacsongrc@gmial.com', 150, 'Riquelme1720', 0)
        ]
        cursor.executemany(sql_empleado, datos_empleado)

        sql_departamento = """
            INSERT IGNORE INTO departamento (id_depart, proposito_depart, nombre_depart, gerente_asociado) 
            VALUES (%s, %s, %s, %s)
        """
        datos_departamento = [
            ('DPT001', 'Marketing digital', 'Marketing', 'Fernanda Román'),
            ('DPT002', 'Administración', 'Recursos Humanos', 'Marcela Soto'),
            ('217743126', 'prueba 1', 'departamento 1', None)
        ]
        cursor.executemany(sql_departamento, datos_departamento)

        sql_proyecto = """
            INSERT IGNORE INTO proyecto (id_proyecto, nombre, descripcion, fecha_inicio, fecha_fin, estado_proyecto, id_empleado) 
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        datos_proyecto = [
            ('PRJ202501', 'Gestión Inventario', 'Sistema para controlar inventarios de bodega.', '2025-02-10', '2025-05-10', 'Planificado', 0),
            ('PRJ202502', 'Web Corporativa', 'Desarrollo e implementación del sitio web institucional.', '2025-01-15', '2025-03-22', 'En progreso', 0),
            ('PRJ202503', 'Portal RRHH', 'Plataforma para autogestión y consultas de empleados.', '2025-01-25', '2025-04-18', 'Terminado', 0),
            ('PRJ202504', 'App Cliente Móvil', 'Aplicación móvil para clientes y seguimiento de pedidos.', '2025-03-01', '2025-06-15', 'En progreso', 0),
            ('217743127', 'tellecto', 'prueba de proyecto', '2000-05-13', '2005-12-25', 'pendiente', None)
        ]
        cursor.executemany(sql_proyecto, datos_proyecto)

        sql_usuario = """
            INSERT IGNORE INTO usuario (nombre_usuario, contraseña, email, password_hash, id_empleado, rol) 
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        datos_usuario = [
            ('tello', '', 'jasda', '$2b$12$3zzpRFBREIgQkRG4cg3ZoOtUy2B8ZwCnUt8T0e3HegI7z9IPn/5SK', 202500008, 'gerente'),
            ('claudia', '', 'asd', '$2b$12$u6XdqFiMh5Ahj7tq1vfcJuszUBXqnha/OgVJVrvQZIMXhEc2r4wOO', 202500002, 'empleado'),
            ('admin', '', 'admin@ecotech.com', '$2b$12$9k.97y6IKMSaAVEtDbTOyuDdP8GoVJep9zXjinEYY8H6ZED9O0H6O', None, 'admin'),
            ('jacson', '1234', 'jacson', '$2b$12$kqDUCiLQtXE5FuZyTOBYIukJZ7rYh6lRFUYFWo1QZ6yesd/NIq73i', 217743125, 'gerente')
        ]
        cursor.executemany(sql_usuario, datos_usuario)

        sql_tiempo = """
            INSERT IGNORE INTO registro_tiempo (id_registro, id_empleado, id_proyecto, fecha, horas, descripcion) 
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        datos_tiempo = [
            (1, '202500008', '111', '2025-11-21', 20, 'hacer juego')
        ]
        cursor.executemany(sql_tiempo, datos_tiempo)

        cursor.execute("INSERT IGNORE INTO empleado_departamento (id_empleado, id_depart) VALUES (202500008, '217743126')")
        
        sql_emp_proy = "INSERT IGNORE INTO empleado_proyecto (id_empleado, id_proyecto) VALUES (%s, %s)"
        datos_emp_proy = [
            (202500001, '111'),
            (202500002, '217743127'),
            (202500008, '111')
        ]

        cursor.execute("INSERT IGNORE INTO proyecto (id_proyecto, nombre, descripcion, fecha_inicio, fecha_fin, estado_proyecto, id_empleado) VALUES ('111', 'Proyecto Base', 'Auto-generado', '2025-01-01', '2025-12-31', 'Activo', 0)")
        
        cursor.executemany(sql_emp_proy, datos_emp_proy)

        cursor.execute("INSERT IGNORE INTO proyecto_departamento (id_proyecto, id_depart) VALUES ('217743127', '217743126')")

        print("Base de datos y datos iniciales cargados correctamente.")
        cone.commit()
        cursor.close()
        cone.close()
        return True

    except mysql.connector.Error as err:
        print(f"Error inicializando BBDD: {err}")
        try:
            if cone.is_connected():
                cursor.close()
                cone.close()
        except:
            pass
        return False
    
def borrar_base_datos():
    config = {
        'host': 'localhost',
        'user': 'root',
        'password': ''
    }
    
    try:
        cone = mysql.connector.connect(**config)
        cursor = cone.cursor()
        
        sql = "DROP DATABASE IF EXISTS ecotech"
        cursor.execute(sql)
        
        print("\n" + "="*40)
        print(" SISTEMA DE LIMPIEZA")
        print("="*40)
        print("Base de datos 'ecotech' eliminada correctamente.")
        print("Datos temporales borrados por seguridad.")
        print("="*40 + "\n")
        
        cursor.close()
        cone.close()
        return True
        
    except mysql.connector.Error as err:
        print(f"Error al borrar la base de datos: {err}")
        return False    
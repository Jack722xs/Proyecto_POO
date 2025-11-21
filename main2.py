

from app.vista.view_departamento import *
from app.vista.view_empleado import *
from app.vista.view_proyecto import *
from app.vista.view_usuario import *
from app.vista.view_informe import menu_informes  
from app.vista.view_registro_tiempo import * 
from app.vista.sub_vista.view_usuario_empleado import *


# Nuevas vistas de relaciones
from app.controlador.sub_controlador.DAO_empleado_departamento import *
from app.controlador.sub_controlador.DAO_empleado_proyecto import *
from app.controlador.sub_controlador.DAO_proyecto_departamento import *

from app.vista.menus.view_menu_admin import *
menu_admin()
  

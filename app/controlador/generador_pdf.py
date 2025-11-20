import sys
import os
from pathlib import Path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../..")))

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from datetime import datetime

class GeneradorInformesPDF:
    """Clase para generar informes en formato PDF"""
    
    def __init__(self, nombre_archivo="informe"):

        # ruta de Descargas del usuario

        descargas = str(Path.home() / "Downloads")
        
        self.nombre_archivo = f"{nombre_archivo}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        self.ruta_pdf = os.path.join(descargas, self.nombre_archivo)
        self.doc = SimpleDocTemplate(self.ruta_pdf, pagesize=letter)
        self.elementos = []
        self.estilos = getSampleStyleSheet()
        self._crear_directorio()
    
    def _crear_directorio(self):
        """Verifica que la carpeta de descargas existe"""
        descargas = str(Path.home() / "Downloads")
        if not os.path.exists(descargas):
            os.makedirs(descargas)
    
    def _estilos_personalizados(self):
        """Define estilos personalizados para el PDF"""
        estilo_titulo = ParagraphStyle(
            'TituloPersonalizado',
            parent=self.estilos['Heading1'],
            fontSize=18,
            textColor=colors.HexColor('#1a5490'),
            spaceAfter=30,
            alignment=1
        )
        
        estilo_subtitulo = ParagraphStyle(
            'SubtituloPersonalizado',
            parent=self.estilos['Heading2'],
            fontSize=14,
            textColor=colors.HexColor('#2a7fbf'),
            spaceAfter=12,
            spaceBefore=12
        )
        
        return estilo_titulo, estilo_subtitulo
    
    def agregar_titulo(self, titulo):
        """Agrega título al informe"""
        estilo_titulo, _ = self._estilos_personalizados()
        self.elementos.append(Paragraph(titulo, estilo_titulo))
        self.elementos.append(Spacer(1, 0.3*inch))
    
    def agregar_fecha_generacion(self, fecha):
        """Agrega fecha de generación"""
        parrafo = Paragraph(f"<b>Fecha de generación:</b> {fecha}", self.estilos['Normal'])
        self.elementos.append(parrafo)
        self.elementos.append(Spacer(1, 0.2*inch))
    
    def agregar_tabla_empleados(self, empleados):
        """Agrega tabla de empleados al PDF"""
        _, estilo_subtitulo = self._estilos_personalizados()
        self.elementos.append(Paragraph("Listado de Empleados", estilo_subtitulo))
        
        datos = [['ID', 'Nombre', 'Apellido', 'Email', 'Salario']]
        
        for emp in empleados:
            datos.append([
                str(emp.get('id_empleado', 'N/A')),
                str(emp.get('nombre', 'N/A')),
                str(emp.get('apellido', 'N/A')),
                str(emp.get('email', 'N/A')),
                f"${float(emp.get('salario', 0)):,.2f}"
            ])
        
        tabla = Table(datos, colWidths=[0.8*inch, 1.2*inch, 1.2*inch, 1.8*inch, 1.2*inch])
        
        estilo_tabla = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2a7fbf')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.lightgrey]),
        ])
        
        tabla.setStyle(estilo_tabla)
        self.elementos.append(tabla)
        self.elementos.append(Spacer(1, 0.3*inch))
    
    def agregar_tabla_departamentos(self, departamentos):
        """Agrega tabla de departamentos al PDF"""
        _, estilo_subtitulo = self._estilos_personalizados()
        self.elementos.append(Paragraph("Listado de Departamentos", estilo_subtitulo))
        
        datos = [['ID Depart', 'Nombre', 'Gerente', 'Propósito']]
        
        for dept in departamentos:
            datos.append([
                str(dept.get('id_depart', 'N/A')),
                str(dept.get('nombre_depart', 'N/A')),
                str(dept.get('gerente_asociado', 'N/A')),
                str(dept.get('proposito_depart', 'N/A'))
            ])
        
        tabla = Table(datos, colWidths=[1*inch, 1.5*inch, 1.5*inch, 2*inch])
        
        estilo_tabla = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2a7fbf')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.lightgrey]),
        ])
        
        tabla.setStyle(estilo_tabla)
        self.elementos.append(tabla)
        self.elementos.append(Spacer(1, 0.3*inch))
    
    def agregar_tabla_proyectos(self, proyectos):
        """Agrega tabla de proyectos al PDF"""
        _, estilo_subtitulo = self._estilos_personalizados()
        self.elementos.append(Paragraph("Listado de Proyectos", estilo_subtitulo))
        
        datos = [['ID Proyecto', 'Nombre', 'Estado', 'Fecha Inicio', 'Fecha Fin']]
        
        for proy in proyectos:
            datos.append([
                str(proy.get('id_proyecto', 'N/A')),
                str(proy.get('nombre', 'N/A')),
                str(proy.get('estado_proyecto', 'N/A')),
                str(proy.get('fecha_inicio', 'N/A')),
                str(proy.get('fecha_fin', 'N/A'))
            ])
        
        tabla = Table(datos, colWidths=[1*inch, 1.5*inch, 1.2*inch, 1.5*inch, 1.5*inch])
        
        estilo_tabla = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2a7fbf')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.lightgrey]),
        ])
        
        tabla.setStyle(estilo_tabla)
        self.elementos.append(tabla)
        self.elementos.append(Spacer(1, 0.3*inch))
    
    def generar_pdf(self):
        """Genera el archivo PDF"""
        try:
            self.doc.build(self.elementos)
            return True, self.ruta_pdf
        except Exception as e:
            return False, str(e)


def generador_informe(empleados, departamentos, proyectos, tipo):
    """
    Función única que genera el informe PDF.
    
    Args:
        empleados: Lista de empleados (dict) o None
        departamentos: Lista de departamentos (dict) o None
        proyectos: Lista de proyectos (dict) o None
        tipo: Tipo de informe ('completo', 'empleados', 'departamentos', 'proyectos')
    
    Returns:
        Tupla (exito: bool, ruta: str)
    """
    try:
        generador = GeneradorInformesPDF(f"informe_{tipo}")
        
        # Título según el tipo
        titulos = {
            "completo": "INFORME COMPLETO DEL SISTEMA - ECOTECH",
            "empleados": "INFORME DE EMPLEADOS - ECOTECH",
            "departamentos": "INFORME DE DEPARTAMENTOS - ECOTECH",
            "proyectos": "INFORME DE PROYECTOS - ECOTECH"
        }
        
        titulo = titulos.get(tipo, "INFORME - ECOTECH")
        generador.agregar_titulo(titulo)
        generador.agregar_fecha_generacion(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        
        # Agregar tablas según tipo
        if tipo in ["completo", "empleados"] and empleados:
            generador.agregar_tabla_empleados(empleados)
            if tipo == "completo":
                generador.elementos.append(PageBreak())
        
        if tipo in ["completo", "departamentos"] and departamentos:
            generador.agregar_tabla_departamentos(departamentos)
            if tipo == "completo":
                generador.elementos.append(PageBreak())
        
        if tipo in ["completo", "proyectos"] and proyectos:
            generador.agregar_tabla_proyectos(proyectos)
        
        exito, ruta = generador.generar_pdf()
        
        if exito:
            print(f"✓ Informe PDF generado en: {ruta}")
        else:
            print(f"✗ Error: {ruta}")
        
        return exito, ruta
    
    except Exception as e:
        print(f"Error en generador_informe: {str(e)}")
        return False, str(e)
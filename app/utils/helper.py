import os
import platform

def limpiar_pantalla():
    sistema = platform.system()
    if sistema == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    input("\nPresione Enter para continuar...")

def saltar_pantalla():
    sistema = platform.system()
    if sistema == "Windows":
        os.system("cls")
    else:
        os.system("clear")              
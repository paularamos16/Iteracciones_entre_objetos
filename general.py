import os, sys


def limpiar():
    os.system("cls") if os.name =="nt" else os.system("clear")
    
def presionar_enter():
    print("presione <Enter> para continuar...")
    input()
    
def salir():
    print("hasta luego....")
    sys.exit(1)
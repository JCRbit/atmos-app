import os
import platform
from datetime import datetime

def limpiar_pantalla():
    """
    Limpia la consola dependiendo del sistema operativo.
    """
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def imprimir_encabezado_h1(titulo):
    """
    Imprime un encabezado para el menú principal de la consola.
    """
    ancho = 50
    print("╔" + "═" * (ancho - 2) + "╗")
    print(f"║{titulo.center(ancho - 2)}║")
    print("╚" + "═" * (ancho - 2) + "╝")

def imprimir_encabezado_h2(titulo: str):
    """
    Imprime un encabezado para los menus secundarios de la consola.
    """
    ancho = 50
    print("=" * ancho)
    print(f"{titulo.center(ancho)}")
    print("=" * ancho)

def normalizar_entrada(texto: str) -> str:
    """
    Limpia el texto de entrada: elimina espacios extra y convierte 
    comas en puntos para asegurar que float() no falle.
    """
    if not texto:
        return ""
    return texto.strip().replace(",", ".")
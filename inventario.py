import os
from tkinter import filedialog

# Función para cargar el inventario inicial desde un archivo .inv
def cargar_inventario_inicial():
    # Crea un diccionario vacío para almacenar el inventario
    inventario = {}
    
    # Muestra un cuadro de diálogo para seleccionar el archivo .inv
    archivo_inv = filedialog.askopenfilename(title="Seleccione el archivo .inv", filetypes=(("Archivos INV", "*.inv"), ("Todos los archivos", "*.*")))
    
import os
from tkinter import filedialog

# Función para cargar el inventario inicial desde un archivo .inv
def cargar_inventario_inicial():
    # Crea un diccionario vacío para almacenar el inventario
    inventario = {}
    
    # Muestra un cuadro de diálogo para seleccionar el archivo .inv
    archivo_inv = filedialog.askopenfilename(title="Seleccione el archivo .inv", filetypes=(("Archivos INV", "*.inv"), ("Todos los archivos", "*.*")))
     # Verifica si el archivo existe
    if os.path.exists(archivo_inv):
        # Abre el archivo en modo lectura
        with open(archivo_inv, "r") as f:
            # Lee cada línea del archivo
            for linea in f:
                try:
                    # Separa la instrucción y los datos
                    instruccion, datos = linea.strip().split(" ")
                except ValueError:
                    # Si ocurre un error al separar la instrucción y los datos, mostrar un mensaje de error y continuar con la siguiente línea
                    print(f"Error: La línea '{linea}' no está formateada correctamente")
                    continue
                
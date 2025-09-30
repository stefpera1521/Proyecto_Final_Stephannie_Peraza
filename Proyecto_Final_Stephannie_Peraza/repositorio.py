# REPOSITORIO

import csv
import os
from modelos import Estudiante

class RepositorioCSV:
    """Maneja la persistencia de datos en archivo CSV."""

    def __init__(self, archivo):
        self.archivo = archivo

    def cargar(self, gestor):
        if not os.path.exists(self.archivo):
            return
        with open(self.archivo, mode="r", newline='', encoding="utf-8") as f:
            lector = csv.DictReader(f)
            for fila in lector:
                try:
                    gestor.agregar_estudiante(fila["nombre"], float(fila["nota"]))
                except Exception as e:
                    print(f"Error al cargar estudiante: {e}")

    def guardar(self, gestor):
        with open(self.archivo, mode="w", newline='', encoding="utf-8") as f:
            campos = ["id", "nombre", "nota"]
            escritor = csv.DictWriter(f, fieldnames=campos)
            escritor.writeheader()
            for estudiante in gestor.obtener_todos():
                escritor.writerow(estudiante.to_dict())
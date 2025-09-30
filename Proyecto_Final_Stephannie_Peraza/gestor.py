# GESTOR ESTUDIANTE

from modelos import Estudiante

class Gestor_Estudiante: #esta clase administra registros y las operaciones sobre los estudiantes

    def __init__(self):
      self.estudiantes = []
      self._next_id = 1

    def agregar_estudiante(self, nombre, nota):
      est = Estudiante(self._next_id, nombre, nota)
      self.estudiantes.append(est)
      self._next_id += 1

    def obtener_todos(self):
      return self.estudiantes

    def listar_estudiantes(self, criterio="id"):
      if criterio == "nombre":
        return sorted(self.estudiantes, key=lambda e: e.nombre)
      elif criterio == "nota":
        return sorted(self.estudiantes, key=lambda e: e.nota, reverse=True)
      return self.estudiantes

    def editar_nota(self, id_est, nueva_nota):
      for e in self.estudiantes:
        if e.id == id_est:
          e.nota = nueva_nota
          return True
      return False

    def eliminar_estudiante(self, id_est):
      for e in self.estudiantes:
        if e.id == id_est:
          self.estudiantes.remove(e)
          return True
      return False

    def calcular_estadisticas(self):
      if not self.estudiantes:
        return None
      notas = [e.nota for e in self.estudiantes]
      return {
        "promedio": sum(notas) / len(notas),
        "maximo": max(notas),
        "minimo": min(notas)
      }

    def clasificar_aprobados(self, umbral=70):
      aprobados = [e for e in self.estudiantes if e.nota >= umbral]
      reprobados = [e for e in self.estudiantes if e.nota < umbral]
      return {"aprobados": aprobados, "reprobados": reprobados}

    def distribucion_porcentual(self):
      if not self.estudiantes:
        return {}
      total = len(self.estudiantes)
      porcentajes = {}
      for e in self.estudiantes:
        rangos = {"0-59": 0, "60-79": 0, "80-100": 0}
        for e in self.estudiantes:
          if e.nota <= 60:
            rangos["0-59"] += 1
          elif e.nota <= 80:
            rangos["60-79"] += 1
          else:
            rangos["80-100"] += 1
            porcentajes = {k: v / total * 100 for k, v in rangos.items()}
      return porcentajes

    def buscar_por_nombre(self, texto):
      texto = texto.lower()
      return [e for e in self.estudiantes if e.nombre.lower().startwith(texto)]
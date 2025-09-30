#CLASE ESTUDIANTE

class Estudiante:  # representacion de un estudiante con id, nombre y nota.

    def __init__(self, id, nombre, nota):
        self.id = id_est
        self.nombre = nombre
        self.nota = nota

    @property
    def id(self):
        return self._id

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("La nota debe ser un número")
        if valor < 0 or valor > 100:
            raise ValueError("La nota debe estar entre 0 y 10")
        self._nota = valor

    def __str__(self):
        return f"[ID: {self.id}] {self.nombre} - Nota: {self.nota:.2f}"

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "nota": self.nota
        }
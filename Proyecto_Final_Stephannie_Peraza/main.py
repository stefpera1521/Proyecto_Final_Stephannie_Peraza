from gestor import Gestor_Estudiante
from repositorio import RepositorioCSV
from interfaz import InterfazConsola

if __name__ == "__main__":
    gestor = Gestor_Estudiante()
    repo = RepositorioCSV("estudiantes.csv")
    repo.cargar(gestor)
    interfaz = InterfazConsola(gestor, repo)
    interfaz.mostrar_menu()
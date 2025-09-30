# CLASE INTERFAZ_CONSOLA

class InterfazConsola: #Manejo de la interaccion en consola y con el usuario final

    def __init__(self, gestor, repositorio):
        self.gestor = gestor
        self.repositorio = repositorio

    def mostrar_menu(self):
        opciones = {
            "1": self.registrar_estudiante,
            "2": self.listar_estudiantes,
            "3": self.editar_nota,
            "4": self.eliminar_estudiante,
            "5": self.mostrar_estadisticas,
            "6": self.clasificar_estudiantes,
            "7": self.distribucion_notas,
            "8": self.buscar_estudiante,
            "9": self.salir
        }
        while True:
            print("\n--- Menú de Gestión Académica ---")
            for k, v in opciones.items():
                print(f"{k}. {v.__name__.replace('_', ' ').capitalize()}")
            eleccion = input("Seleccione una opción: ").strip()
            accion = opciones.get(eleccion)
            if accion:
                try:
                    accion()
                except Exception as e:
                    print(f"Error inesperado: {e}")
            else:
                print("Opción inválida, intente de nuevo.")

    def registrar_estudiante(self):
        try:
            nombre = input("Nombre del estudiante: ").strip()
            if not nombre:
                print("El nombre no puede estar vacío.")
                return
            nota = float(input("Nota (0-100): "))
            self.gestor.agregar_estudiante(nombre, nota)
            print("Estudiante registrado.")
        except ValueError:
            print("Entrada inválida. Debe ingresar un número válido para la nota.")

    def listar_estudiantes(self):
        criterio = input("Ordenar por (nombre/nota/id): ").strip().lower()
        estudiantes = self.gestor.listar_estudiantes(criterio)
        if estudiantes:
            print("\n Lista de estudiantes:")
            for e in estudiantes:
                print(e)
        else:
            print("No hay estudiantes registrados.")

    def editar_nota(self):
        try:
            id_est = int(input("ID del estudiante: "))
            nueva_nota = float(input("Nueva nota (0-100): "))
            if self.gestor.editar_nota(id_est, nueva_nota):
                print("Nota actualizada.")
            else:
                print("Estudiante no encontrado.")
        except ValueError:
            print("Entrada inválida.")

    def eliminar_estudiante(self):
        try:
            id_est = int(input("ID del estudiante a eliminar: "))
            if self.gestor.eliminar_estudiante(id_est):
                print("Estudiante eliminado.")
            else:
                print("Estudiante no encontrado.")
        except ValueError:
            print("Entrada inválida. Debe ingresar un número de ID.")

    def mostrar_estadisticas(self):
        stats = self.gestor.calcular_estadisticas()
        if stats:
            print(f"\n Estadísticas:")
            print(f"- Promedio: {stats['promedio']:.2f}")
            print(f"- Nota máxima: {stats['maxima']}")
            print(f"- Nota mínima: {stats['minima']}")
        else:
            print("No hay estudiantes registrados.")

    def clasificar_estudiantes(self):
        try:
            umbral = float(input("Umbral de aprobación (ej. 70): "))
            clasificacion = self.gestor.clasificar_aprobados(umbral)
            print("\n Aprobados:")
            for e in clasificacion["aprobados"]:
                print(e)
            print("\n Reprobados:")
            for e in clasificacion["reprobados"]:
                print(e)
        except ValueError:
            print("Entrada inválida.")

    def distribucion_notas(self):
        distribucion = self.gestor.distribucion_porcentual()
        if distribucion:
            print("\n Distribución porcentual de notas:")
            for rango, porcentaje in distribucion.items():
                print(f"{rango}: {porcentaje:.2f}%")
        else:
            print("No hay estudiantes registrados.")

    def buscar_estudiante(self):
        nombre = input("Buscar por nombre o inicial: ").strip()
        if not nombre:
            print("El criterio de búsqueda no puede estar vacío.")
            return
        resultados = self.gestor.buscar_por_nombre(nombre)
        if resultados:
            print("\nResultados de búsqueda:")
            for e in resultados:
                print(e)
        else:
            print("No se encontraron coincidencias.")

    def salir(self):
        self.repositorio.guardar(self.gestor)
        print("Datos guardados. ¡Hasta luego!")
        exit()
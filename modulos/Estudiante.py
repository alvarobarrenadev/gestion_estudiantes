class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.notas = {} # Diccionario para almacenar las notas
    
    def agregar_nota(self, asignatura, nota):
        # Verificar que la asignatura no esté vacía
        if not asignatura or not isinstance(asignatura, str):
            print("Error: El nombre de la asignatura no puede estar vacío.")
            return # Detener la ejecución si hay error
        
        # Verificar que la nota sea un número
        if not isinstance(nota, float) and not isinstance(nota, int):
            print("Error: La nota debe ser un número.")
            return # Detener la ejecución si hay error
        
        # Verificar que la nota esté entre el 0 y 10
        if not (0 <= nota <= 10):
            print("Error: La nota debe estar entre 0 y 10.")
            return # Detener la ejecución si hay error
        
        # key: asignatura - value nota
        self.notas[asignatura] = nota # Agregar la nota al diccionario
        print("\n-------------------------")
        print("¡Nota agregada con éxito!")
        print("-------------------------\n")

    def calcular_promedio(self):
        if len(self.notas) == 0: # Si no hay notas, retornar 0
            return 0
        else:
            return sum(self.notas.values()) / len(self.notas)
        
    def mostrar_notas(self):
        if len(self.notas) == 0: # Si no hay notas, mostrar mensaje
            print(f"\n{self.nombre.title()} no tiene notas registradas.\n")
            return # Detener la ejecución si no hay notas
        else:
            print(f"\nLas notas de {self.nombre.title()} son: ")
            # Recorrer el diccionario de notas y mostrarlas
            for indice, (asignatura, nota) in enumerate(self.notas.items()):
                print(f"{indice+1}. {asignatura.title()}: {nota}")
            print() # Salto de línea


    def actualizar_nota(self, asignatura, nota):
        if asignatura in self.notas: # Verificar si la asignatura existe
            self.notas[asignatura] = nota # Actualizar la nota
            print(f"\nLa nota de la asignatura '{asignatura.title()}' ha sido actualizada correctamente.\n")
        else:
            print(f"\nError: La asignatura '{asignatura.title()}' no existe.\n")
            return # Detener la ejecución si hay error

    def eliminar_asignatura(self, asignatura):
        if asignatura in self.notas: # Verificar si la asignatura existe
            self.notas.pop(asignatura) # Eliminar la asignatura
            print(f"\nLa asignatura '{asignatura.title()}' ha sido eliminada correctamente.\n")
        else:
            print(f"\Error: La asignatura '{asignatura.title()}' no existe.\n")
            return # Detener la ejecución si hay error
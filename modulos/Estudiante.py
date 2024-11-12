# Ejercicio 1: Gestión de Estudiantes y Notas

# Objetivo: Crear una clase Estudiante con atributos y métodos que permitan gestionar notas usando listas y diccionarios.

# 1.Crea una clase Estudiante con los atributos:
#   - nombre (str)
#   - edad (int)
#   - notas (un diccionario donde las claves sean nombres de asignaturas y los valores sean las notas).

# 2. Agrega métodos a la clase para:
#   - agregar_nota(asignatura, nota): agrega o actualiza la nota de una asignatura.
#   - calcular_promedio(): calcula y devuelve el promedio de las notas.

# 3. Crea una lista de estudiantes y agrega varias instancias de la clase Estudiante. Llena sus notas y calcula el promedio de cada uno.

# 4. Finalmente, crea una función que reciba la lista de estudiantes y devuelva un diccionario con el nombre de cada estudiante como clave y su promedio como valor.

class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.notas = {}
    
    def agregar_nota(self, asignatura, nota):
        # Verificar que la asignatura no esté vacía
        if not asignatura or not isinstance(asignatura, str):
            print("Error: El nombre de la asignatura no puede estar vacío.")
            return # Detener la ejecución si hay error
        
        # Verificar que la nota sea un número
        if not isinstance(nota, int):
            print("Error: La nota debe ser un número.")
            return # Detener la ejecución si hay error
        
        # Verificar que la nota esté entre el 0 y 10
        if not (0 <= nota <= 10):
            print("Error: La nota debe estar entre 0 y 10.")
            return # Detener la ejecución si hay error
        
        # key: asignatura - value nota
        self.notas[asignatura] = nota 
        print("Nota agregada correctamente")

    def calcular_promedio(self):
        if len(self.notas) == 0:
            return 0
        else:
            return sum(self.notas.values()) / len(self.notas)
        
    def mostrar_notas(self):
        print(f"\nLas notas del estudiante {self.nombre} son: ")
        for indice, (k, v) in enumerate(self.notas.items()):
            print(f"{indice+1}. Asignatura: {k} - Nota: {v}")


    def actualizar_nota(self, asignatura, nota):
        if asignatura in self.notas:
            self.notas[asignatura] = nota
            print(f"Nota de la asignatura '{asignatura}' actualizada correctamente.")
        else:
            print(f"Error: La asignatura '{asignatura}' no existe.")
            return # Detener la ejecución si hay error

    def eliminar_nota(self, asignatura):
        if asignatura in self.notas:
            self.notas.pop(asignatura)
            print(f"Nota de la asignatura '{asignatura}' eliminada correctamente.")
        else:
            print(f"Error: La asignatura '{asignatura}' no existe.")
            return # Detener la ejecución si hay error
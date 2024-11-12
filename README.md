# Gestión de Notas y Estudiantes

Este proyecto permite gestionar las notas de los estudiantes, incluyendo la adición, actualización, eliminación y visualización de notas, así como el cálculo del promedio de las mismas.

## Características

- Añadir un estudiante con nombre y edad.
- Agregar notas a diferentes asignaturas.
- Calcular el promedio de las notas.
- Mostrar todas las notas de un estudiante.
- Actualizar una nota existente.
- Eliminar una nota de una asignatura específica.

## Requisitos

- Python 3.13

## Instalación

1. Clona el repositorio:
    ```sh
    git clone https://github.com/alvarobarrena02/gestion_estudiantes.git
    cd gestion_estudiantes
    ```

## Uso

1. Ejecuta el script principal:
    ```sh
    python main.py
    ```

2. Sigue las opciones del menú para gestionar las notas de los estudiantes.

## Menú de Opciones

- `0`: Añadir un estudiante.
- `1`: Agregar una nota.
- `2`: Calcular el promedio de las notas.
- `3`: Mostrar todas las notas.
- `4`: Actualizar una nota.
- `5`: Eliminar una nota.
- `6`: Salir del programa.

## Ejemplo de Uso

```python
# Agrego notas y asignaturas a la lista
estudiante1.agregar_nota("Programación", 8)
estudiante1.agregar_nota("Bases de datos", 6)
estudiante1.agregar_nota("Desarrollo cliente", 9)

# Muestro las notas y el promedio
estudiante1.mostrar_notas()
promedio = estudiante1.calcular_promedio()
print(f"\nPromedio: {promedio:.2f}")

# Elimino una nota
estudiante1.eliminar_nota("Programación")
estudiante1.mostrar_notas()

# Actualizo una nota
estudiante1.actualizar_nota("Bases de datos", 10)
estudiante1.mostrar_notas()
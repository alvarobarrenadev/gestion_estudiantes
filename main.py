from modulos.Estudiante import Estudiante
from modulos import funciones

funciones.limpiar_consola() # Limpio la consola
funciones.ver_menu() # Muestro el menú

while True:
    opcion = input("Introduce una opción (0-6): ")

    match opcion:
        case '0': # Crear estudiante
            nombre = input("Introduce tu nombre: ").lower()
            edad = int(input("Introduce tu edad: "))
            print("\n-----------------------------")
            print("¡Estudiante creado con éxito!")
            print("-----------------------------\n")
            estudiante = Estudiante(nombre, edad)
            funciones.ver_menu()
        
        case '1': # Agregar nota
            asignatura = input("Introduce una asignatura: ")
            nota = float(input("Introduce una nota: "))
            estudiante.agregar_nota(asignatura, nota)
            funciones.ver_menu()

        case '2': # Calcular promedio
            promedio = estudiante.calcular_promedio()
            print("\n-----------------------------")
            print(f"El promedio de notas es de: {promedio:.0f}")
            print("-----------------------------\n")
            funciones.ver_menu()

        case '3': # Mostrar notas
            estudiante.mostrar_notas()
            funciones.ver_menu()
        
        
        case '4': # Actualizar nota
            asignatura = input("Introduce una asignatura: ")
            nota = float(input("Introduce una nota: "))
            estudiante.actualizar_nota(asignatura, nota)
            funciones.ver_menu()
        
        case '5': # Eliminar asignatura
            asignatura = input("Introduce una asignatura: ")
            estudiante.eliminar_asignatura(asignatura)
            funciones.ver_menu()
        
        case '6': # Salir del programa
            print("Saliendo del programa...")
            break

        case _:
            print("Opción no encontrada, vuelve a intentarlo.\n")
            funciones.ver_menu()
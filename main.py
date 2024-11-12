from modulos import Estudiante
from modulos import menu

menu.ver_menu()
# Instancio la clase estudiante
# estudiante1 = Estudiante("Juan", 18)

while True:
    opcion = input("Introduce una opción: ")

    match opcion:
        case '0':
            nombre = input("Introduce tu nombre: ")
            edad = int(input("Introduce tu edad: "))
            estudiante = Estudiante(nombre, edad)
        
        case '1':
            asignatura = input("Introduce una asignatura: ")
            nota = int(input("Introduce una nota: "))

            estudiante.agregar_nota(asignatura, nota)

        case '2':
            pass
        
        case '3':
            pass
        
        case '4':
            pass
        
        case '5':
            pass

        case _:
            print("Opción no encontrada, vuelve a intentarlo")


"""
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
"""
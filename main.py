
def main():

    while True:
        print("--------------------------------------------------")
        print("            Mi Administrador de Tareas            ")
        print("--------------------------------------------------")
        print("1. Agregar tarea")
        print("2. Marcar tarea \"en progreso\" ")
        print("3. Terminar una tarea")
        print("4. Ver listas de tareas")
        print("5. Ver información")
        print("6. Salir")
        print("--------------------------------------------------")
        respuesta = input("Ingresa la acción que quieras realizar: ")
        print()

        if respuesta == "1":
            agregar_tarea()
        elif respuesta == "2":
            tarea_enProgreso()
        elif respuesta == "3":
            terminar_tarea()
        elif respuesta == "4":
            ver_tareas()
        elif respuesta == "5":
            ver_informacion()
        elif respuesta == "6":
            print("¡Hasta luego!")
            print()
            break
        else:
            print("Opción inválida. Inténtalo de nuevo")

def agregar_tarea():
    pass

def tarea_enProgreso():
    pass

def terminar_tarea():
    pass

def ver_tareas():
    pass

def ver_informacion():
    pass

if __name__ == "__main__":
    main()

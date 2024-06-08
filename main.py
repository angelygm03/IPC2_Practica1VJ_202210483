import os
import graphviz
from listaTareas import ListaTareas

def main():
    lista_tareas = ListaTareas()
    while True:
        print("------------------------------------------------------------")
        print("                 Mi Administrador de Tareas                 ")
        print("------------------------------------------------------------")
        mostrar_tareas_menu(lista_tareas)
        print("1. Agregar tarea")
        print("2. Marcar tarea \"en progreso\" ")
        print("3. Terminar una tarea")
        print("4. Ver listas de tareas")
        print("5. Ver información")
        print("6. Salir")
        print("------------------------------------------------------------")
        respuesta = input("Ingresa la acción que quieras realizar: ")
        print()

        if respuesta == "1":
            agregar_tarea(lista_tareas)
        elif respuesta == "2":
            tarea_enProgreso(lista_tareas)
        elif respuesta == "3":
            terminar_tarea(lista_tareas)
        elif respuesta == "4":
            ver_tareas(lista_tareas)
        elif respuesta == "5":
            ver_informacion()
        elif respuesta == "6":
            print("¡Hasta luego!")
            print()
            break
        else:
            print("Opción inválida. Inténtalo de nuevo")

def mostrar_tareas_menu(lista_tareas):
    if lista_tareas.header is None:
        print("                ¡No hay tareas registradas!")
        print("------------------------------------------------------------")
    else:
        actual = lista_tareas.header
        while actual:
            tarea = actual.tarea
            print(f"\n ID: {tarea.id} \n Nombre: {tarea.nombre} \n Descripción: {tarea.descripcion} \n Estado: {tarea.estado}")
            print("------------------------------------------------------------")
            actual = actual.siguiente

def agregar_tarea(lista_tareas):
    print("------------------------------------------------------------")
    print("                        Nueva Tarea                         ")
    print("------------------------------------------------------------")
    nombre = input("Ingrese el nombre de la tarea: ")
    descripcion = input("Ingrese la descripción de la tarea: ")
    lista_tareas.agregar_tarea(nombre, descripcion)
    print()
    print("¡Tarea creada con éxito!")

def tarea_enProgreso(lista_tareas):
    if lista_tareas.header is None:
        print("¡No hay tareas registradas!")
    else:
        id_tarea = int(input("Ingrese el ID de la tarea: "))
        if lista_tareas.marcar_en_progreso(id_tarea):
            print(f"La tarea {id_tarea} ha sido marcada como 'En Progreso'.")
        else:
            print(f"No se encontró una tarea con el ID {id_tarea}.")

def terminar_tarea(lista_tareas):
    if lista_tareas.header is None:
        print("¡No hay tareas registradas!")
    else:
        print("------------------------------------------------------------")
        print("                      Eliminar Tarea                        ")
        print("------------------------------------------------------------")
        id_tarea = int(input("Ingrese el ID de la tarea: "))
        print()
        if lista_tareas.eliminar_tarea(id_tarea):
            print(f"La tarea {id_tarea} ha sido eliminada.")
            print()
        else:
            print(f"No se encontró una tarea con el ID {id_tarea}.")
            print()

def ver_tareas(lista_tareas):
    lista_tareas.generar_grafico()
    print("Generando imagen...")
    os.system("lista_tareas.png")

def ver_informacion():
    pass

if __name__ == "__main__":
    main()

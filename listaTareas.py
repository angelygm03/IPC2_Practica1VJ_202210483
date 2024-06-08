from tarea import Tarea
from nodo import Nodo
import graphviz

class ListaTareas:
    def __init__(self):
        self.header = None
        self.id_actual = 1

    def agregar_tarea(self, nombre, descripcion):
        nueva_tarea = Tarea(self.id_actual, nombre, descripcion, "Pendiente")
        nuevo_nodo = Nodo(nueva_tarea)
        if not self.header:
            self.header = nuevo_nodo
        else:
            actual = self.header
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
        self.id_actual += 1
        print(f"La tarea '{nombre}' fue agregada con el ID {self.id_actual - 1} a la lista")  #verificar que se agrega a la lista

    def marcar_en_progreso(self, id_tarea):
        actual = self.header
        while actual:
            if actual.tarea.id == id_tarea:
                actual.tarea.estado = "En Progreso"
                return True
            actual = actual.siguiente
        return False
    
    def eliminar_tarea(self, id_tarea):
        actual = self.header
        anterior = None
        while actual:
            if actual.tarea.id == id_tarea:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.header = actual.siguiente
                return True
            anterior = actual
            actual = actual.siguiente
        return False
    
    def generar_grafico(self):
        dot = graphviz.Digraph(comment='Lista de Tareas', format='png')
        dot.attr(rankdir='LR')  # orientación horizontal
        actual = self.header
        while actual:
            tarea = actual.tarea
            label = f"ID: {tarea.id}\nNombre: {tarea.nombre}\nDescripción: {tarea.descripcion}\nEstado: {tarea.estado}"
            dot.node(str(tarea.id), label, shape='box')
            if actual.siguiente:
                dot.edge(str(tarea.id), str(actual.siguiente.tarea.id))
            actual = actual.siguiente
        dot.render('lista_tareas', cleanup=True)
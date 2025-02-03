from collections import namedtuple
import heapq

from collections import namedtuple
import heapq

# Definimos una estructura de datos para representar una tarea
Tarea = namedtuple("Tarea", ["nombre", "duracion", "costo"])

class Planificacion:
    def __init__(self, presupuesto):
        self.presupuesto = presupuesto
        self.tareas = []
    
    def agregar_tarea(self, nombre, duracion, costo):
        """Agrega una tarea al sistema."""
        tarea = Tarea(nombre, duracion, costo)
        heapq.heappush(self.tareas, (duracion, costo, tarea))
    
    def planificar_tareas(self):
        """Devuelve la planificación óptima de tareas dentro del presupuesto."""
        planificacion = []
        costo_total = 0
        
        # Las tareas ya están ordenadas por heapq (por duración y costo)
        for duracion, costo, tarea in self.tareas:
            if costo_total + costo <= self.presupuesto:
                planificacion.append(tarea)
                costo_total += costo
            else:
                break
        
        return planificacion, costo_total

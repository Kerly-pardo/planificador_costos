import unittest
from planificacion import Planificacion

class TestPlanificacion(unittest.TestCase):

    def test_agregar_tarea(self):
        planificador = Planificacion(1000)
        planificador.agregar_tarea("Tarea 1", 5, 200)
        self.assertEqual(len(planificador.tareas), 1)

    def test_planificar_tareas(self):
        planificador = Planificacion(1000)
        planificador.agregar_tarea("Tarea 1", 5, 200)
        planificador.agregar_tarea("Tarea 2", 3, 300)
        planificador.agregar_tarea("Tarea 3", 2, 500)
        plan, costo_total = planificador.planificar_tareas()
        self.assertEqual(len(plan), 2)
        self.assertEqual(costo_total, 500)

if __name__ == '__main__':
    unittest.main()

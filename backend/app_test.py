import unittest
import json
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_planificar(self):
        response = self.app.post('/planificar', 
                                 data=json.dumps({
                                     "presupuesto": 1000,
                                     "tareas": [
                                         {"nombre": "Tarea 1", "duracion": 5, "costo": 200},
                                         {"nombre": "Tarea 2", "duracion": 3, "costo": 300},
                                         {"nombre": "Tarea 3", "duracion": 2, "costo": 500}
                                     ]
                                 }),
                                 content_type='application/json')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertIn('plan', data)
        self.assertIn('costo_total', data)

if __name__ == '__main__':
    unittest.main()

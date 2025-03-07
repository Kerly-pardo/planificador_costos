# backend/app.py
from flask import Flask, request, jsonify
from flask_cors import CORS  # Importar CORS aquí
from planificacion import Planificacion

app = Flask(__name__)
CORS(app)  # Habilitar CORS después de crear la instancia de Flask

@app.route('/planificar', methods=['POST'])
def planificar():
    try:
        data = request.json
        presupuesto = data.get('presupuesto')
        tareas = data.get('tareas')

        if not presupuesto or not tareas:
            return jsonify({"error": "Faltan datos en la solicitud."}), 400

        # Validar tipos de datos
        if not isinstance(presupuesto, int) or not all(isinstance(t['costo'], int) and isinstance(t['duracion'], int) for t in tareas):
            return jsonify({"error": "Datos inválidos."}), 400

        planificador = Planificacion(presupuesto)
        for tarea in tareas:
            planificador.agregar_tarea(tarea['nombre'], tarea['duracion'], tarea['costo'])

        plan, costo_final = planificador.planificar_tareas()
        return jsonify({
            'plan': [{'nombre': t.nombre, 'duracion': t.duracion, 'costo': t.costo} for t in plan],
            'costo_total': costo_final
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

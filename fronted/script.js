// frontend/script.js
const tareas = [];

// Función para agregar una tarea
function agregarTarea() {
    const nombre = prompt("Nombre de la tarea:");
    const duracion = prompt("Duración (días):");
    const costo = prompt("Costo:");

    // Validar que todos los campos estén completos
    if (nombre && duracion && costo) {
        // Agregar la tarea al array
        tareas.push({ nombre, duracion: parseInt(duracion), costo: parseInt(costo) });
        console.log(tareas); // Verificar que la tarea se ha agregado
        mostrarTareas(); // Mostrar las tareas actuales
    } else {
        alert("Por favor, completa todos los campos.");
    }
}

// Función para mostrar las tareas en el DOM
function mostrarTareas() {
    const tasksDiv = document.getElementById('tasks');
    tasksDiv.innerHTML = ''; // Limpiar la lista de tareas

    // Mostrar cada tarea en el div
    tareas.forEach((tarea, index) => {
        tasksDiv.innerHTML += `
            <p>
                ${tarea.nombre} - Duración: ${tarea.duracion} días, Costo: $${tarea.costo} 
                <button onclick="eliminarTarea(${index})">Eliminar</button>
            </p>`;
    });
}

// Función para eliminar una tarea
function eliminarTarea(index) {
    tareas.splice(index, 1); // Eliminar la tarea del array
    mostrarTareas(); // Actualizar la visualización de tareas
}

// Evento para manejar el envío del formulario
document.getElementById('taskForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevenir el comportamiento por defecto del formulario
    const presupuesto = document.getElementById('presupuesto').value;

    // Validación del presupuesto
    if (presupuesto <= 0) {
        alert("El presupuesto debe ser un valor positivo.");
        return;
    }

    fetch('http://127.0.0.1:5000/planificar', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ presupuesto: parseInt(presupuesto), tareas })
    })
    .then(response => response.json())
    .then(data => {
        // Insertar los resultados en la tabla
        const tablaResultado = document.getElementById('tabla-planificacion').getElementsByTagName('tbody')[0];
        tablaResultado.innerHTML = ''; // Limpiar tabla

        data.plan.forEach(tarea => {
            const row = tablaResultado.insertRow();
            row.innerHTML = `
                <td>${tarea.nombre}</td>
                <td>${tarea.duracion}</td>
                <td>$${tarea.costo}</td>
            `;
        });

        // Mostrar el costo total
        const costoTotalDiv = document.getElementById('costoTotal');
        costoTotalDiv.innerHTML = `<strong>Costo total del proyecto: $${data.costo_total}</strong>`;
    })
    .catch(error => {
        console.error('Error al enviar los datos:', error);
    });
});

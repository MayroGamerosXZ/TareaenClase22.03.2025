# TareaenClase22.03.2025
# Sistema de Gestión de Tareas y Atención al Cliente

Este proyecto implementa un sistema de gestión de tareas y atención al cliente. El sistema maneja diferentes niveles de prioridad para tareas y clientes VIP, asegurando que se atiendan según su importancia.

## Contenido

- [Funcionalidad](#funcionalidad)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Clases y Funciones](#clases-y-funciones)
- [Ejemplo de Uso](#ejemplo-de-uso)
- [Contribuciones](#contribuciones)

## Funcionalidad

- **Gestión de Tareas**: El sistema puede manejar múltiples tareas con diferentes niveles de prioridad.
- **Atención al Cliente**: El sistema distingue entre clientes VIP y clientes regulares, atendiendo primero a los VIP.

## Estructura del Proyecto

- `CustomQueue.py`: Implementación de una cola personalizada para gestionar tareas y clientes.
- `TaskManagerX.py`: Gestor de tareas que maneja prioridades.
- `CustomerServiceX.py`: Simulación de un sistema de atención al cliente que distingue entre VIP y clientes regulares.
- `main.py`: Archivo principal que ejecuta el sistema.
- `README.md`: Documentación del proyecto.

## Clases y Funciones

### CustomQueue

Una cola personalizada para manejar tareas y clientes.

- `enqueue(task)`: Agrega una tarea o cliente a la cola.
- `dequeue()`: Quita y devuelve la primera tarea o cliente de la cola.
- `is_empty()`: Comprueba si la cola está vacía.

### TaskManagerX

Gestor de tareas con prioridad.

- `add_task(task)`: Agrega una tarea con un nivel de prioridad específico.
- `process_tasks()`: Procesa las tareas en orden de prioridad.

### CustomerServiceX

Simulación de un sistema de atención al cliente.

- `add_customer(customer, vip=False)`: Agrega un cliente a la cola de atención.
- `serve_customer()`: Atiende a los clientes en orden de prioridad, dando preferencia a los VIP.

## Ejemplo de Uso

### Ejecutar el sistema

1. Ejecuta el archivo `main.py`:
   ```sh
   python main.py

###Salida de Ejemplo
Processing task: Task 8 (Priority: Baja)

Serving customers:
Atendiendo a cliente VIP: Nico Robin
Atendiendo a cliente VIP: Monkey D Luffy
Atendiendo a cliente VIP: Zoro Roronoa
Atendiendo a cliente VIP: Vinsmoke Sanji
Serving regular customer: Ussop
Serving regular customer: Nami
Serving regular customer: Brook
Serving regular customer: Chopper
Serving regular customer: Jimbei
Serving regular customer: Franky


Contribuciones
Las contribuciones son bienvenidas. Si tienes alguna sugerencia o mejora, no dudes en abrir un issue o enviar un pull request.

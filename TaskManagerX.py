from CustomQueue import CustomQueue


class TaskManagerX:
    """Gestor de tareas con prioridad."""

    def __init__(self):
        self.task_queue = CustomQueue()

    def add_task(self, task):
        """Agrega una tarea con un nivel de prioridad específico."""
        task_info = {
            'Nombre': task.get('Nombre'),
            'Edad': task.get('Edad'),
            'DPI': task.get('DPI'),
            'Tipo de Sangre': task.get('Tipo de Sangre'),
            'Prioridad': task.get('Prioridad')
        }
        self.task_queue.enqueue(task_info)

    def process_tasks(self):
        """Procesa las tareas en orden de prioridad."""
        priorities = {'Crítica': 3, 'Media': 2, 'Baja': 1}
        tasks = []
        while not self.task_queue.is_empty():
            task = self.task_queue.dequeue()
            tasks.append(task)

        tasks.sort(key=lambda x: priorities[x['Prioridad']], reverse=True)

        for task in tasks:
            print(f"Processing task: {task['Nombre']} (Priority: {task['Prioridad']})")


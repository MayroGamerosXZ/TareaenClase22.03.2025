class CustomQueue:
    """Una cola personalizada para manejar tareas."""
    def __init__(self):
        self.queue = []

    def enqueue(self, task):
        """Agrega una tarea a la cola."""
        self.queue.append(task)

    def dequeue(self):
        """Quita y devuelve la primera tarea de la cola."""
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def is_empty(self):
        """Comprueba si la cola está vacía."""
        return len(self.queue) == 0

    def peek(self):
        """Muestra la primera tarea de la cola sin quitarla."""
        if not self.is_empty():
            return self.queue[0]
        return None
from CustomQueue import CustomQueue


class CustomerServiceX:
    """Simulación de un sistema de atención al cliente."""

    def __init__(self):
        self.customer_queue = CustomQueue()

    def add_customer(self, customer, vip=False):
        """Agrega un cliente a la cola."""
        customer_info = {
            'Nombre': customer.get('Nombre'),
            'Edad': customer.get('Edad'),
            'DPI': customer.get('DPI'),
            'Tipo de Sangre': customer.get('Tipo de Sangre'),
            'VIP': vip
        }
        self.customer_queue.enqueue(customer_info)

    def serve_customer(self):
        """Atiende a los clientes en orden de prioridad."""
        if not self.customer_queue.is_empty():
            customers = []
            while not self.customer_queue.is_empty():
                customer = self.customer_queue.dequeue()
                customers.append(customer)

            customers.sort(key=lambda x: x['VIP'], reverse=True)

            for customer in customers:
                if customer['VIP']:
                    print(f"Atendiendo a cliente VIP: {customer['Nombre']}")
                else:
                    print(f"Serving regular customer: {customer['Nombre']}")
        else:
            print("No customers to serve")
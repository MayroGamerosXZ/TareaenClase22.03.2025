from TaskManagerX import TaskManagerX
from CustomerServiceX import CustomerServiceX

def run_task_manager():
    task_manager = TaskManagerX()
    task_manager.add_task({
        'Nombre': 'Task 1',
        'Edad': 20,
        'DPI': 1234567890,
        'Tipo de Sangre': 'O',
        'Prioridad': 'Baja'
    })
    task_manager.add_task({
        'Nombre': 'Task 2',
        'Edad': 25,
        'DPI': 9876543210,
        'Tipo de Sangre': 'A',
        'Prioridad': 'Baja'
    })
    task_manager.add_task({
        'Nombre': 'Task 3',
        'Edad': 30,
        'DPI': 1122334455,
        'Tipo de Sangre': 'B',
        'Prioridad': 'Crítica'
    })
    task_manager.add_task({
        'Nombre': 'Task 4',
        'Edad': 35,
        'DPI': 6677889900,
        'Tipo de Sangre': 'AB',
        'Prioridad': 'Crítica'
    })
    task_manager.add_task({
        'Nombre': 'Task 5',
        'Edad': 40,
        'DPI': 1234567890,
        'Tipo de Sangre': 'O',
        'Prioridad': 'Crítica'
    })
    task_manager.add_task({
        'Nombre': 'Task 6',
        'Edad': 45,
        'DPI': 9876543210,
        'Tipo de Sangre': 'A',
        'Prioridad': 'Crítica'
    })
    task_manager.add_task({
        'Nombre': 'Task 7',
        'Edad': 50,
        'DPI': 1122334455,
        'Tipo de Sangre': 'B',
        'Prioridad': 'Media'
    })
    task_manager.add_task({
        'Nombre': 'Task 8',
        'Edad': 55,
        'DPI': 6677889900,
        'Tipo de Sangre': 'AB',
        'Prioridad': 'Baja'
    })
    task_manager.add_task({
        'Nombre': 'Task 9',
        'Edad': 60,
        'DPI': 1234567890,
        'Tipo de Sangre': 'O',
        'Prioridad': 'Media'
    })
    task_manager.add_task({
        'Nombre': 'Task 10',
        'Edad': 65,
        'DPI': 9876543210,
        'Tipo de Sangre': 'A',
        'Prioridad': 'Media'
    })

    print("Processing tasks:")
    task_manager.process_tasks()

def run_customer_service():
    customer_service = CustomerServiceX()
    customer_service.add_customer({
        'Nombre': 'Ussop',
        'Edad': 20,
        'DPI': 1234567890,
        'Tipo de Sangre': 'O'
    })
    customer_service.add_customer({
        'Nombre': 'Nami',
        'Edad': 25,
        'DPI': 9876543210,
        'Tipo de Sangre': 'A'
    })
    customer_service.add_customer({
        'Nombre': 'Nico Robin',
        'Edad': 30,
        'DPI': 1122334455,
        'Tipo de Sangre': 'B'
    }, vip=True)
    customer_service.add_customer({
        'Nombre': 'Monkey D Luffy',
        'Edad': 35,
        'DPI': 6677889900,
        'Tipo de Sangre': 'AB'
    }, vip=True)
    customer_service.add_customer({
        'Nombre': 'Zoro Roronoa',
        'Edad': 40,
        'DPI': 1234567890,
        'Tipo de Sangre': 'O'
    }, vip=True)
    customer_service.add_customer({
        'Nombre': 'Vinsmoke Sanji',
        'Edad': 45,
        'DPI': 9876543210,
        'Tipo de Sangre': 'A'
    }, vip=True)
    customer_service.add_customer({
        'Nombre': 'Brook',
        'Edad': 50,
        'DPI': 1122334455,
        'Tipo de Sangre': 'B'
    })
    customer_service.add_customer({
        'Nombre': 'Chopper',
        'Edad': 55,
        'DPI': 6677889900,
        'Tipo de Sangre': 'AB'
    })
    customer_service.add_customer({
        'Nombre': 'Jimbei',
        'Edad': 60,
        'DPI': 1234567890,
        'Tipo de Sangre': 'O'
    })
    customer_service.add_customer({
        'Nombre': 'Franky',
        'Edad': 65,
        'DPI': 9876543210,
        'Tipo de Sangre': 'A'
    })

    print("\nServing customers:")
    customer_service.serve_customer()

run_task_manager()
run_customer_service()
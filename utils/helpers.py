import time

def generate_unique_employee_id():
    # Gera um ID baseado no timestamp atual para garantir unicidade
    return str(int(time.time()))

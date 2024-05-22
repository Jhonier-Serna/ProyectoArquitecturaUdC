from Class.Register import Register


# Clase RegisterBank (Banco de Registros)
# Responsabilidades:
# - Almacena y gestiona múltiples registros.
# - Proporciona métodos para obtener y establecer valores en los registros.
class RegisterBank:
    def __init__(self, canvas, x, y):
        # Crea una serie de registros numerados y los almacena en un diccionario.
        self.registers = {f'R{i}': Register(canvas, x, y + i * 30, f'R{i}') for i in range(1, 10)}

    def get(self, reg_name):
        if reg_name not in self.registers:
            raise KeyError(f"Register {reg_name} not found")
        return self.registers[reg_name].value

    def set(self, reg_name, value):
        if reg_name not in self.registers:
            raise KeyError(f"Register {reg_name} not found")
        self.registers[reg_name].set_value(value)

    def clear_registers(self):
        for register in self.registers.values():
            register.set_value(0)

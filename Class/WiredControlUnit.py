# Clase WiredControlUnit (Unidad de Control Cableada)
# Responsabilidades:
# - Genera señales de control basadas en el opcode recibido.
class WiredControlUnit:
    def __init__(self):
        # El diccionario control_signals almacena las señales de control y sus estados (True/False).
        self.control_signals = {}

    # Método generate_control_signals: Genera señales de control basadas en el opcode recibido.
    # Devuelve un diccionario con las señales de control y sus estados correspondientes.
    def generate_control_signals(self, opcode):
        # Restablece las señales de control a un estado inicial.
        self.control_signals = {
            'fetch': True,
            'decode': True,
            'execute': False,
            'memory_read': False,
            'memory_write': False,
            'register_read': False,
            'register_write': False,
            'alu_operation': None,
        }

        if opcode in ['ADD', 'SUB', 'MUL', 'DIV', 'AND', 'OR', 'NOT', 'XOR']:
            self.control_signals['execute'] = True
            self.control_signals['alu_operation'] = opcode
            self.control_signals['register_read'] = True
            self.control_signals['register_write'] = True
        elif opcode == 'LOAD':
            self.control_signals['memory_read'] = True
            self.control_signals['register_write'] = True
        elif opcode == 'STORE':
            self.control_signals['memory_write'] = True
        elif opcode == 'MOVE':
            self.control_signals['register_read'] = True
            self.control_signals['register_write'] = True
        elif opcode == 'JUMP':
            self.control_signals['execute'] = True
            self.control_signals['alu_operation'] = opcode
        elif opcode == 'JUMP_IF_ZERO':
            self.control_signals['execute'] = True
            self.control_signals['alu_operation'] = opcode

        return self.control_signals

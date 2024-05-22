# Clase ALU (Unidad Aritmético-Lógica)
# Responsabilidades:
# - Realiza operaciones aritméticas (suma, resta, multiplicación, división) en función del opcode recibido.
# - Almacena el resultado de la operación en su atributo `value`.
class ALU:
    def __init__(self):
        self.value = 0

    # Método execute: Ejecuta una operación aritmética basada en el opcode y los operandos recibidos.
    # Parámetros:
    # - opcode: Código de operación que especifica qué operación realizar.
    # - operand1: Primer operando para la operación.
    # - operand2: Segundo operando para la operación.
    # - Almacena el resultado de la operación en el atributo `value`.
    def execute(self, opcode, operand1, operand2):
        if opcode == 'ADD':
            self.value = operand1 + operand2
        elif opcode == 'SUB':
            self.value = operand1 - operand2
        elif opcode == 'MUL':
            self.value = operand1 * operand2
        elif opcode == 'DIV':
            if operand2 == 0:
                self.value = 0
            else:
                self.value = operand1 / operand2

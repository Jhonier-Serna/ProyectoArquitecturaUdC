from Class.Register import Register

# Clase Memory (Memoria)
# Responsabilidades:
# - Almacena las instrucciones del programa y los datos.
# - Proporciona métodos para cargar y almacenar datos/instrucciones.
class Memory:
    def __init__(self, canvas, x, y, size):
        # La memoria se divide en dos partes: memoria de instrucciones y memoria de datos.
        self.instruction_memory = [''] * (size // 2)
        self.data_memory = {f'D{i}': Register(canvas, x, y + i * 20, f'D{i}') for i in range(0, 20)}

    # Método load_instruction: Carga una instrucción desde la memoria de instrucciones.
    # Parámetros:
    # - address: Dirección de memoria desde la cual cargar la instrucción.
    # - Devuelve la instrucción cargada.
    def load_instruction(self, address):
        if address < 0 or address >= len(self.instruction_memory):
            raise ValueError(f"Invalid memory address for instruction: {address}")
        return self.instruction_memory[address]

    # Método store_instruction: Almacena una instrucción en la memoria de instrucciones.
    # Parámetros:
    # - address: Dirección de memoria en la cual almacenar la instrucción.
    # - value: Instrucción a almacenar.
    def store_instruction(self, address, value):
        if address < 0 or address >= len(self.instruction_memory):
            raise ValueError(f"Invalid memory address for instruction: {address}")
        self.instruction_memory[address] = value


    # Método load_data: Carga un dato desde la memoria de datos.
    # Parámetros:
    # - address: Dirección de memoria en la cual cargar almacenar el dato.
    # - Devuelve el dato cargado.
    def load_data(self, address):
        if address < 0 or address >= len(self.data_memory):
            raise ValueError(f"Invalid memory address for data: {address}")
        return self.data_memory[address].value


    # Método store_instruction: Almacena un dato desde la memoria de datos.
    # Parámetros:
    # - address: Dirección de memoria en la cual almacenar la dato.
    # - value: Dato a almacenar.
    def store_data(self, address, value):
        if address < 0 or address >= len(self.data_memory):
            raise ValueError(f"Invalid memory address for data: {address}")
        self.data_memory[address].set_value(value)
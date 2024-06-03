import tkinter as tk
from tkinter import Canvas, Text

from Class.ALU import ALU
from Class.ControlUnit import ControlUnit
from Class.Memory import Memory
from Class.Register import Register
from Class.RegisterBank import RegisterBank
from Class.WiredControlUnit import WiredControlUnit


# Clase ComputerSimulator (Simulador de Computadora)
# Responsabilidades:
# - Controla la simulación de la computadora.
# - Interactúa con los elementos de la interfaz gráfica de usuario (GUI) para mostrar la simulación.
class ComputerSimulator:
    def __init__(self, root):
        # Configura la ventana de la GUI y otros elementos visuales.
        self.root = root
        self.root.title("Proyecto Final Arquitectura")
        self.root.configure(bg="#2A629A")

        # Crea y organiza los elementos de la GUI.
        self.create_widgets()
        self.create_layout()

        # Inicializa los componentes principales de la computadora.
        self.memory = Memory(256)
        self.alu = ALU()
        self.control_unit = ControlUnit()
        self.register_bank = RegisterBank(self.canvas, 300, 45)
        self.wired_control_unit = WiredControlUnit()

        # Inicializa los registros especiales de la computadora.
        self.pc_register = Register(self.canvas, 155, 50, "PC")
        self.mar_register = Register(self.canvas, 55, 50, "MAR")
        self.ir_register = Register(self.canvas, 105, 120, "IR")
        self.mbr_register = Register(self.canvas, 110, 200, "MBR")
        self.alu_text = Register(self.canvas, 105, 280, "ALU")

        # Inicializa otros elementos visuales y datos necesarios para la simulación.
        self.instructions = []
        self.control_signals_text = {}
        self.create_control_signals_display()

    # Métodos para crear y organizar los elementos de la GUI.
    def create_widgets(self):
        # Crea elementos de la GUI como lienzo, widget de texto y botón de inicio.
        self.canvas = Canvas(self.root, width=1200, height=500,
                             bg="#2A829A", highlightthickness=0)
        self.text_widget = Text(
            self.root, height=5, width=40, bg="#D8BFD8", fg="black", font=("Arial", 12))
        self.input_button = tk.Button(self.root, text="Comenzar", command=self.load_instructions,
                                      bg="#FF69B4", fg="white", font=("Arial", 12, "bold"))
        self.charge_button = tk.Button(self.root, text="Cargar Instrucciones", command=self.load_single_instructions,
                                       bg="#FF69B4", fg="white", font=("Arial", 12, "bold"))
        self.step_button = tk.Button(self.root, text="Paso a paso", command=self.execute_single_instruction,
                                     bg="#FF69B4", fg="white", font=("Arial", 12, "bold"))

    def create_layout(self):
        # Organiza los elementos de la GUI en la ventana.
        self.canvas.pack()
        self.text_widget.pack(pady=10)
        self.input_button.pack(pady=5)

        self.charge_button.pack(pady=5)
        self.step_button.pack(pady=5)

        self.canvas.create_rectangle(170, 40, 250, 85, outline="white")
        self.canvas.create_rectangle(70, 40, 150, 85, outline="white")
        self.canvas.create_rectangle(70, 105, 250, 165, outline="white")
        self.canvas.create_rectangle(70, 185, 250, 245, outline="white")
        self.canvas.create_rectangle(70, 265, 250, 325, outline="white")

        self.bus_direcciones = self.canvas.create_rectangle(
            450, 105, 600, 165, outline="white")
        self.canvas.create_text(
            525, 135, text="Bus de Direcciones", fill="white", font=("Arial", 12, "bold"))
        self.bus_datos = self.canvas.create_rectangle(
            450, 185, 600, 245, outline="white")
        self.canvas.create_text(
            525, 215, text="Bus de Datos", fill="white", font=("Arial", 12, "bold"))
        self.bus_control = self.canvas.create_rectangle(
            450, 265, 600, 325, outline="white")
        self.canvas.create_text(
            525, 295, text="Bus de Control", fill="white", font=("Arial", 12, "bold"))

        self.canvas.create_text(
            350, 60, text="Banco de registros", fill="white", font=("Arial", 12, "bold"))
        self.canvas.create_rectangle(270, 40, 430, 350, outline="white")

        self.canvas.create_text(
            720, 60, text="Memoria Principal", fill="white", font=("Arial", 12, "bold"))
        self.canvas.create_rectangle(630, 40, 810, 350, outline="white")
        self.memory_text = self.canvas.create_text(660, 80, text="", fill="white", anchor="nw",
                                                   font=("Arial", 12, "bold"))

    # Método para mostrar las señales de control en la GUI.
    def create_control_signals_display(self):
        # Crea textos en el lienzo para mostrar las señales de control y sus estados.
        signals = ['fetch', 'decode', 'execute', 'memory_read', 'memory_write', 'register_read', 'register_write',
                   'alu_operation']
        y_position = 60
        for idx, signal in enumerate(signals):
            text_id = self.canvas.create_text(900, y_position + idx * 30, text=f"{signal}: Off", fill="white",
                                              font=("Arial", 12, "bold"))
            self.control_signals_text[signal] = text_id

    def update_control_signals_display(self, control_signals):
        for signal, value in control_signals.items():
            color = "green" if value else "red"
            text = f"{signal}: {'On' if value else 'Off'}"
            self.canvas.itemconfig(
                self.control_signals_text[signal], text=text, fill=color)

    def highlight_bus(self, bus, color):
        # Resalta el bus especificado cambiando su color.
        self.canvas.itemconfig(bus, outline=color)

    def reset_bus_color(self, bus):
        # Restablece el color del bus especificado.
        self.canvas.itemconfig(bus, outline="white")

    def update_memory_display(self):
        memory_contents = "\n".join(
            f"{i + 1} - {instr}" for i, instr in enumerate(self.instructions))
        self.canvas.itemconfig(self.memory_text, text=memory_contents)

    def reset(self):
        self.memory = Memory(256)
        self.alu = ALU()
        self.control_unit = ControlUnit()
        self.wired_control_unit = WiredControlUnit()

        self.pc_register.set_value(0)
        self.mar_register.set_value(0)
        self.ir_register.set_value("")
        self.mbr_register.set_value(0)
        self.alu_text.set_value("")

        self.instructions = []
        self.register_bank.clear_registers()  # Limpia los registros
        self.update_memory_display()

    def load_instructions(self):
        # Carga las instrucciones ingresadas por el usuario desde el widget de texto.
        # Inicializa la simulación y ejecuta las instrucciones cargadas.
        self.reset()
        instructions = self.text_widget.get("1.0", tk.END).strip().split('\n')
        for idx, instruction in enumerate(instructions):
            if instruction.strip():
                self.memory.store_instruction(idx, instruction.strip())
                self.instructions.append(instruction.strip())
        self.update_memory_display()
        self.execute_all_instructions()

    def load_single_instructions(self):
        # Carga las instrucciones ingresadas por el usuario desde el widget de texto.
        # Inicializa la simulación y ejecuta las instrucciones cargadas.
        instructions = self.text_widget.get("1.0", tk.END).strip().split('\n')
        for idx, instruction in enumerate(instructions):
            if instruction.strip():
                self.memory.store_instruction(idx, instruction.strip())
                self.instructions.append(instruction.strip())
        self.update_memory_display()

    # Métodos para ejecutar el ciclo de búsqueda, decodificación y ejecución de instrucciones.
    def fetch_cycle(self):
        # Realiza la fase de búsqueda de la instrucción desde la memoria.
        pc_value = self.pc_register.value
        self.mar_register.set_value(pc_value)

        mar_value = self.mar_register.value

        instruction = self.control_unit.fetch(
            self.memory, mar_value)

        if not instruction:
            raise ValueError("No instruction found at PC address")

        self.mbr_register.set_value(instruction)
        self.ir_register.set_value(instruction)
        self.pc_register.set_value(pc_value + 1)
        self.mar_register.set_value(self.pc_register.value)

        opcode, reg1, reg2 = self.control_unit.decode()

        operand1 = self.register_bank.get(
            reg1) if reg1 in self.register_bank.registers else None
        operand2 = None
        if reg2.startswith('*'):
            address_register = reg2[1:]
            if address_register in self.register_bank.registers:
                address = self.register_bank.get(address_register)
                operand2 = self.memory.load_data(address)
            else:
                raise ValueError(f"Invalid register for indirect addressing: {
                                 address_register}")
        elif reg2.isdigit():
            operand2 = int(reg2)
        elif reg2 in self.register_bank.registers:
            operand2 = self.register_bank.get(reg2)

        control_signals = self.wired_control_unit.generate_control_signals(
            opcode)
        self.update_control_signals_display(control_signals)

        self.highlight_bus(self.bus_direcciones, "blue")

        self.root.after(500, self.reset_bus_color, self.bus_direcciones)

        self.root.after(500, self.execute_cycle, opcode, reg1,
                        reg2, operand1, operand2, control_signals)

    def execute_cycle(self, opcode, reg1, reg2, operand1, operand2, control_signals):
        # Realiza la fase de ejecución de la instrucción, actualizando registros y memoria según sea necesario.
        self.reset_data_travel()

        if control_signals['alu_operation']:
            self.alu.execute(
                control_signals['alu_operation'], operand1, operand2)
            result = self.alu.value
            self.alu_text.set_value(f"{operand1} {opcode} {
                                    operand2} = {self.alu.value}")
            self.register_bank.set(reg1, result)

        elif opcode == 'LOAD':
            if reg2.startswith('*'):
                address = self.register_bank.get(reg2[1:])
                value = self.memory.load_data(address)
                self.highlight_data_travel()
                self.mbr_register.set_value(value)

            else:
                value = operand2
                self.mbr_register.set_value(value)
                self.highlight_data_travel()

            self.register_bank.set(reg1, value)

        elif opcode == 'STORE':
            self.highlight_data_travel()
            self.memory.store_data(operand2, operand1)

        elif opcode == 'MOVE':
            self.register_bank.set(reg1, self.register_bank.get(reg2))

        self.update_control_signals_display(control_signals)

    def reset_data_travel(self):
        self.root.after(500, self.reset_bus_color, self.bus_control)
        self.root.after(1000, self.reset_bus_color, self.bus_datos)

    def highlight_data_travel(self):
        self.highlight_bus(self.bus_control, "green")
        self.highlight_bus(self.bus_datos, "blue")

    def execute_all_instructions(self):
        # Ejecuta todas las instrucciones cargadas secuencialmente hasta que se complete la simulación.
        if self.pc_register.value < len(self.instructions):
            self.fetch_cycle()
            self.root.after(2000, self.execute_all_instructions)
        else:
            print("Execution completed.")

    def execute_single_instruction(self):
        # Si no hay instrucciones en la cola, termina la ejecución
        if self.pc_register.value < len(self.instructions):
            self.fetch_cycle()
        else:
            print("Execution completed.")

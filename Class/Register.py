# Clase Register (Registro)
# Responsabilidades:
# - Representa un registro en la computadora.
# - Almacena un valor y lo muestra en el lienzo.
class Register:
    def __init__(self, canvas, x, y, name):
        self.value = 0
        self.canvas = canvas
        self.x = x
        self.y = y
        self.name = name
        # Crea un texto en el lienzo para representar el valor del registro.
        self.text_id = canvas.create_text(x + 50, y + 15, text=f"{name}: {self.value}", fill="white",
                                          font=("Arial", 12, "bold"))

    # Método set_value: Establece el valor del registro y actualiza el texto correspondiente en el lienzo.
    def set_value(self, value):
        self.value = value
        self.canvas.itemconfig(self.text_id, text=f"{self.name}: {self.value}")

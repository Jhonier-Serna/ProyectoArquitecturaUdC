El código proporciona una simulación de una computadora básica con una arquitectura simplificada.
Está diseñado para ejecutar un conjunto limitado de instrucciones y mostrar el flujo de control y datos dentro de la computadora.

Principales características:

Clases para componentes de la computadora:
El código define varias clases que representan los componentes principales de una computadora, como la ALU (Unidad Aritmético-Lógica),
la Unidad de Control, la Memoria, el Banco de Registros y la Unidad de Control Cableada.

Interfaz Gráfica de Usuario (GUI):
Utiliza la biblioteca Tkinter para crear una interfaz gráfica simple. La GUI permite al usuario cargar instrucciones en la memoria
y observar el estado de varios componentes de la computadora durante la ejecución de las instrucciones.

Ejecución de Instrucciones:
La simulación sigue un ciclo de búsqueda, decodificación y ejecución de instrucciones. Durante la fase de búsqueda,
se carga la siguiente instrucción desde la memoria. Luego, la instrucción se decodifica para determinar la operación a realizar
y los operandos involucrados. Finalmente, la instrucción se ejecuta, con acciones como operaciones aritméticas,
acceso a la memoria y manipulación de registros.

Visualización del Estado:
La GUI muestra el estado de la memoria, los registros y las señales de control en tiempo real.
Esto permite al usuario observar cómo cambian los datos y el flujo de control dentro de la computadora durante
la ejecución de las instrucciones.

Ejemplos de uso y explicación:

LOAD R1, 10
LOAD R4, 50
STORE R1, 8
LOAD R2, 8
LOAD R3, *R2
ADD R4, R3
MOVE R5, R4


LOAD R1, 10: Carga el valor 10 en el registro R1.
LOAD R4, 50: Carga el valor 50 en el registro R4.
STORE R1, 20: Almacena el valor de R1 (que es 10) en la dirección de memoria 8.
LOAD R2, 8: Carga el valor 8 en el registro R2.
LOAD R3, *R2:
R2 tiene 8.
Se accede a la dirección de memoria 8, donde está almacenado el valor 10 (por la instrucción STORE anterior).
Carga ese valor 10 en R3.
ADD R4, R3: Suma el valor de R3 (que es 10) al valor de R4 (que es 50), resultando en 60, y almacena el resultado en R4.
MOVE R5, R4: Mueve el valor de R4 (que es 60) al registro R5.


////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
LOAD R1, 100
STORE R1, 3
LOAD R2, 3
MOVE R3, R2
STORE R3, 4
LOAD R4, *R3
LOAD R5, *R3

LOAD R1, 100: Carga el valor 100 en el registro R1.
STORE R1, 3: Almacena el valor de R1 (que es 100) en la dirección de memoria 3.
LOAD R2, 3: Carga el valor 3 en el registro R2.
MOVE R3, R2: Copia el valor de R2 (que es 3) a R3.
LOAD R4, *R3: Carga el valor de la memoria en la dirección contenida en R3 (que es 100).
LOAD R5, *R3: Igual que el anterior.
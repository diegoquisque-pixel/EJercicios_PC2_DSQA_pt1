import pyfiglet
from colorama import init, Fore, Back, Style
init()
# Alonzo = Amarillo
titulo = pyfiglet.figlet_format("ALONZO")
print(titulo)
print(Fore.YELLOW + titulo + Style.RESET_ALL)
print(Fore.RED + "Texto en color ")
print("😹😹")

# Diego quisque
class Calculadora():
    def __init__(self, num1, num2):
        self._num1 = num1  # Almacena el primer número
        self._num2 = num2  # Almacena el segundo número

    def suma(self):
        resultado = self._num1 + self._num2  # Suma los dos números
        print(f"El resultado de la suma es: {self._num1} + {self._num2} = {resultado}")

    def resta(self):
        resultado = self._num1 - self._num2  # Resta los dos números
        print(f"El resultado de la resta es: {self._num1} - {self._num2} = {resultado}")

    def division(self):
        # Nota: En la imagen usa // que es división entera (sin decimales)
        resultado = self._num1 // self._num2  # División entera
        print(f"El resultado de la división es: {self._num1} // {self._num2} = {resultado}")

    def multiplicacion(self):
        resultado = self._num1 * self._num2  # Multiplica los dos números
        print(f"El resultado de la multiplicación es: {self._num1} * {self._num2} = {resultado}")


# Crear objetos y realizar operaciones

# Prueba de Suma
operacion = Calculadora(num1=10, num2=5)
operacion.suma()

# Prueba de Resta
operacion = Calculadora(num1=20, num2=5)
operacion.resta()

# Prueba de División
operacion = Calculadora(num1=15, num2=3)
operacion.division()

# Prueba de Multiplicación
operacion = Calculadora(num1=8, num2=4)
operacion.multiplicacion()
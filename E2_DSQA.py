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
# Definición de la clase Persona
class Persona:
    def __init__(self, n, e):
        self.nombre = n  # Asigna el nombre recibido
        self.edad = e    # Asigna la edad recibida

    def cumpleaños(self):
        self.edad += 1   # Incrementa la edad en 1

# Creación del objeto p solicitando datos al usuario
p = Persona(input("Ingrese nombre: "), int(input("Ingrese edad: ")))

# Llama dos veces al método cumpleaños para sumar 2 años
p.cumpleaños()
p.cumpleaños()

# Muestra el resultado con un mensaje bien formado
print(f"{p.nombre} cumple {p.edad} años")
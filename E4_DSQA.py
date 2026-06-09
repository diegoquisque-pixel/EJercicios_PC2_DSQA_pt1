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
# Clase base Fabrica
class Fabrica():
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio

class Moto(Fabrica):
    def cantidad(self):
        print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(
            self._llantas, self._color, self._precio))

class Carro(Fabrica):
    def cantidad(self):
        print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(
            self._llantas, self._color, self._precio))

# Crear objeto tipo Moto
print("OBJETO = moto")
moto = Moto(llantas=2, color="Gris", precio="0.200")
moto.cantidad()

# Crear objeto tipo Carro
print("\nOBJETO = carro")
carro = Carro(llantas=4, color="Negro", precio="0.600")
carro.cantidad()
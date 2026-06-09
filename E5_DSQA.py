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
# Clase base Marino
class Marino():
    def hablar(self):
        print("Hola soy un animal marino!")

class Pulpo(Marino):
    # Sobrescribe el método hablar de la clase padre
    def hablar(self):
        print("Hola soy un pulpo.")

class Foca(Marino):
    # Sobrescribe el método hablar y agrega un parámetro extra
    def hablar(self, mensaje):
        self.mensaje = mensaje
        print(mensaje)

# Creación de objetos y llamadas a métodos
marino = Marino()
marino.hablar()

pulpo = Pulpo()
pulpo.hablar()

foca = Foca()
# se pasa el argumento personalizado requerido por la clase Foca
foca.hablar("Hola soy una foca!")
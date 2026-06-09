import pyfiglet
from colorama import init, Fore, Back, Style
init()
# Alonzo = AmarilloS
titulo = pyfiglet.figlet_format("ALONZO")
print(titulo)
print(Fore.YELLOW + titulo + Style.RESET_ALL)
print(Fore.RED + "Texto en color ")
print("😹😹")

# Diego quisque


class  Estudiante ():
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir (self):
            print(f"Nombre: {self.nombre} \nNota: {self.nota}")

    def  resultados (self):
            if self.nota >= 70:
                print("Has Reprobado!!! 😕💔")
            else:
                print("Has  aprovado!!! 🥳🎉")

# crear primer objeto Estudiante
estudiante1 = Estudiante(nombre="Pedro", nota = 60 )
estudiante1.imprimir()
estudiante1.resultados()
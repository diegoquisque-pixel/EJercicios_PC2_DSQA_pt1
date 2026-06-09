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
# crear una clase alumno  y promedio en python

# se define la clase llamada alumno
class Alumno:
    def __init__(self, nombre, promedio):
        self.__nombre = nombre
        self.__promedio = promedio

    # Cambia 'get_nombre' por 'obtener_nombre'
    def obtener_nombre(self):
        return self.__nombre

    # Cambia 'get_promedio' por 'obtener_promedio'
    def obtener_promedio(self):
        return self.__promedio

    # Cambia 'set_promedio' por 'cambiar_promedio'
    def cambiar_promedio(self, nuevo):
        self.__promedio = nuevo

# ... (aquí iría la definición de la clase Alumno) ...

# Se solicita al usuario que ingrese el nombre del alumno (Esta es la parte que faltaba)
nombre_ingresado = input("Ingrese el nombre del alumno: ")

# Se solicita al usuario que ingrese el promedio del alumno, convirtiéndolo a float
promedio_ingresado = float(input("Ingrese el promedio del alumno: "))

# Se crea un objeto de la clase Alumno con los datos ingresados por el usuario
alumno1 = Alumno(nombre_ingresado, promedio_ingresado)

# Se muestra el nombre del alumno usando el método obtenernombre()
print("Nombre del alumno:", alumno1.obtener_nombre())

# Se muestra el promedio del alumno usando el método obtener_promedio()
print("Promedio del alumno:", alumno1.obtener_promedio())

# Se solicita un nuevo promedio al usuario para modificar el dato existente
nuevo_promedio = float(input("Ingrese un nuevo promedio para el alumno: "))

# Se llama al método cambiar_promedio para actualizar el promedio del alumno
alumno1.cambiar_promedio(nuevo_promedio)

# Se muestra el nuevo promedio actualizado
print("Nuevo promedio actualizado:", alumno1.obtener_promedio())

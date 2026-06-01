# ======ENCAPSULAMIENTO====== #
class Producto:
    def __init__(self, nombre, precio):
        self.__nombre = nombre
        self.__precio = precio
# ===GETS=== #
    def get_nombre(self):
        return self.__nombre
    def get_precio(self):
        return self.__precio

# ======HERENCIA====== #
class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre
# ===GETS=== #
    def get_nombre(self):
        return self.__nombre
# ===CLASE HIJA=== #
class Estudiante(Persona):
    def __init__(self, nombre, curso):
        super().__init__(nombre)
        self.__curso = curso

# ======ABSTRACCIÓN====== #
from abc import ABC, abstractmethod

class Figura(ABC):

    @abstractmethod
    def calcular_area(self):
        pass

# ======POLIMORFISMO====== #
class Perro:
    def hacer_sonido(self):
        print("Guau")

class Gato:
    def hacer_sonido(self):
        print("Miau")
animales = [Perro(), Gato()]

for animal in animales:
    animal.hacer_sonido()
        
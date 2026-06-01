# ===EJERCICIO#7=== #
#CLASE ABSTRACTA
from abc import ABC, abstractmethod

class Figura(ABC):
    
    @abstractmethod
    def calcular_area(self):
        pass
#CLASE CUADRADO
class Cuadrado(Figura):
    def __init__(self, lado):
        self.__lado = lado
# ==GETS== #
    def get_lado(self):
        return self.__lado
    def calcular_area(self):
        return self.__lado * self.__lado

# ===EJERCICIO#8=== #
from abc import ABC, abstractmethod

class Pago(ABC):
    def procesar_pago(self):
        pass
#CLASE PagoTarjeta
class PagoTarjeta(Pago):
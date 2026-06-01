# ===EJERCICIO#1=== #
class Empleado:
    def __init__(self, nombre, rut, sueldo):
        self.__nombre = nombre
        self.__rut = rut
        self.__sueldo = sueldo
#== GETS ==#
    def get_nombre(self):
        return self.__nombre
    def get_rut(self):
        return self.__rut
    def get_sueldo(self):
        return self.__sueldo

# ===EJERCICIO#2=== #   
class Mascota:
    def __init__(self, nombre, especie, edad):
        self.__nombre = nombre
        self.__especie = especie
        self.__edad = edad
#== GETS ==#
    def get_nombre(self):
        return self.__nombre
    def get_especie(self):
        return self.__especie
    def get_edad(self):
        return self.__edad
    
# ===EJERCICIO#3=== #
class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock
# ==GETS== #
    def get_codigo(self):
        return self.__codigo
    def get_nombre(self):
        return self.__codigo
    def get_precio(self):
        return self.__precio
    def get_stock(self):
        return self.__stock
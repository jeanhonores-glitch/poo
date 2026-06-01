# ===EJERCICIO#4=== #
class Persona:
    def __init__(self, nombre, rut, edad):
        self.__nombre
        self.__rut
        self.__edad
# ==GETS== #
    def get_nombre(self):
        return self.__nombre
    def get_rut(self):
        return self.__rut
    def get_edad(self):
        return self.__edad
#==CLASE HIJA==#
class Estudiante(Persona):
    def __init__(self, nombre, rut, edad, curso, promedio):
        super().__init__(nombre, rut, edad)
        self.__curso
        self.__promedio
# ==GETS== #
    def get_curso(self):
        return self.__curso
    def get_promedio(self):
        return super().get_promedio()
    
# ===EJERCICIO#5=== #
class Vehiculo:
    def __init__(self, patente, marca, año):
        self.__patente
        self.__marca
        self.__año
# ==GETS== #
    def get_patente(self):
        return self.__patente
    def get_marca(self):
        return self.__marca
    def get_año(self):
        return self.__año
# ==CLASE HIJA== #
class Bus(Vehiculo):
    def __init__(self, patente, marca, año, capacidad):
        super().__init__(patente, marca, año)
        self.__capacidad
# ==GETS== #
    def get_capacidad(self):
        return self.__capacidad

# ===EJERCICIO#6=== #
class Trabajador:
    def __init__(self, nombre,sueldo):
        self.__nombre
        self.__sueldo
# ==GETS== #
    def get_nombre(self):
        return self.__nombre
    def get_sueldo(self):
        return self.__sueldo
# ===CLASE HIJA=== #
class Medico(Trabajador):
    def __init__(self, nombre, sueldo, especialidad):
        super().__init__(nombre, sueldo)
        self.__especialidad
# ==GETS== #
    def get_capacidad(self):
        return self.__capacidad
class Paciente:
    def __init__(self):
    
        self.__nombre = ""
        self.__id = int
        self.__edad = int
        self.__imagen = ""
        
    def verNombre(self):
        return self.__nombre
    def verImagen(self):
        return self.__servicio
    def verEdad(self):
        return self.__genero
    def verId(self):
        return self.__cedula
    
    def asignarNombre(self,n):
        self.__nombre = n
    def asignarImagen(self,s):
        self.__servicio = s
    def asignarEdad(self,g):
        self.__genero = g
    def asignarId(self,c):
        self.__cedula = c
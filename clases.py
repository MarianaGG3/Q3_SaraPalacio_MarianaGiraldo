class Paciente:
    def __init__(self):
    
        self.__nombre = ""
        self.__id = int
        self.__edad = int
        self.__imagen = ""
        
    def verNombre(self):
        return self.__nombre
    def verImagen(self):
        return self.__imagen
    def verEdad(self):
        return self.__edad
    def verId(self):
        return self.__id
    
    def asignarNombre(self,n):
        self.__nombre = n
    def asignarImagen(self,s):
        self.__imagen = s
    def asignarEdad(self,g):
        self.__edad = g
    def asignarId(self,c):
        self.__id = c
class usuario:
    def __init__(self,idusuario,nombre,password,direccion):
        self.__idusuario=idusuario
        self.__nombre=nombre
        self.__password=password
        self.__direccion=direccion
    def getIdusuario(self):
        return self.__idusuario
    def getNombre(self):
        return self.__nombre
    def getpassword(self):
        return self.__password
    def getdireccion(self):
        return self.__direccion
    def setdireccion(self):
        self.__direccion
    def setIdusuario(self):
        self.__idusuario
    def setNombre(self,nombre):
        self.__nombre=nombre
    def setDocumento(self,password):
        self.__password=password
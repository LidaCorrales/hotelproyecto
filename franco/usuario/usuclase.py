class usuario:
    def __init__(self,idusuario,nombre,documento):
        self.__idusuario=idusuario
        self.__nombre=nombre
        self.__documento=documento
    def getIdusuario(self):
        return self.__idusuario
    def getNombre(self):
        return self.__nombre
    def getDocumento(self):
        return self.__documento
    
    def setIdusuario(self):
        self.__idusuario
    def setNombre(self,nombre):
        self.__nombre=nombre
    def setDocumento(self,documento):
        self.__documento=documento
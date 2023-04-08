class habitacion:
    def __init__(self,id_habitacion,descripción,tipo,estado):
        self.__id_habitacion=id_habitacion
        self.__descripcion=descripción
        self.__tipo=tipo
        self.__estado=estado

    def getid_habitacion(self):
        return self.__id_habitacion
    def getdescripcion(self):
        return self.__descripcion
    def gettipo(self):
        return self.__tipo
    def getestado(self):
        return self.__estado
    
    def setid_habitacion(self,id_habitacion):
        self.__id_habitacion=id_habitacion
    def setdescripcion(self,descripcion):
        self.__descripcion=descripcion
    def settipo(self,tipo):
        self.__tipo=tipo
    def setestado(self,estado):
        self.__estado=estado
    
    
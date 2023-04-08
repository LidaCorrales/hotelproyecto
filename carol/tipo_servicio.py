class tipo_servicio:
    def __init__(self,id_tipo_servicio_servi,tipo_servi,precio_servi):
        self.__id_tipo_servicio_servi = id_tipo_servicio_servi
        self.__tipo_servi = tipo_servi
        self.__precio_servi = precio_servi
        

    def getIdtipservi(self):
        return self.__id_tipo_servicio_servi

    def setIdtipservi(self,id_tipo_servicio_servi):
        self.__id_tipo_servicio_servi = id_tipo_servicio_servi

    def getTiposer(self):
        return self.__tipo_servi

    def setTiposer(self,tipo_servi):
        self.__tipo_servi = tipo_servi

    def getPrecioser(self):
        return self.__precio_servi

    def setPrecioser(self,precio_servi):
        self.__precio_servi = precio_servi
    
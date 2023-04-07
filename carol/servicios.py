class Servicios:
    def __init__(self,id_servicio_ser,can_ser,id_tp_ser,id_factura):
        self.__id_servicio_ser = id_servicio_ser
        self.__can_ser = can_ser
        self.__id_tp_ser = id_tp_ser
        self.__id_factura = id_factura

    def getIdservi(self):
        return self.__id_servicio_ser

    def setIdservi(self,id_servicio_ser):
        self.__id_servicio_ser = id_servicio_ser

    def getcanser(self):
        return self.__can_ser

    def setcanser(self,can_ser):
        self.__can_ser = can_ser

    def getIdtipo(self):
        return self.__id_tp_ser

    def setIdtipo(self,id_tp_ser):
        self.__id_tp_ser = id_tp_ser
    
    def getIdfactura(self):
        return self.__id_factura

    def setIdfactura(self,id_factura):
        self.__id_factura = id_factura

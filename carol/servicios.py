class Servicios:
    def __init__(self,id_servicio,cantidad,id_tp_ser,id_factura):
        self.__id_servicio = id_servicio
        self.__cantidad = cantidad
        self.__id_tp_ser = id_tp_ser
        self.__id_factura = id_factura

    def getIdservi(self):
        return self.__id_servicio

    def setIdservi(self,id_servicio):
        self.id_servicio = id_servicio

    def getCantidad(self):
        return self.__cantidad

    def setCantidad(self,cantidad):
        self.__cantidad = cantidad

    def getIdtipo(self):
        return self.__id_tp_ser

    def setIdtipo(self,id_tp_ser):
        self.__id_tp_ser = id_tp_ser
    
    def getIdfactura(self):
        return self.__id_factura

    def setIdfactura(self,id_factura):
        self.__id_factura = id_factura

ob=Servicios("123","2","restaurante","233")
print(ob.getIdservi)

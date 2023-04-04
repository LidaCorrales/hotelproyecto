class Reserva:
    def __init__(self,idreserva,documento,numpersonas,tipo_hab,fechaentrada,fechasalida):
        self.__idreserva=idreserva
        self.__documento=documento
        self.__numpersonas=numpersonas
        self.__tipo_hab=tipo_hab
        self.__fechaentrada=fechaentrada
        self.__fechasalida=fechasalida
    def getIdreserva(self):
        return self.__idreserva
    def getDocumento(self):
        return self.__documento
    def getNumpersona(self):
        return self.__numpersonas
    def getHab(self):
        return self.__tipo_hab
    def getFechauno(self):
        return self.__fechaentrada
    def getFechados(self):
        return self.__fechasalida
    
    def setIdreserva(self,idreserva):
        self.__idreserva=idreserva
    def setDocumento(self,documento):
        self.__documento=documento
    def setNumpersonas(self,numpersonas):
        self.__numpersonas=numpersonas
    def setHab(self,tipo_hab):
        self.__tipo_hab=tipo_hab
    def setFechauno(self,fechaentrada):
        self.__fechaentrada=fechaentrada
    def setFechados(self,fechasalida):
        self.__fechasalida=fechasalida

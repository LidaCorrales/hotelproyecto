class Reserva:
    def __init__(self,can_hab,documento,numpersonas,tipo_hab,fechaentrada,fechasalida):
        self.__can_hab=can_hab
        self.__documento=documento
        self.__numpersonas=numpersonas
        self.__tipo_hab=tipo_hab
        self.__fechaentrada=fechaentrada
        self.__fechasalida=fechasalida
    def getCan_hab(self):
        return self.__can_hab
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
    
    def setCan_hab(self,can_hab):
        self.__can_hab=can_hab
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

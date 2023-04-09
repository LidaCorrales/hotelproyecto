class Reserva:
    def __init__(self,can_hab,numpersonas,fechaentrada,fechasalida):
        self.__can_hab=can_hab
        self.__numpersonas=numpersonas
        self.__fechaentrada=fechaentrada
        self.__fechasalida=fechasalida
    def getCan_hab(self):
        return self.__can_hab
    def getNumpersona(self):
        return self.__numpersonas
    def getFechauno(self):
        return self.__fechaentrada
    def getFechados(self):
        return self.__fechasalida
    
    def setCan_hab(self,can_hab):
        self.__can_hab=can_hab
    def setNumpersonas(self,numpersonas):
        self.__numpersonas=numpersonas
    def setFechauno(self,fechaentrada):
        self.__fechaentrada=fechaentrada
    def setFechados(self,fechasalida):
        self.__fechasalida=fechasalida

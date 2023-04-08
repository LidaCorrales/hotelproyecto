class tipo_habitacion:
    def __init__(self,id_tipo_hab,tipo_hab,precio_hab):
        self.__id_tipo_hab=id_tipo_hab
        self.__tipo_hab=tipo_hab
        self.__precio_hab=precio_hab

    def get_id_tipo_hab(self):
        return self.__id_tipo_hab
    
    def get_tipo_hab(self):
        return self.__tipo_hab
    
    def get_precio_hab(self):
        return self.__precio_hab
    

    def set_id_tipo_hab(self,id_tipo_hab):
        self.__id_tipo_hab=id_tipo_hab

    def set_tipo_hab(self,tipo_hab):
        self.__tipo_hab=tipo_hab

    def set_precio_hab(self,precio_hab):
        self.__precio_hab=precio_hab
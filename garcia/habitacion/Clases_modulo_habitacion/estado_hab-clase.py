class estado_habitacion:
    def __init__(self,id_estado_hab,estado_es):
        self.__id_estado_hab=id_estado_hab
        self.__estado_es=estado_es

    def get_id_estado_hab(self):
        return self.__id_estado_hab
    
    def get_estado(self):
        return self.__estado_es
    

    def set_id_estado_hab(self,id_estado_hab):
        self.__id_estado_hab=id_estado_hab
        
    def settipo(self,estado_es):
        self.__estado_es=estado_es
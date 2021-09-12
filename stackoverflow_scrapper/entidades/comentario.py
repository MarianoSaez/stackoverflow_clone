class Comentario:
    def __init__(self, descripcion, fecha, usuario=None):
        self.descripcion = descripcion
        self.fecha = fecha
        self.usuario = usuario
        self.usuario_id = None

    @property
    def descripcion(self):
        return self.__descripcion

    @descripcion.setter
    def descripcion(self, value):
        if value != None:
            self.__descripcion = value.text
        else:
            self.__descripcion = "NA"

    @property
    def fecha(self):
        return self.__fecha

    @fecha.setter
    def fecha(self, value):
        if value != None:
            self.__fecha = value.get("title")
        else:
            self.__fecha = "NA"

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self, value):
        if value != None:
            self.__usuario = value.text
        else:
            self.__usuario = "NA"
 
    def __repr__(self):
        return str(self.__dict__)

    def jsonize(self):
        return json.dumps(self.__dict__)
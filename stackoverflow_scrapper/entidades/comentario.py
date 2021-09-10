class Comentario:
    _id = 0
    def __init__(self, descripcion, fecha, usuario=None):
        self._id = type(self)._id
        type(self)._id += 1
        self.descripcion = descripcion
        self.fecha = fecha
        self.usuario = usuario

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
        rep = ""
        for i in self.__dict__:
            rep += f"\n{i.upper()}\n{self.__dict__[i]}\n"
        return rep

    def jsonize(self):
        return json.dumps(self.__dict__)
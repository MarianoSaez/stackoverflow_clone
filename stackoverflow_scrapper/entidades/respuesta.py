class Respuesta:
    _id = 0
    def __init__(self, fecha, descripcion, votes=0,
                 comentarios=None, usuario=None):
        self._id = type(self)._id
        type(self)._id += 1
        self.fecha = fecha
        self.descripcion = descripcion
        self.votes = votes
        # self.tags = tags [NO TIENEN ESTE ATRIBUTO - COMPARTEN LAS DE PREG]

        self.comentarios = comentarios
        self.usuario = usuario

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
    def descripcion(self):
        return self.__descripcion

    @descripcion.setter
    def descripcion(self, value):
        if value != None:
            self.__descripcion = value.text
        else:
            self.__descripcion = "NA"

    @property
    def votes(self):
        return self.__votes

    @votes.setter
    def votes(self, value):
        if value != None:
            self.__votes = int(value.text)
        else:
            self.__votes = 0

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self, value):
        if value != None:
            self.__usuario = value.text
        else:
            self.__usuario = "ANON"

    def __repr__(self):
        rep = ""
        for i in self.__dict__:
            rep += f"\n{i.upper()}\n{self.__dict__[i]}\n"
        return rep

    def jsonize(self):
        return json.dumps(self.__dict__)

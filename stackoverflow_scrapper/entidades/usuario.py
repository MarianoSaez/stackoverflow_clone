class Usuario:
    _id = 0
    def __init__(self, nickname):
        self._id = type(self)._id
        type(self)._id += 1
        self.nickname = nickname
        # self.nombre = nombre
        # self.password = password
        # self.img_usuario = img_usuario
        # self.ubicacion = ubicacion
        # self.especialidades = especialidades
        # self.descripcion = descripcion
        # self.links_trabajo = links_trabajo

        self.respuestas = list()
        self.preguntas = list()
        self.comentarios = list()
        # self.preguntas_seguidas = preguntas_seguidas

    @property
    def nickname(self):
        return self.__nickname

    @nickname.setter
    def nickname(self, value):
        if value != None:
            self.__nickname = value
        else:
            self.__nickname = "NA"

    def __repr__(self):
        return str(self.__dict__)


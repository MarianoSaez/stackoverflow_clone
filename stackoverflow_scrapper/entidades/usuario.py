class Usuario:
    _id = 0
    def __init__(self, nickname, nombre, password, img_usuario, ):
        self._id = type(self)._id
        type(self)._id += 1
        self.nickname = nickname
        self.nombre = nombre
        # self.password = password
        # self.img_usuario = img_usuario
        # self.ubicacion = ubicacion
        # self.especialidades = especialidades
        # self.descripcion = descripcion
        # self.links_trabajo = links_trabajo

        # self.respuestas = respuestas
        # self.pregunta = pregunta
        # self.preguntas_seguidas = preguntas_seguidas

    @property
    def nickname(self):
        return self.__nickname

    @nickname.setter
    def nickname(self, value):
        if value != None:
            self.__nickname = value.get("title")
        else:
            self.__nickname = "NA"
    
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        if value != None:
            self.__nombre = value.text
        else:
            self.__nombre = self.nickname


    def __repr__(self):
        rep = ""
        for i in self.__dict__:
            rep += f"\n{i.upper()}\n{self.__dict__[i]}\n"
        return rep

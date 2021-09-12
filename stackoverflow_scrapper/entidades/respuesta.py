from .usuario import Usuario


class Respuesta:
    _id = 0
    def __init__(self, fecha, descripcion, votes=0,
                 comentarios=None, usuario=None):
        self._id = type(self)._id
        type(self)._id += 1
        self.fecha = fecha
        self.descripcion = descripcion
        self.votes = votes
        self.comentarios = comentarios
        self.usuario = usuario
        self.usuario_id = None

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
        return str(self.__dict__)

    def useUserDB(self, DB, name, titulo, pregunta_id):
        if name not in DB:
            DB[name] = Usuario(name)
        DB[name].respuestas.append({
            "titulo" : titulo,
            "pregunta_id" : pregunta_id,
            "respuesta_id" : self._id,
        })
        return DB[name]._id


    def jsonize(self):
        return json.dumps(self.__dict__)

from .usuario import Usuario


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

    def useUserDB(self, DB, name, titulo, pregunta_id):
        if name not in DB:
            DB[name] = Usuario(name)
        DB[name].comentarios.append({
            "titulo" : titulo,
            "pregunta_id" : pregunta_id,
        })
        return DB[name]._id

    def jsonize(self):
        return json.dumps(self.__dict__)
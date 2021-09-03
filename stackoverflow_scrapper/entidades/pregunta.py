import json


class Pregunta:
    def __init__(self, titulo, fecha, descripcion, votes=0,
                 tags=None, comentarios=None, respuestas=None,
                 respuesta_aceptada=None, usuario=None, respondida=None):
        self.titulo = titulo
        self.fecha = fecha
        self.descripcion = descripcion
        self.votes = votes
        self.tags = tags
        self.comentarios = comentarios
        self.respuestas = respuestas
        self.respuesta_aceptada = respuesta_aceptada
        self.usuario = usuario
        self.respondida = respondida

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, value):
        if value != None:
            self.__titulo = value.text
        else:
            self.__titulo = "NA"

    @property
    def fecha(self):
        return self.__fecha

    @fecha.setter
    def fecha(self, value):
        if value != None:
            self.__fecha = value.text
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

    def jsonize(self):
        return json.dumps(self.__dict__)


if __name__ == "__main__":
    p = Pregunta(0,0,0,0,0,0,0,0,0,0,0)
    print(p.jsonize())

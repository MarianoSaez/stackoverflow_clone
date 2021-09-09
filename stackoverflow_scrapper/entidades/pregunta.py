import json
from .respuesta import Respuesta
from bs4 import BeautifulSoup


class Pregunta:
    _id = 0
    def __init__(self, titulo, fecha, descripcion, votes=0,
                 tags=None, respondida=None, respuestas=None,
                 respuesta_aceptada=None, comentarios=None, usuario=None):
        self._id = type(self)._id
        type(self)._id += 1
        self.titulo = titulo
        self.fecha = fecha
        self.descripcion = descripcion
        self.votes = votes
        self.tags = tags
        self.respondida = respondida
        
        self.respuestas = respuestas
        # self.respuesta_aceptada = respuesta_aceptada [Agregado cuando respondida == True]
        self.comentarios = comentarios
        self.usuario = usuario

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
    def tags(self):
        return self.__tags

    @tags.setter
    def tags(self, value):
        if value != None:
            self.__tags = list(set([i.text for i in value])) # Cochino de momento :v
        else:
            self.__tags = list()

    @property
    def respondida(self):
        return self.__respondida

    @respondida.setter
    def respondida(self, value):
        if value != None:

            fecha = value.find("span", attrs={"class" : "relativetime"})
            descripcion = value.find("div", attrs={"class" : "s-prose js-post-body"})
            votes = value.find("div", attrs={"class" : "js-vote-count flex--item d-flex fd-column ai-center fc-black-500 fs-title"})
            
            self.__respuesta_aceptada = Respuesta(fecha, descripcion, votes)
            self.__respondida = True

        else:
            self.__respondida = False
            self.__respuesta_aceptada = "NA"

    @property
    def respuestas(self):
        return self.__respuestas

    @respuestas.setter
    def respuestas(self, value):
        if value != None:
            self.__respuestas = [i.id for i in value]
        else:
            self.__respuestas = 0




    def jsonize(self):
        return json.dumps(self.__dict__)


if __name__ == "__main__":
    p = Pregunta(0,0,0,0,0,0,0,0,0,0,0)
    print(p.jsonize())

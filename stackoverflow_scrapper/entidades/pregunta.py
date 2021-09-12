import json
from .respuesta import Respuesta
from .usuario import Usuario
from bs4 import BeautifulSoup
from utils import collectComments


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
        self.comentarios = comentarios
        self.usuario = usuario
        self.usuario_id = None

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

            try:
                usuario = value.find("div", attrs={"class" : "post-layout"}).find("div", attrs={"class" : "user-details", "itemprop" : "author"}).find("a", href=True)
            except AttributeError:
                usuario = None

            fecha = value.find("span", attrs={"class" : "relativetime"})
            descripcion = value.find("div", attrs={"class" : "s-prose js-post-body"})
            votes = value.find("div", attrs={"class" : "js-vote-count flex--item d-flex fd-column ai-center fc-black-500 fs-title"})
            
            lista_value = value.findAll("div", attrs={"class" : "comment-body js-comment-edit-hide"})
            comentarios = list()

            collectComments(lista_value, comentarios)

            


            self.__respuesta_aceptada = Respuesta(fecha, descripcion, votes, comentarios, usuario)
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
            self.__respuestas = value
        else:
            self.__respuestas = list()

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

    def jsonize(self):
        return json.dumps(self.__dict__)

    def useUserDB(self, DB, name):
        if name not in DB:
            DB[name] = Usuario(name)
        DB[name].preguntas.append({
            "titulo" : self.titulo,
            "_id" : self._id,
        })

if __name__ == "__main__":
    p = Pregunta(0,0,0,0,0,0,0,0,0,0,0)
    print(p.jsonize())

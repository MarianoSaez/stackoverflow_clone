from bs4 import BeautifulSoup
from entidades.comentario import Comentario
import re
import json


"""
Recibe una lista de PageElements sobre la cual iterar buscando atributos con
los cuales se construye la instancia de Comentario la cual es agregada a la
lista recibida por parametro attributeList [Trabaja con pasaje por referencia]
"""
def collectComments(pageElementList : list, attributeList : list, DB : dict, titulo : str, pregunta_id : int):
    for pageElement in pageElementList:
        descripcion_com = pageElement.find("span", attrs={"class" : "comment-copy"})
        usuario_com = pageElement.find("a", href=True, attrs={"class" : "comment-user"})
        fecha_com = pageElement.find("span", attrs={"class" : "relativetime-clean"})

        # TODO : Deberia ser necesario guardar el id del usuario dentro del comentario
        comentario = Comentario(descripcion_com, fecha_com, usuario_com)

        usuario_comentario_id = comentario.useUserDB(DB, comentario.usuario, titulo, pregunta_id)

        comentario.usuario_id = usuario_comentario_id

        attributeList.append(comentario)


"""
Esta clase se encarga de codificar instancias de Clases Custom
a objetos serializables a JSON
"""
class MyEncoder(json.JSONEncoder):
    def default(self, o):
        if type(o) != list:
            return o.__dict__
        else:
            return o


def rectifyTags(JSON : str):
    rgxList = [
        r"\"_.*__titulo\"",
        r"\"_.*__fecha\"",
        r"\"_.*__descripcion\"",
        r"\"_.*__votes\"",
        r"\"_.*__tags\"",
        r"\"_.*__respuesta_aceptada\"",
        r"\"_.*__respondida\"",
        r"\"_.*__usuario\"",
        r"\"_.*__respuestas\"",
        r"\"_.*__comentarios\"",
        r'(\"\d{4}(-\d{2}){2}\s.*Z\")',
        r'(\"\d{4}(-\d{2}){2}\s.*Z)\,.*\"'
    ]

    replaceList = [
        '"titulo"',
        '"fecha"',
        '"decripcion"',
        '"votes"',
        '"tags"',
        '"respuesta_aceptada"',
        '"respondida"',
        '"usuario"',
        '"respuestas"',
        '"comentarios"',
        r'{ "$date" : \1 }',
        r'{ "$date" : \1" }'
    ]

    for i in range(len(rgxList)):
        JSON = re.sub(rgxList[i], replaceList[i], JSON)

    return JSON





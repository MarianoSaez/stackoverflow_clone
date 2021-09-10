from bs4 import BeautifulSoup
from entidades.comentario import Comentario


# Recibe una lista de PageElements sobre la cual iterar buscando atributos con
# los cuales se construye la instancia de Comentario la cual es agregada a la
# lista recibida por parametro attributeList [Trabaja con pasaje por referencia]
def collectComments(pageElementList : list, attributeList : list):
    for pageElement in pageElementList:
        descripcion_com = pageElement.find("span", attrs={"class" : "comment-copy"})
        usuario_com = pageElement.find("a", href=True, attrs={"class" : "comment-user"})
        fecha_com = pageElement.find("span", attrs={"class" : "relativetime-clean"})

        # TODO : Deberia ser necesario guardar el id del usuario dentro del comentario
        comentario = Comentario(descripcion_com, fecha_com, usuario_com)

        attributeList.append(comentario)
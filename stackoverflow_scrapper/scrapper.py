from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
from entidades.pregunta import Pregunta
from entidades.respuesta import Respuesta
from entidades.comentario import Comentario
from utils import collectComments
import json
from encoder import MyEncoder

# TODO 
#   Crear usuarios - Ya sea de forma aleatoria usando los nombres en los post's
#   o ingresando a cada perfil de usuario real (COSTOSO EN TIEMPO)
#
#   Volcar objetos en un formato serializado JSON para su posterior importacion
#   a MongoDB - DONE



driver = webdriver.Firefox()

tags = [
    "python",
    # "javascript",
    # "js",
    # "python-3.x",
    # "java",
    # "sockets",
    # "threads",
    # "processes",
]

questions = list()
answers = list()

for i in tags:
    links = list()
    driver.get(f"https://stackoverflow.com/questions/tagged/{i}?tab=Frequent")

    content = driver.page_source
    soup = BeautifulSoup(content)

    for url in soup.findAll("a", href=True, attrs={"class" : "question-hyperlink"}):
        try:
            driver.get(f"https://stackoverflow.com{url.get('href')}")
        except Exception:
            print(f" Se finaliza el tag : {i.upper()} ".center(90, "="))
            break

        pregunta = driver.page_source
        src = BeautifulSoup(pregunta)
    
        titulo = src.find("a", href=True, attrs={"class" : "question-hyperlink"})
        fecha = src.find("span", attrs={"class" : "relativetime"})
        desc = src.find("div", attrs={"class" : "s-prose js-post-body"})
        votes = src.find("div", attrs={"class" : "js-vote-count flex--item d-flex fd-column ai-center fc-black-500 fs-title"})
        tags = src.findAll("a", href=True, attrs={"class" : "post-tag"})
        respuesta_aceptada = src.find("div", attrs={"class" : "answer accepted-answer"})

        # Se construye el objeto pregunta con atributos disponibles
        pregunta = Pregunta(titulo, fecha, desc, votes, tags,
                            respuesta_aceptada)

        # REPUESTAS
        respuestas = list()
        # Se completa la lista que se agregara a la pregunta
        for ans in src.findAll("div", attrs={"class" : "answer"}):
            fecha_rta = ans.find("span", attrs={"class" : "relativetime"})
            descripcion_rta = ans.find("div", attrs={"class" : "s-prose js-post-body"})
            votes_rta = ans.find("div", attrs={"class" : "js-vote-count flex--item d-flex fd-column ai-center fc-black-500 fs-title"})

            # Se construye el objeto respuesta con atributos disponibles
            respuesta = Respuesta(fecha_rta, descripcion_rta, votes_rta)

            comentarios_rta = list()
            lista_ans = ans.findAll("div", attrs={"class" : "comment-body js-comment-edit-hide"})

            collectComments(lista_ans, comentarios_rta)

            # Los comentarios se agregaran en forma embebida por lo que se agrega la instancia
            respuesta.comentarios = comentarios_rta

            respuestas.append(respuesta)
            answers.append(respuesta)
        
        # COMENTARIOS
        comentarios = list()
        lista_src = src.find("div", attrs={"class" : "post-layout"}).findAll("div", attrs={"class" : "comment-body js-comment-edit-hide"})

        collectComments(lista_src, comentarios)


        # USUARIO
        # TODO : Buscar o asignar un ID a este usuario
        try:
            usuario = src\
                    .find("div", attrs={"class" : "post-layout"})\
                    .find("div", attrs={"class" : "user-details", "itemprop" : "author"})\
                    .find("a", href=True)
        except AttributeError:
            usuario = None

        # Agregando mas atributos de pregunta
        pregunta.comentarios = comentarios
        pregunta.respuestas = [i._id for i in respuestas] # Se agregaran por referencia por lo q se usa el id
        pregunta.usuario = usuario

        questions.append(pregunta)



driver.close()

with open("stackoverflow_scrapper/out/questions.json", "w+") as f:
    questionCollection = json.dumps(questions, cls=MyEncoder, indent=4)
    f.write(questionCollection)

with open("stackoverflow_scrapper/out/answers.json", "w+") as f:
    answerCollection = json.dumps(answers, cls=MyEncoder, indent=4)
    f.write(answerCollection)

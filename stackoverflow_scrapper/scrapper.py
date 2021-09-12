from selenium import webdriver
from bs4 import BeautifulSoup
from entidades.pregunta import Pregunta
from entidades.respuesta import Respuesta
from entidades.comentario import Comentario
from entidades.usuario import Usuario
from utils import collectComments
import json
from encoder import MyEncoder

# TODO 
#   Crear usuarios - Ya sea de forma aleatoria usando los nombres en los post's
#   o ingresando a cada perfil de usuario real (COSTOSO EN TIEMPO)
#
#   No se esta encontrando a los autores de las respuestas se ve en la salida que
#   el usuario ANON por default esta recibiendo todas las respuestas - Checkear
#   la secuencia de busqueda del usuario para cada respuesta

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
    # "mongodb",
    # "sql",
    # "django",
    # "flask",
]

questions = list()
answers = list()
users = list()

userDB = dict()

for i in tags:
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
        pregunta = Pregunta(titulo, fecha, desc, votes, tags, respuesta_aceptada)

        # REPUESTAS
        respuestas = list()
        # Se completa la lista que se agregara a la pregunta
        for ans in src.findAll("div", attrs={"class" : "answer"}):
            fecha_rta = ans.find("span", attrs={"class" : "relativetime"})
            descripcion_rta = ans.find("div", attrs={"class" : "s-prose js-post-body"})
            votes_rta = ans.find("div", attrs={"class" : "js-vote-count flex--item d-flex fd-column ai-center fc-black-500 fs-title"})
            try:
                usuario_rta = ans.find("div", attrs={"class" : "user-details"}).find("a", href=True)
            except AttributeError:
                usuario_rta = None

            # Se construye el objeto respuesta con atributos disponibles
            respuesta = Respuesta(fecha_rta, descripcion_rta, votes_rta, usuario=usuario_rta)

            comentarios_rta = list()
            lista_ans = ans.findAll("div", attrs={"class" : "comment-body js-comment-edit-hide"})
            collectComments(lista_ans, comentarios_rta)

            # Los comentarios se agregaran en forma embebida por lo que se agrega la instancia
            respuesta.comentarios = comentarios_rta

            usuario_rta_id = respuesta.useUserDB(userDB, respuesta.usuario, pregunta.titulo, pregunta._id)

            respuesta.usuario_id = usuario_rta_id

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

        # Agregar el usuario que hizo la pregunta a la DB
        usuario_id = pregunta.useUserDB(userDB, pregunta.usuario)

        pregunta.usuario_id = usuario_id

        questions.append(pregunta)

driver.close()

print(json.dumps(userDB, cls=MyEncoder, indent=4))

with open("stackoverflow_scrapper/out/questions.json", "w+") as f:
    questionCollection = json.dumps(questions, cls=MyEncoder, indent=4)
    f.write(questionCollection)

with open("stackoverflow_scrapper/out/answers.json", "w+") as f:
    answerCollection = json.dumps(answers, cls=MyEncoder, indent=4)
    f.write(answerCollection)

with open("stackoverflow_scrapper/out/users.json", "w+") as f:
    userCollection = json.dumps(users, cls=MyEncoder, indent=4)
    f.write(userCollection)

from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
from entidades.pregunta import Pregunta

# TODO 
#   Enlazar preguntas, respuestas, comentarios y usarios entre si
#       Quizas por ID que stackoverflow asigna (creo que lo hace) para
#       desprenderse del ObjectId() que debe ser generado en js o en su defecto
#       usar alguna libreria que lo simule


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

        pregunta = Pregunta(titulo, fecha, desc, votes, tags)

        print("\n==============================\n")
        for k in pregunta.__dict__:
            print(pregunta.__dict__[k])

driver.close()
            



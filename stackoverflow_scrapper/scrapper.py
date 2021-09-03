from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
from entidades.pregunta import Pregunta


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

    for div in soup.findAll("div", attrs={"class" : "question-summary"}):
        titulo = div.find("a", href=True, attrs={"class" : "question-hyperlink"})
        fecha = div.find("span", attrs={"class" : "relativetime"})
        desc = div.find("div", attrs={"class" : "excerpt"})

        pregunta = Pregunta(titulo, fecha, desc)
        json = pregunta.jsonize()

        print("\n==============================\n")
        for k in pregunta.__dict__:
            print(pregunta.__dict__[k])

driver.close()
            



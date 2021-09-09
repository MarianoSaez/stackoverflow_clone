from bs4 import BeautifulSoup

def check_existance(pe_list : list):
    # Checkear que no este vacia
    if len(pe_list) == 0:
        return False

    # Iterar para encontrar la aceptada
    for element in pe_list:
        if element.find("div", attrs={"class" : "js-accepted-answer-indicator"}):
            return True    
    return False
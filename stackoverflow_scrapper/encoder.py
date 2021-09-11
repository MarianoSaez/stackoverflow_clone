import json


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
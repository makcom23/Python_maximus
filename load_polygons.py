import json
import os

class LoadPolygons:
    def __init__(self):
        pass

    def load(self):
        path = os.path.join(os.path.dirname(__file__), 'polygon.json')
        with open(os.path.abspath(path)) as poly:
            load_poly = json.load(poly)
        return load_poly

    

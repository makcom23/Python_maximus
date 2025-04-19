import json
import os
import Polygon as plg

class LoadPolygons:
    def load():
        try:
            path = os.path.join(os.path.dirname(__file__), 'polygon.json')
            with open(os.path.abspath(path)) as poly:
                load_poly = json.load(poly)
            poligons=[]
            for p in load_poly:
                poligon = plg.Polygon()
                poligon.from_dict(p)
                poligons.append(poligon)
            return poligons
        except NameError:
            return []

    

import os
import json
import Polygon as plg

class SavePolygons:
    def __init__(self):
        pass
    
    def save(self, poligons):
        dict_poly = [p.to_dict() for p in poligons]
        path = os.path.join(os.path.dirname(__file__), 'polygon.json')
        with open(os.path.abspath(path), 'w', encoding='utf-8') as poly:
            json.dump(dict_poly, poly, indent=4)
        return
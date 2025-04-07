import Polygon as plg
import Visualizer_1 as vlz
import random as rnd 
import Explorer as expl
import sys
import os
import json
import load_polygons as lplg


# Основной рабочий процесс
sys.setrecursionlimit(50000)
height = 300
width = 300

# Проверка settings.json строки "load_polygons_from_file": True
path = os.path.join(os.path.dirname(__file__), 'settings.json')
with open(os.path.abspath(path)) as stts:
    settings = json.load(stts)
    if settings.get("load_polygons_from_file") is True:
        loader = lplg.LoadPolygons()
        polygons = loader.load()    


poligonNumber = range(rnd.randint(3, 20)) # количество полигонов
poligonNumber = range(20)
#poligonNumber = range(5)
visualizer = vlz.Visualizer_1()
poligons = []

#for _ in poligonNumber:
    #poligon = plg.Polygon(width,height)
    #poligon.createPoints()
    #poligons.append(poligon)

for i in poligonNumber:
    p = None
    check = True
    while check:
        check = False
        p = plg.Polygon(width,height)
        
        for polygon in poligons:
            check = check or polygon.isIntersectPolygon(p)
            
        #pass
    p.createPoints()
    p.name = i+1
    
    poligons.append(p)
        

explorer = expl.Explorer(poligons)


#print(counter)
visualizer.PrintPoligons(poligons, explorer)


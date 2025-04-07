import Polygon as plg
import Visualizer_1 as vlz
import random as rnd 
import Explorer as expl
import sys
import os
import json
import load_polygons as lplg
import Save_polygons as splg


# Основной рабочий процесс
sys.setrecursionlimit(50000)
height = 300
width = 300

# Проверка settings.json строки "load_polygons_from_file": True
path = os.path.join(os.path.dirname(__file__), 'settings.json')
with open(os.path.abspath(path)) as stts:
    settings = json.load(stts)
    if settings.get("load_polygons_from_file") == True:
        loader = lplg.LoadPolygons()
        polygons = loader.load() # теперь у нас есть полигоны из модуля load_polygons.py, но без поинтов. 
                                 # И им нужно добавить поинты и кому-то куда-то пристроить  
    else:
        print(f"THE FILE WITH POLYGONS IS UNAVAILABLE OR MISSING OUT. DON'T CRY BABY")


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

# Проверка settings.json строки "save_polygons_after_generation": True
path = os.path.join(os.path.dirname(__file__), 'settings.json')
with open(os.path.abspath(path)) as stts:
    settings=json.load(stts)
    if settings.get('save_polygons_after_generation') == True:
        saving = splg.SavePolygons()
        saving.save()
    else:
        print()


explorer = expl.Explorer(poligons)


#print(counter)
visualizer.PrintPoligons(poligons, explorer)


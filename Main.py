import Polygon as plg
import Visualizer_1 as vlz
import random as rnd 
import Explorer as expl
import sys
import load_polygons as lplg
import Save_polygons as splg
import CheckJson as chjs

# Основной рабочий процесс
sys.setrecursionlimit(50000)
height = 300
width = 300
poligons = []

#check.check_json_load() # Вызов проверки файла settings.json, нужно ли загружать полигоны из файла polygon.json, и не пустой ли файл
load_polygons_from_file = chjs.CheckJson.check_json_load()
if load_polygons_from_file:

    poligons = lplg.LoadPolygons.load()

    if not poligons or len(poligons)==0:
        print(f"Загружено 0 полигонов")
        sys.exit()

else:
    poligonNumber = range(rnd.randint(3, 20)) # количество полигонов
    poligonNumber = range(20)
    #poligons = []

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

    chjs.CheckJson.check_json_save(poligons) # Вызов проверки settings.json нужно ли записывать полигоны в файл polygon.json


explorer = expl.Explorer(poligons)


#print(counter)
visualizer = vlz.Visualizer_1()
visualizer.PrintPoligons(poligons, explorer)


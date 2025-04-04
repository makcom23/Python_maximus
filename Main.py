import Polygon as plg
import Visualizer_1 as vlz
import random as rnd 
import Explorer as expl
import sys

# Основной рабочий процесс
sys.setrecursionlimit(50000)
height = 300
width = 300

poligonNumber = range(rnd.randint(3, 50)) # количество полигонов
poligonNumber = range(35)
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
        
        #pass
    
explorer = expl.Explorer(poligons)

#print(counter)
visualizer.PrintPoligons(poligons, explorer)


import Polygon as plg
import Visualizer as vlz
import random as rnd 

# Основной рабочий процесс

height = 400
width = 400

poligonNumber = range(rnd.randint(3, 10))
visualizer = vlz.Visualizer()

poligons = []

for _ in poligonNumber:
    poligon = plg.Polygon(width,height)
    poligons.append(poligon)
    #if len(poligons)==0:
        #poligons.append(poligon)
    #else:
        #for item in poligons:
            # тут нужно проверить что они не пересекаются
            # если не пересекаются с существующими - то добавляем в коллекцию
            #pass
    


visualizer.PrintPoligons(poligons)


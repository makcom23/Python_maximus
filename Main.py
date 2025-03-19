import Polygon as plg
import Visualizer as vlz

# Основной рабочий процесс

height = 1000
width = 1000

poligonNumber = range(4)
visualizer = vlz.Visualizer()

poligons = []

for _ in poligonNumber:
    poligon = plg.Polygon(width,height)
    if len(poligons)==0:
        poligons.append(poligon)
    else:
        for item in poligons:
            # тут нужно проверить что они не пересекаются
            # если не пересекаются с существующими - то добавляем в коллекцию
            pass
    


visualizer.PrintPoligons(poligons)


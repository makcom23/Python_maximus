import Polygon as plg
import Visualizer as vlz

# Основной рабочий процесс

height = 1000
width = 1000

poligonNumber = range(4)

poligons = []

for _ in poligonNumber:
    poligons.append(plg.Polygon(width,height))

vis = vlz.Visualizer()
vis.PrintPoligons(poligons)


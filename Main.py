import Polygon as plg
import Visualizer_1 as vlz
import random as rnd 
import Explorer as expl


# Основной рабочий процесс

height = 500
width = 500

poligonNumber = range(rnd.randint(3, 50)) # количество полигонов

#poligonNumber = range(2)
visualizer = vlz.Visualizer_1()
counter = 0
poligons = []

for _ in poligonNumber:
    poligon = plg.Polygon(width,height)
    poligons.append(poligon)

check = True
while check:
    check = False
    for i in range(len(poligons)):  # проверяем полигоны на пересечения
        for j in range((i+1), len(poligons)):
            item1 = poligons[i]
            item2 = poligons[j]
            counter = counter + 1
            if not  item1.checkIntersectPolygon(item2):
                step = rnd.randint(-10, 10)
                j = 1 if step > 0  else -1
                # разводим сравниваемые полигоны друг от друга
                item1.center_x = item1.center_x+step * j
                item1.center_y = item1.center_y-step * j
                item2.center_x = item2.center_x-step * j
                item2.center_y = item2.center_y+step * j
                item1.updatePolygon()
                item2.updatePolygon()
                check = True
        
        #pass
    
explorer = expl.Explorer(poligons)

print(counter)
visualizer.PrintPoligons(poligons, explorer)


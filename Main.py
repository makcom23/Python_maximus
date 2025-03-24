import Polygon as plg
import Visualizer as vlz
import random as rnd 

# Основной рабочий процесс

height = 500
width = 500

poligonNumber = range(rnd.randint(3, 50)) # количество полигонов
visualizer = vlz.Visualizer()

poligons = []

for _ in poligonNumber:
    poligon = plg.Polygon(width,height)
    poligons.append(poligon)
    #if len(poligons)==0:
        #poligons.append(poligon)
    #else:
    check = True
    while check:
        check = False
        for i in range(len(poligons)):  # проверяем полигоны на пересечения
            for j in range((i+1), len(poligons)):
                item1 = poligons[i]
                item2 = poligons[j]
                if (item1.right < item2.left or
                    item1.left > item2.right or
                    item1.top < item2.bottom or
                    item1.bottom > item2.top):
                    continue

                else:  # разводим сравниваемые полигоны друг от друга
                    item1.center_x = item1.center_x-10
                    item1.center_y = item1.center_y-10
                    item2.center_x = item2.center_x+10
                    item2.center_y = item2.center_y+10
                    item1.updatePolygon()
                    item2.updatePolygon()
                    check = True
            
            #pass
    


visualizer.PrintPoligons(poligons)


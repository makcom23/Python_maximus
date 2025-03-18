import Polygon
import matplotlib.pyplot as plt

class Visualizer:
    def __init__(self):
    
        return
    def PrintPoligons(self, poligons):
        # тут в цикле все рисуем на одной плоскости
        # а пока так
        if len(poligons)>0:
            poligon = poligons[0]
            points=poligon.getPoints()
            print(points)
            x_coord, y_coord = zip(*points)
            plt.plot(x_coord, y_coord, marker="o", linestyle="-", color="b", label="Quadro")
            plt.show()


        return


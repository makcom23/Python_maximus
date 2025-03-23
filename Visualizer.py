import Polygon
import matplotlib.pyplot as plt
import random 

class Visualizer:
    def __init__(self):
    
        return
    def PrintPoligons(self, poligons):
        # тут в цикле все рисуем на одной плоскости
        # а пока так
        
        for i in range(len(poligons)):
            poligon = poligons[i]
            points=poligon.getPoints()
            x_coord, y_coord = zip(*points)
            plt.plot(x_coord, y_coord, marker="o", linestyle="-", color="b", label="Quadro")
            
        plt.show()


        return


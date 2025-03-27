import Polygon
import Visualizer
import matplotlib.pyplot as plt
import random 
import Explorer as expl

class Visualizer_1(Visualizer.Visualizer):
    def __init__(self):
    
        return
    def PrintPoligons(self, poligons, explorer):
        # тут в цикле все рисуем на одной плоскости 
        # а пока так
        steps = explorer.getPath()

        for i in range(len(poligons)):
            polygon = poligons[i]
            points=polygon.getPoints()
            x_coord, y_coord = zip(*points)
            plt.plot(x_coord, y_coord, marker=".", linestyle="-", label="Polygons")
            
        for step in steps:
            x_coord, y_coord = step
            plt.plot(x_coord, y_coord, marker=".", linestyle="-", color='r', label="explorer")
        plt.show()


        return


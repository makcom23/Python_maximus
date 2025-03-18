import matplotlib.pyplot as plt
import random
import math

class Figure:
    def __init__(self, global_x, global_y):
        self.height=random.randint(10, 100)
        self.width=random.randint(10, 100)
        self.counter=random.randint(3, 10)
        self.center_x=random.randint(self.width, global_x)
        self.center_y=random.randint(self.width, global_y)

    def getPoint(self):
        x_point = random.randint(self.center_x-self.width/2, self.center_x+self.width/2)
        y_point = random.randint(self.center_y-self.height/2, self.center_y+self.height/2)
        return x_point, y_point
    
    def getPoints(self):
        points = []
        for _ in range(self.counter):
            points.append(self.getPoint())
            return points



figure=Figure(1000,1000)

x_coord, y_coord=figure.getPoints()

plt.plot(x_coord, y_coord, marker="o", linestyle="-", color="b", label="Quadro")

plt.show()


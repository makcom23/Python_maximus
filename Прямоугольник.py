import matplotlib.pyplot as plt
import random
import math

class Figure:
    def __init__(self, lenght, width):
        self.lenght=lenght
        self.width=width

    def getPoint(self):
        x_point = [0, 0, self.lenght, self.lenght, 0]
        y_point = [0, self.width, self.width, 0, 0]
        return x_point, y_point


lenght=random.randint(-10, 10)
width=random.randint(-10, 10)

if lenght==0:
    lenght=lenght+1
else: 
    width=width+1 

rect=Figure(lenght,width)

x_coord, y_coord=rect.getPoint()

plt.plot(x_coord, y_coord, marker="o", linestyle="-", color="b", label="Quadro")

plt.show()
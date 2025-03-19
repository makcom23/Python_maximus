import random
import math

class Polygon:
    def __init__(self, global_x, global_y):
        self.height=random.randint(10, 100)
        self.width=random.randint(10, 100)
        self.counter=random.randint(3, 10)
        self.center_x=random.randint(self.width, global_x)
        self.center_y=random.randint(self.height, global_y)
        self.left = self.center_x - self.width // 2
        self.right = self.center_x + self.width // 2
        self.top = self.center_y + self.height // 2
        self.bottom = self.center_y - self.height // 2

    def getPoint(self):
        x_point = random.randint(int(self.center_x-self.width/2), int(self.center_x+self.width/2))
        y_point = random.randint(int(self.center_y-self.height/2), int(self.center_y+self.height/2))
        return x_point, y_point
    
    def getPoints(self):
        points = []
        for _ in range(self.counter):
            points.append(self.getPoint())

        # sort
        return self.sortArray(points)
    def sortArray(self, arr):
        
        return arr




import random
import math
import sys
import numpy as np

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
        for i in range(self.counter):
            #if i < self.counter // 2:
            points.append(self.getPoint())

        # sort
        return self.sortArray(points)
    def sortArray(self, points):
        if not points:
            return []

        sorted_points = [points[0]]
        remaining_points = points[1:]

        while remaining_points:
            last_point = sorted_points[-1]
            nearest_point = None
            nearest_distance = float('inf')

            for point in remaining_points:
                distance = self.distance(last_point, point)
                if distance < nearest_distance:
                    nearest_distance = distance
                    nearest_point = point

            sorted_points.append(nearest_point)
            remaining_points.remove(nearest_point)

        return sorted_points

    def distance(self,p1,p2):
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


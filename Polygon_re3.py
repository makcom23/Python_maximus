import matplotlib.pyplot as plt
import random
import math

class Polygon:
    def __init__(self, global_x, global_y):
        self.height=random.randint(10, 100)
        self.width=random.randint(10, 100)
        self.counter=random.randint(3, 50)
        #self.counter=4
        self.center_x=random.randint(self.width, global_x)
        self.center_y=random.randint(self.height, global_y)

    def getPoint(self):
        x_point = random.randint(int(self.center_x-self.width/2), int(self.center_x+self.width/2))
        y_point = random.randint(int(self.center_y-self.height/2), int(self.center_y+self.height/2))
        return x_point, y_point
    
    def getPoints(self):
        points = []
        for _ in range(self.counter):
            points.append(self.getPoint())
            #points.sort()
            #points.append(points[0])
        points=self.sortArray2(points)
        return points
        
    # sort ------------------------------------------------------------------------------------------
    def sortArray2(self, points):
        if not points:
            return []

        # 1. Находим центр всех точек
        center_x = sum(p[0] for p in points) / len(points) # Среднее значение X
        center_y = sum(p[1] for p in points) / len(points) # Среднее значение Y

        # 2. Функция для вычисления угла точки относительно центра
        def polar_angle(p):
            return math.atan2(p[1] - center_y, p[0] - center_x)

        # 3. Сортируем точки по углу наклона (по полярному углу)
        sorted_points = sorted(points, key=polar_angle)

        # 4. Добавляем первую точку в конец, чтобы контур замкнулся
        sorted_points.append(sorted_points[0])

        return sorted_points    
# End sort ------------------------------------------------------------------------------------------------

polygon=Polygon(1000,1000)
points=polygon.getPoints()


x_coord, y_coord = zip(*points)

plt.plot(x_coord, y_coord, marker="o", linestyle="-", color="b", label="Quadro")

plt.show()
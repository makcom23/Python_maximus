import matplotlib.pyplot as plt
import random
import math

class Polygon:
    def __init__(self, global_x, global_y):
        self.height=random.randint(10, 100)
        self.width=random.randint(10, 100)
        self.counter=random.randint(3, 20)
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
            points.append(points[0])
        return points
        
    #def sortArray(self, arr):
        #arr.append(self.getPoints())
        #for i in range(len(arr)):
         #   for j in range(len(arr)-1-i):
          #      if(arr[j]>arr[j+1]):
          #          arr[j], arr[j+1] = arr[j+1], arr[j]
        #return arr
# sort
    def sortArray(self, points):
        # Проверяем, если список точек пустой
        if not points:
            # Если список пустой, возвращаем пустой список
            return []

        # Инициализируем отсортированный список первой точкой из исходного списка
        sorted_points = [points[0]]
        # Создаем список оставшихся точек, исключая первую точку
        remaining_points = points[1:]

        # Пока в списке оставшихся точек есть элементы, продолжаем цикл
        while remaining_points:
            # Получаем последнюю добавленную точку из отсортированного списка
            last_point = sorted_points[-1]
            # Инициализируем ближайшую точку как None (пока не найдем)
            nearest_point = None
            # Инициализируем расстояние до ближайшей точки как бесконечность (чтобы первое найденное расстояние было меньше)
            nearest_distance = float('inf')

            # Проходим по каждой оставшейся точке
            for point in remaining_points:
                # Вычисляем расстояние между последней точкой и текущей точкой
                distance = self.distance(last_point, point)
                # Если вычисленное расстояние меньше текущего ближайшего расстояния
                if distance < nearest_distance:
                    # Обновляем ближайшее расстояние
                    nearest_distance = distance
                    # Обновляем ближайшую точку
                    nearest_point = point

            # Добавляем найденную ближайшую точку в отсортированный список
            sorted_points.append(nearest_point)
            # Удаляем добавленную точку из списка оставшихся точек
            remaining_points.remove(nearest_point)

        # Возвращаем отсортированный список точек
        return sorted_points

    def distance(self, p1, p2):
        # Вычисляем евклидово расстояние между двумя точками (p1 и p2)
        # p1[0] и p2[0] - координаты x точек
        # p1[1] и p2[1] - координаты y точек
        # math.sqrt - извлекает квадратный корень
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)    


polygon=Polygon(1000,1000)
points=polygon.getPoints()


x_coord, y_coord = zip(*points)

plt.plot(x_coord, y_coord, marker="o", linestyle="-", color="b", label="Quadro")

plt.show()
import random
import math
import sys
import numpy as np

class Polygon:
    def __init__(self, global_x, global_y):
        self.height=random.randint(10, 100)
        self.width=random.randint(10, 100)
        self.counter=random.randint(3, 10)
        #self.counter = 3
        self.center_x=random.randint(self.width, global_x)
        self.center_y=random.randint(self.height, global_y)
        self.left = self.center_x - self.width // 2
        self.right = self.center_x + self.width // 2
        self.top = self.center_y + self.height // 2
        self.bottom = self.center_y - self.height // 2
        self.points = []

    def getPoint(self):
        x_point = random.randint(int(self.center_x-self.width/2), int(self.center_x+self.width/2))
        y_point = random.randint(int(self.center_y-self.height/2), int(self.center_y+self.height/2))
        return x_point, y_point
    
    def getPoints(self):
        self.points = []
        for i in range(self.counter):
            #if i < self.counter // 2:
            self.points.append(self.getPoint())

        # sort
        self.points = self.sortArray(self.points)
        self.points = self.sortArray2(self.points)
        
        if self.isExistsIntersections(self.points) == False:
            self.points.append(self.points[0])
            return self.points
        else:
            return self.getPoints()
        



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
        #sorted_points.append(sorted_points[0])

        return sorted_points

    def distance(self,p1,p2):
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    
    def isExistsIntersections (self, points):

        def orientation(point1, point2, point3): # проверка ориентации векторов, возвращает знак поворота:
        # >0 — левый поворот # <0 — правый поворот  # ==0 — точки на одной прямой
            x1, y1 = point1 # распаковываем кортежи
            x2, y2 = point2
            x3, y3 = point3
            return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
            # т.е. имея 3 точки, мы формируем 2 вектора: A = point1 -> point2 = (x2 - x1, y2 - y1)
            #                                            B = point1 -> point3 = (x3 - x1, y3 - y1)
            # и далее производим векторное умножения для определения знака, указываещего на ориентацию
            # т.е.: A*B=(x2−x1)∗(y3−y1)−(y2−y1)∗(x3−x1) 
            # фактически мы получаем третий вектор, который лежит в плоскости z, 
            # и ориентирован в ту или иную сторону, но мы используем скалярную величину и ее знак 
            # для анализа направллености, так как работаем в 2х плоскостях
            # таким образом мы проделываем это для каждой точки вектора, 
            # а далее проверка, на какой полуплоскостии лежат точки,
            # если они лежат в разных полуплоскостях, то имеют разные знаки - пересекат другой вектор
            # если в одной полуплоскости - то имеею одинаковые знаки - не пересекают
        
        # создаем "векторы" из пар точек массива
        vectors=[]
        for i in range(len(points)):
            A = points[i]
            B = points[(i+1) % len(points)] 
            vectors.append([A, B])
            print('vectors: ', vectors)
        # теперь создаем список пар векторов которые не примыкают друг к другу 
        for i in range(len(vectors)): # цикл создания пар векторов для проверки пересечения
            A, B = vectors[i]
            
            for j in range(i+1, len(vectors)):
                C, D = vectors[j]
                if abs(i-j)==1 or (i==0 and j==len(vectors)-1): # проверка на непересечение
                    continue
                  
                # создаем ориентации
                o1 = orientation(A, B, C)
                o2 = orientation(A, B, D)
                o3 = orientation(C, D, A)
                o4 = orientation(C, D, B)

                # Если C и D по разные стороны от AB, и A и B по разные стороны от CD
                if o1 * o2 < 0 and o3 * o4 < 0:
                    return True
                    
                            
        return False


import random
import math
import sys
import numpy as np

class Polygon:
    def __init__(self, global_x, global_y):
        self.name = 0
        self.height=random.randint(10, 100)
        self.width=random.randint(10, 100)
        self.counter=random.randint(3, 10)
        self.counter = 3
        self.center_x=random.randint(self.width, global_x)
        self.center_y=random.randint(self.height, global_y)
        self.left = self.center_x - self.width // 2
        self.right = self.center_x + self.width // 2
        self.top = self.center_y + self.height // 2
        self.bottom = self.center_y - self.height // 2
        self.points = []

    def isIntersectPolygon (self, item):
        res = self.right < item.left or self.left > item.right or self.top < item.bottom or self.bottom > item.top
        return not res # если не пересекаются, то True, иначе False
    
    
    def updatePolygon(self): # передаются новые координаты центра полигонов - проверка на пересечение
        self.left = self.center_x - self.width // 2
        self.right = self.center_x + self.width // 2
        self.top = self.center_y + self.height // 2
        self.bottom = self.center_y - self.height // 2

    def getPoint(self):
        x_point = random.randint(int(self.center_x-self.width/2), int(self.center_x+self.width/2))
        y_point = random.randint(int(self.center_y-self.height/2), int(self.center_y+self.height/2))
        return x_point, y_point
    
    def createPoints(self):
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
            return self.createPoints() # WTF Ш0сь тут не те...!!!
        



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

        # создаем "векторы" из пар точек массива
        vectors=[]

        for i in range(len(points)):
            A = points[i]
            B = points[(i+1) % len(points)] 
            vectors.append([A, B])

        for edge in vectors:
            A = edge[0]
            B = edge[1]
            for i in range(len(vectors)):
                if vectors[i] == edge:
                    continue
                C = vectors[i][0]
                D = vectors[i][1]
                if self.isCrossed(A, B, C, D):
                    print("INTERSECTED")
                    return True
                            
        return False
    
    def isCrossed(self, current, next, A, B):
        C = current
        N = next
        x_C, y_C = C
        x_N, y_N = N
        x_A, y_A = A
        x_B, y_B = B
        #           
        #           . A
        #   C
        #   .
        #                       . N
        #
        #           . B
        # Создаем векторы
        CB = (x_B - x_C, y_B - y_C)
        CN = (x_N - x_C, y_N - y_C)
        CA = (x_A - x_C, y_A - y_C)
        BC = (x_C - x_B, y_C - y_B)
        BA = (x_A - x_B, y_A - y_B)
        BN = (x_N - x_B, y_N - y_B)
        AC = (x_C - x_A, y_C - y_A)
        AB = (x_B - x_A, y_B - y_A)
        AN = (x_N - x_A, y_N - y_A)
        NB = (x_B - x_N, y_B - y_N)
        NC = (x_C - x_N, y_C - y_N)
        NA = (x_A - x_N, y_A - y_N)

        # Вычисляем произведение векторов
        R1 = np.dot(CN, CB)
        R2 = np.dot(CN, CA)
        
        R3 = np.dot(BA, BN)
        R4 = np.dot(BA, BC)

        R5 = np.dot(AB, AC)
        R6 = np.dot(AB, AN)

        R7 = np.dot(NC, NB)
        R8 = np.dot(NC, NA)
        
        # Возвращаем ориентацию
        res = R1 * R2 <= 0 and R3 * R4 <= 0 and R5 * R6 <= 0 and R7 * R8 <= 0
        if(res):
            print("CROSSED")
        return res

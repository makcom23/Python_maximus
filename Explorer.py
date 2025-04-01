import Polygon as plg
import numpy as np
import math
import sys

class Explorer():
    def __init__(self, poligons):
        
        self.STEP = 5 # шаг
        self.poligons=poligons
        self.lefts =[]
        self.rights = []
        self.tops = []
        self.bottoms = []
        self.sumCenter_x=[]
        self.sumCenter_y=[]
        self.clearLog()

        for poligon in poligons: 
            self.log(f"{poligon.name} points: {poligon.points}")
            self.lefts.append(poligon.left)
            self.bottoms.append(poligon.bottom)
            self.tops.append(poligon.top)
            self.rights.append(poligon.right)
            self.sumCenter_x.append(poligon.center_x)
            self.sumCenter_y.append(poligon.center_y)
        min_x = min(self.lefts)
        min_y = min(self.bottoms)
        max_x = max(self.rights)
        max_y = max(self.tops)

        self.start = (min_x, min_y) # вычислить минимальное значение по X, Y
        self.finish = (max_x, max_y)# вычислить максимальное значение по X, Y
        self.current = self.start # текущая позиция
    
    def getPath(self):
        
        self.log(f"start: {self.start}, finish: {self.finish}")

        points = []
        while self.current != self.finish:
            
            next = self.nextStep()
            x,y = next
            # TODO: проверить на пересечение с полигонами
            next = self.checkNearestPolygon(next, self.poligons)
            self.log(f"C:{self.current}, N:{next}")
            self.current = next
            
            points.append((x,y))  
        return points
    
    def nextStep(self):
        next = self.getNextPosition()

        lengthToFinish = self.vector_length(next, self.finish)
        if(lengthToFinish < self.STEP):
            next = self.finish

        return next

    def checkNearestPolygon(self, nextpoint, poligons):
        max_attempts = 360
        attempt = 0

        while attempt < max_attempts:
            if not self.pointCrossPoly(poligons, nextpoint):  # проверяем все полигоны
                return nextpoint

            nextpoint = self.rotatePoint(nextpoint, attempt)
            attempt += 1

        print("Не удалось найти точку после 360 попыток")
        return nextpoint


    def getNextPosition(self): # вычисление следующей точки
        ## Получаем угол между текущей и конечной точками
        alfa = self.getRadAngle(self.current, self.finish)

        x1, y1 = self.current
        ## и вычисляем координаты следующей точки на основе этого угла
        x = x1 + self.STEP * math.cos(alfa)
        y = y1 + self.STEP * math.sin(alfa)
        # тут можно было бы  использовать y = y1 + self.STEP * math.sin(alfa), но это не результат не очень хороший точный
        return (int(x),int(y))

    


    def vector_length(self, point1, point2):
        """
        Вычисляет длину вектора между двумя точками.

        Args:
            point1: координаты первой точки.
            point2: координаты второй точки.
        Returns:
            Длина вектора.
        """
        def vector_length(x1, y1, x2, y2):
            point1 = np.array([x1, y1])
            point2 = np.array([x2, y2])
            vector = point2 - point1
            length = np.linalg.norm(vector)
            return length
        x1, y1 = point1
        x2, y2 = point2
        
        result= vector_length(x1, y1, x2, y2)
        return result

    def log(self, message):
        with open("log.txt", "a") as log_file:
            log_file.write(message + "\n")
    def clearLog(self):
        with open("log.txt", "w") as log_file:
            log_file.write("")
        
    def pointCrossPoly(self, poligons, nextPoint): # ищем пересечения отрезка(вектора) с потенциальными полигонами 
        C = self.current
        N = nextPoint
        res = False
        for polygon in poligons: 
            for i in range(len(polygon.points)-1):
                A = polygon.points [i]
                B = polygon.points [i+1]
                
                r_t = self.isCrossed(C, N, A, B)

                if r_t:
                    self.log(f"Crossed: C({C}) -> N({N}) пересекает ({polygon.name}): A({A}) -> B({B})")
                    return True

                res = res or r_t
            if polygon.points[0] != polygon.points[-1]:
                r_t1 = self.isCrossed(C, N, polygon.points[-1], polygon.points[0])
                if r_t1:
                    self.log(f"Crossed: C({C}) -> N({N}) пересекает ({polygon.name}): A({polygon.points[-1]}) -> B({polygon.points[0]})")
                    return True
                res = res or r_t1
                
        return res

    def rotatePoint(self, nextpoint, attempt):
        alfa = self.getRadAngle(self.current, nextpoint)
        alfa_grad = alfa * 180 / math.pi
        alfa_grad = alfa_grad + 1
        alfa_rad = alfa_grad * math.pi / 180

        x1, y1 = nextpoint
        ## и вычисляем координаты следующей точки на основе этого угла
        x = x1 + self.STEP * math.cos(alfa_grad)
        y = y1 + self.STEP * math.sin(alfa_grad)
        rotated_point = (int(x), int(y))

        self.log(f"Поворот: C:{self.current}, N:{nextpoint} => {rotated_point}, поворот на {attempt+1} : {int(alfa_grad)} градус")
        # тут можно было бы  использовать y = y1 + self.STEP * math.sin(alfa), но это не результат не очень хороший точный
        return rotated_point
    
    def getRadAngle(self, point_1, point_2):
        x1, y1 = point_1
        x2, y2 = point_2
        dx = x2 - x1
        dy = y2 - y1
        angle = math.atan2(dy, dx)
        return angle

    def rotatePoint2(self, nextpoint):
        currentpoint = self.current
        alfa = self.getRadAngle(currentpoint, nextpoint)
        alfa_grad = alfa * 180 / math.pi
        alfa_grad = alfa_grad + 1
        alfa_rad = alfa_grad * math.pi / 180

        current = np.array(currentpoint)
        nextpoint = np.array(nextpoint)

        vector = nextpoint - current

        cos_rot = np.cos(alfa_grad)
        sin_rot = np.sin(alfa_grad)

        # Матрица поворота
        rotation_matrix = np.array([
            [cos_rot, -sin_rot],
            [sin_rot,  cos_rot]
        ])

        # Поворачиваем вектор 
        rotated_vector = rotation_matrix @ vector
        # Находим новую позицию точки, добавляя повернутый вектор к центру
        rotated_point = current + rotated_vector
        # Возвращаем как кортеж
        rotated_point = tuple(rotated_point)

        self.log(f"next = {nextpoint} => {rotated_point}, поворот на {alfa_grad}")
        return rotated_point
    
    def multiplyVectors(self, vector_A, vector_B):
        x_a, y_a = vector_A
        x_b, y_b = vector_B
        return x_a * y_b - y_a * x_b
    
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
        R1 = self.multiplyVectors(CN, CB)
        R2 = self.multiplyVectors(CN, CA)
        
        R3 = self.multiplyVectors(BA, BN)
        R4 = self.multiplyVectors(BA, BC)

        R5 = self.multiplyVectors(AB, AC)
        R6 = self.multiplyVectors(AB, AN)

        R7 = self.multiplyVectors(NC, NB)
        R8 = self.multiplyVectors(NC, NA)
        
        # Возвращаем ориентацию
        res = R1 * R2 <= 0 and R3 * R4 <= 0 and R5 * R6 <= 0 and R7 * R8 <= 0
        if(res):
            print(f"CROSSED: {C} -> {N} пересекает {A} -> {B}")
        return res




poligons = []
poligon = plg.Polygon(300, 300)
poligon.createPoints()
poligon.name = 1
poligon.points = [(120, 65), (130, 58), (100, 96), (120, 65)]
poligons.append(poligon)

explorer = Explorer(poligons)
explorer.current = (100, 93)
explorer.checkNearestPolygon((103, 96), poligons)
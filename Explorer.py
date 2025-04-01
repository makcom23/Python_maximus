import Polygon as plg
import numpy as np
import math
import sys

class Explorer():
    def __init__(self, poligons):
        
        self.STEP = 2 # шаг
        self.poligons=poligons
        self.lefts =[]
        self.rights = []
        self.tops = []
        self.bottoms = []
        self.sumCenter_x=[]
        self.sumCenter_y=[]

        for poligon in poligons: 
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
        self.clearLog()
        self.log(f"start: {self.start}, finish: {self.finish}")

        points = []
        while self.current != self.finish:
            
            next = self.nextStep()
            x,y = next
            # TODO: проверить на пересечение с полигонами
            next = self.checkNearestPolygon(next, self.poligons)

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
        max_attempts = 360  # ограничение по количеству попыток (360 поворотов по 1 градусу)
        attempt = 0
        while attempt < max_attempts:
            crossedPolygons = []
            x, y = nextpoint
            res = True
            for poligon in poligons:
                if poligon.left <= x <= poligon.right and poligon.bottom <= y <= poligon.top:
                    res = False
                    crossedPolygons.append(poligon)

            if res or not self.pointCrossPoly(crossedPolygons, nextpoint):
                return nextpoint

            # поворот точки и увеличение счетчика попыток
            nextpoint = self.rotatePoint(nextpoint)
            attempt += 1

        # если не удалось найти точку, возвращаем текущую как есть (или можно выбросить исключение)
        return nextpoint

    def getNextPosition(self): # вычисление следующей точки
        ## Получаем угол между текущей и конечной точками
        alfa = self.getRadAngle(self.current, self.finish)

        x1, y1 = self.current
        ## и вычисляем координаты следующей точки на основе этого угла
        x = x1 + self.STEP * math.cos(alfa)
        y = y1 + self.STEP * math.sin(alfa)
        # тут можно было бы  использовать y = y1 + self.STEP * math.sin(alfa), но это не результат не очень хороший точный
        return (x,y)

    


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
        
    def pointCrossPoly(self, crossedPolygons, nextPoint): # ищем пересечения отрезка(вектора) с потенциальными полигонами 
        A = self.current
        B = nextPoint
        for polygon in crossedPolygons: 
            for i in range(len(polygon.points)-1):
                C = polygon.points [i]
                D = polygon.points [i+1]
                
                # создаем ориентации
                o1 = polygon.orientation(A, C, D) # используем функцию orientation из polygon.py
                # o1 = polygon.orientation(A, B, C) # old version
                o2 = polygon.orientation(B, C, D)
                # o2 = polygon.orientation(A, B, D) # old version
                # o3 = polygon.orientation(C, D, A) # old version
                # o4 = polygon.orientation(C, D, B) # old version

                # Если C и D по разные стороны от AB, и A и B по разные стороны от CD
                if o1 * o2 < 0: # and o3 * o4 < 0:
                    return True
        return False

    def rotatePoint(self, nextpoint):
        alfa = self.getRadAngle(self.current, nextpoint)
        alfa_grad = alfa * 180 / math.pi
        x1, y1 = nextpoint
        ## и вычисляем координаты следующей точки на основе этого угла
        x = x1 + self.STEP * math.cos(alfa_grad+1)
        y = y1 + self.STEP * math.sin(alfa_grad+1)
        nextpoint = (x, y)
        # тут можно было бы  использовать y = y1 + self.STEP * math.sin(alfa), но это не результат не очень хороший точный
        return (nextpoint)       
    
    def getRadAngle(self, point_1, point_2):
        def getRadAngle(x1, y1, x2, y2):
            dx = x2 - x1
            dy = y2 - y1
            angle = math.atan2(dy, dx) #* 180 / math.pi
            return angle
        x1, y1 = point_1
        x2, y2 = point_2
        return getRadAngle(x1, y1, x2, y2)

    def rotatePoint2(self, nextpoint):
        alfa = self.getRadAngle(self.current, nextpoint)
        alfa_grad = alfa * 180 / math.pi
        alfa_grad = alfa_grad + 1
        alfa_rad = alfa_grad * math.pi / 180

        current = np.array(self.current)
        nextpoint = np.array(nextpoint)

        vector = nextpoint - current
        
        R = np.array([[np.cos(alfa_rad),-np.sin(alfa_rad)],[np.sin(alfa_rad), np.cos(alfa_rad)]])

        rotated_vector = np.dot(R, vector)
        rotated_point = current + rotated_vector
        rotated_point = tuple(rotated_point)
        return rotated_point
    
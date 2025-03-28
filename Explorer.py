import Polygon as plg
import numpy as np
import math

class Explorer():
    def __init__(self, poligons):
        self.STEP = 10 # шаг
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
            next = self.getNextPosition()
            lengthToFinish = self.vector_length(self.current, self.finish)

            vectorLength = self.vector_length(self.start, self.finish)

            next = self.nextStep()
            x,y = next
            # TODO: проверить на пересечение с полигонами
            
            self.current = next
            
            points.append((x,y))  
        return points
    
    def nextStep(self):
        next = self.getNextPosition()

        lengthToFinish = self.vector_length(next, self.finish)
        if(lengthToFinish < self.STEP):
            next = self.finish

        return next

    
    def checkNearestPolygon(self, x, y, poligons):
        crossedPolygon =[]
        for poligon in poligons:
            if x >= poligon.left and x <= poligon.right and y >= poligon.bottom and y <= poligon.top:
                crossedPolygon.append(poligon)
                return True
            return False

    def getNextPosition(self):
        ## Получаем угол между текущей и конечной точками
        alfa = self.getRadAngle(self.current, self.finish)

        x1, y1 = self.current
        ## и вычисляем координаты следующей точки на основе этого угла
        x = x1 + self.STEP * math.cos(alfa)
        y = y1 + self.STEP * math.sin(alfa)
        # тут можно было бы  использовать y = y1 + self.STEP * math.sin(alfa), но это не результат не очень хороший точный
        #return (x,y)

        x2, y2 = self.finish
        # теперь скорректируем y, чтобы он вычислялся по уравнению прямой линии между двумя точками
        y_correcting = ((x*(y2-y1)-x2*(y2-y1))/(x2-x1))+(y2**2-y2*y1)/(y2-y1)

        msg = f"current: {self.current}, finish: {self.finish}, x: {x}, y: {y_correcting}"
        print(msg)
        self.log(msg)

        return (x, y_correcting)
    

    def getRadAngle(self, point_1, point_2):
        def getRadAngle(x1, y1, x2, y2):
            dx = x2 - x1
            dy = y2 - y1
            angle = math.atan2(dy, dx) #* 180 / math.pi
            return angle
        x1, y1 = point_1
        x2, y2 = point_2
        return getRadAngle(x1, y1, x2, y2)
    
    


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
        
        return vector_length(x1, y1, x2, y2)


    def log(self, message):
        with open("log.txt", "a") as log_file:
            log_file.write(message + "\n")
    def clearLog(self):
        with open("log.txt", "w") as log_file:
            log_file.write("")
        

            




        


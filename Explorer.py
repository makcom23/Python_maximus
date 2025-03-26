import Polygon as plg

class Explorer():
    def __init__(self, poligons):
        
        lefts =[]
        rights = []
        tops = []
        bottoms = []
        for poligon in poligons:
            lefts.append(poligon.left)
            bottoms.append(poligon.bottom)
            tops.append(poligon.top)
            rights.append(poligon.right)
        min_x = min(lefts)
        min_y = min(bottoms)
        max_x = max(rights)
        max_y = max(tops)   

        self.start = (min_x, min_y) # вычислить минимальное значение по X, Y
        self.finish = (max_x, max_y)# вычислить максимальное значение по X, Y
    
    def getPath (self):
        points = []
       
        points.append(self.start)
        points.append(self.finish)
        return points
        pass


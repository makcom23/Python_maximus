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
    
    def getPath(self):
        x1, y1 = self.start
        x2, y2 = self.finish
        points = []
        x=x1
        while x<x2:
            y = ((x*(y2-y1)-x2*(y2-y1))/(x2-x1))+(y2**2-y2*y1)/(y2-y1)
            points.append((x,y))
            isCrossSection2()
            x+=1
        
        return points
    
    def isCrossSection2(self, points, poligons):
        x1, y1 = points
        x2, y2 = self.finish
        for poligon in poligons:
            for point in poligon:
                x3, y3 = point
                o1 = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)

            



    #def straightLine(self, start, finish, x):
        #x1, y1 = self.start
        #x2, y2 = self.finish
        #return ((x*(y2-y1)-x2*(y2-y1))/(x2-x1))+(y2**2-y2*y1)/(y2-y1)
   

        


import Polygon as plg

class Explorer():
    def __init__(self, poligons):
        
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
    
    def getPath(self):
        x1, y1 = self.start
        x2, y2 = self.finish
        points = []
        x=x1
        y=y1
        while x<x2 and y<y2:
            y = ((x*(y2-y1)-x2*(y2-y1))/(x2-x1))+(y2**2-y2*y1)/(y2-y1)
            if self.checkNearestPolygon(x, y, self.poligons):
               x-=1 
               y-=1
            else: points.append((x,y))  
            x+=1
        
        return points
    
    def checkNearestPolygon(self, x, y, poligons):
        crossedPolygon =[]
        for poligon in poligons:
            if x >= poligon.left and x <= poligon.right and y >= poligon.bottom and y <= poligon.top:
                crossedPolygon.append(poligon)
                return True
            return False

    
    



        
        

            



    #def straightLine(self, start, finish, x):
        #x1, y1 = self.start
        #x2, y2 = self.finish
        #return ((x*(y2-y1)-x2*(y2-y1))/(x2-x1))+(y2**2-y2*y1)/(y2-y1)
   

        


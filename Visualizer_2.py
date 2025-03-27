import Visualizer
import pygame as pg
import Polygon
import sys
from pygame.locals import *
import Explorer as expl

class Visualizer_2(Visualizer.Visualizer):
    def __init__(self):
        self.start = (0,0)
        self.finish = (1000,1999)
        self.HEGHT = 600
        self.WIDTH = 800
        self.GREEN = (0,255,0)
        self.WHITE = (255,255,255)
        self.BLUE = (0,0,255)

        
    
    def PrintPoligons(self, poligons, explorer):
         # границы окна
         self.setBorders(poligons)
         
         pg.init()
         surf = pg.display.set_mode((self.WIDTH, self.HEGHT)) 
         surf.fill(self.WHITE)

         for poligon in poligons:
             points = poligon.getPoints()

             pg.draw.polygon(surf, self.GREEN, points)

         
         steps = explorer.getPath()
         for step in steps:
             pass
         run = True
         while run:
            for e in pg.event.get():
                if e.type == pg.QUIT:
                    run = False
            pg.display.update()
         pg.quit()


    def setBorders(self, poligons):
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

        self.start = (min_x - 5, min_y - 5) # вычислить минимальное значение по X, Y
        self.finish = (max_x + 5, max_y + 5)# вычислить максимальное значение по X, Y

        self.HEGHT = max_x + abs(min_x) + 100
        self.HEGHT = max_y + abs(min_y) + 100
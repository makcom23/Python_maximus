import Visualizer
import pygame, sys
from pygame.locals import *
import Explorer as expl

class Visualizer_2(Visualizer.Visualizer):
    def __init__(self):
        self.start = (0,0)
        self.finish = (1000,1999)
        
    
    def PrintPoligons(self, poligons, explorer):
         # границы окна
         self.setBorders(poligons)
         
         pygame.init()

         for i in range(len(poligons)):
             pass
         
         steps = explorer.getPath()
         for step in steps:
             pass
         
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

# Импорт модулей
import Visualizer
import pygame as pg
import Polygon
import sys
from pygame.locals import *
import Explorer as expl

class Visualizer_2(Visualizer.Visualizer):
    def __init__(self):
        self.start = (0, 0)
        self.finish = (1000, 1999)
        self.HEIGHT = 600
        self.WIDTH = 800
        self.GREEN = (0, 255, 0)
        self.WHITE = (255, 255, 255)
        self.BLUE = (0, 0, 255)
        self.global_scale = 1.0

    def transform_coordinates(self, x, y):
        x -= self.scene_start[0]
        y -= self.scene_start[1]
        x *= self.scale
        y *= self.scale
        x *= self.global_scale
        y *= self.global_scale
        x += self.padding
        y += self.padding
        return int(x), int(y)

    def PrintPoligons(self, polygons, explorer):
        min_point, max_point = self.getMinMaxSceneRect(polygons)
        self.setSceneBorders(min_point, max_point)  # Устанавливаем границы сцены
        self.calculate_scale()

        pg.init()
        self.screen = pg.display.set_mode((self.WIDTH, self.HEIGHT))
        self.screen.fill(self.WHITE)

        self.play_music()
        clock = pg.time.Clock()
        clock.tick(60)
        
        for polygon in polygons:
            if not polygon.points:
                polygon.points = polygon.getPoints()
            pixel_points = []
            for x, y in polygon.points:
                pixel_x, pixel_y = self.transform_coordinates(x, y)
                pixel_points.append((pixel_x, pixel_y))
            pg.draw.polygon(self.screen, self.GREEN, pixel_points)

        steps = explorer.getPath()
        for step in steps:
            x, y = step
            pixel_x, pixel_y = self.transform_coordinates(x, y)
            pg.draw.circle(self.screen, self.BLUE, (pixel_x, pixel_y), 3)

        run = True
        while run:
            for e in pg.event.get():
                if e.type == pg.QUIT:
                    run = False
            pg.display.update()
        pg.quit()

    def setSceneBorders(self, min_point, max_point):
        min_x, min_y = min_point
        max_x, max_y = max_point

        # Calculate scene dimensions
        scene_width = max_x - min_x
        scene_height = max_y - min_y

        # Add padding based on scene dimensions and global scale
        padding_x = scene_width * 0.1 * self.global_scale
        padding_y = scene_height * 0.1 * self.global_scale

        self.scene_start = (min_x - padding_x, min_y - padding_y)
        self.scene_finish = (max_x + padding_x, max_y + padding_y)

        # Update window dimensions based on padded scene and global scale
        self.WIDTH = int((self.scene_finish[0] - self.scene_start[0]) * self.global_scale)
        self.HEIGHT = int((self.scene_finish[1] - self.scene_start[1]) * self.global_scale)

    def calculate_scale(self):
        scene_width = self.scene_finish[0] - self.scene_start[0]
        scene_height = self.scene_finish[1] - self.scene_start[1]

        # Calculate scale based on padded scene dimensions and window size
        scale_x = (self.WIDTH - 20) / scene_width if scene_width != 0 else 1
        scale_y = (self.HEIGHT - 20) / scene_height if scene_height != 0 else 1

        self.scale = min(scale_x, scale_y)
        self.padding = 10  # Minimum padding

    def getMinMaxSceneRect(self, polygons):
        lefts = [p.left for p in polygons]
        rights = [p.right for p in polygons]
        tops = [p.top for p in polygons]
        bottoms = [p.bottom for p in polygons]

        min_x = min(lefts)
        min_y = min(bottoms)
        max_x = max(rights)
        max_y = max(tops)

        return (min_x, min_y), (max_x, max_y)
    
    def play_music(self):
        try:
            pg.mixer.init()
            pg.mixer.music.load("topot.wav")
            pg.mixer.music.set_volume(0.3)
            pg.mixer.music.play(-1)
        except Exception as e:
            print(f"Ошибка загрузки звука: {e}")
# Импорт модулей и зависимостей
import Visualizer  # Базовый визуализатор
import pygame as pg  # Библиотека для отрисовки
import Polygon  # Модуль, содержащий класс полигона
import sys
from pygame.locals import *  # Константы событий
import Explorer as expl  # Модуль для поиска пути

# Расширение базового визуализатора
class Visualizer_2(Visualizer.Visualizer):
    def __init__(self):
        # Инициализация стартовых и конечных координат области визуализации
        self.start = (0, 0)
        self.finish = (1000, 1999)

        # Размеры окна отрисовки (в пикселях)
        self.HEIGHT = 600
        self.WIDTH = 800

        # Цвета в RGB-формате
        self.GREEN = (0, 255, 0)   # цвет полигонов
        self.WHITE = (255, 255, 255)  # цвет фона
        self.BLUE = (0, 0, 255)    # запасной цвет

    # Главный метод отрисовки всех полигонов и пути
    def PrintPoligons(self, polygons, explorer):
        # Определяем минимальные и максимальные координаты всех полигонов
        min_point, max_point = self.getMinMaxPoints(polygons)

        # Устанавливаем границы и размеры окна на основе этих координат
        self.setBorders(min_point, max_point)

        # Сдвигаем все точки так, чтобы они помещались в окно
        self.shiftPolygonPoints(polygons, min_point, max_point)

        # Инициализация окна pygame
        pg.init()
        surf = pg.display.set_mode((self.WIDTH, self.HEIGHT)) 
        surf.fill(self.WHITE)  # Заливка фона

        # Загружаем и воспроизводим звук шагов в фоне (бесконечно)
        try:
            pg.mixer.init()
            pg.mixer.music.load("topot.wav")  # Локальный путь к звуковому файлу в корне проекта
            pg.mixer.music.set_volume(0.3)  # Уровень громкости (0.0 - 1.0)
            pg.mixer.music.play(-1)  # -1 означает бесконечное повторение
        except Exception as e:
            print(f"Ошибка загрузки звука: {e}")

        # Рисуем каждый полигон, если в нем достаточно точек
        for polygon in polygons:
            pg.draw.polygon(surf, self.GREEN, polygon.points)

        # Получаем маршрут из объекта-исследователя
        steps = explorer.getPath()
        for step in steps:
            pass  # здесь добавить отрисовку пути

        # Основной цикл pygame — поддерживает открытым окно
        run = True
        while run:
            for e in pg.event.get():
                if e.type == pg.QUIT:
                    run = False
            pg.display.update()  # Обновление экрана

        pg.quit()  # Завершение работы с pygame

    # Устанавливает границы области и размеры окна отображения
    def setBorders(self, min_point, max_point):
        min_x, min_y = min_point
        max_x, max_y = max_point

        # Устанавливаем координаты начала и конца области с отступом
        self.start = (min_x - 5, min_y - 5)
        self.finish = (max_x + 5, max_y + 5)

        # Обновляем размеры окна
        self.WIDTH = max_x - min_x + 100
        self.HEIGHT = max_y - min_y + 100

    # Сдвигает все точки полигонов, чтобы вписать их в окно визуализации с масштабированием
    def shiftPolygonPoints(self, polygons, min_point, max_point):
        min_x, min_y = min_point
        max_x, max_y = max_point

        # Вычисляем ширину и высоту всей сцены
        scene_width = max_x - min_x
        scene_height = max_y - min_y

        # Коэффициенты масштабирования по ширине и высоте
        scale_x = (self.WIDTH - 20) / scene_width if scene_width != 0 else 1
        scale_y = (self.HEIGHT - 20) / scene_height if scene_height != 0 else 1

        # Используем минимальный коэффициент, чтобы сохранить пропорции
        scale = min(scale_x, scale_y)

        for polygon in polygons:
            if not polygon.points:
                polygon.points = polygon.getPoints()
            for i in range(len(polygon.points)):
                x, y = polygon.points[i]
                # Сначала нормализуем координаты относительно минимальных значений
                x -= min_x
                y -= min_y
                # Масштабируем и добавляем отступ
                x = int(x * scale + 10)
                y = int(y * scale + 10)
                polygon.points[i] = (x, y)

    # Возвращает минимальные и максимальные координаты всех полигонов
    def getMinMaxPoints(self, polygons):
        lefts = [p.left for p in polygons]
        rights = [p.right for p in polygons]
        tops = [p.top for p in polygons]
        bottoms = [p.bottom for p in polygons]

        min_x = min(lefts)
        min_y = min(bottoms)
        max_x = max(rights)
        max_y = max(tops)

        return (min_x, min_y), (max_x, max_y)
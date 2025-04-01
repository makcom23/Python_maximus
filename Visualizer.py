from abc import ABC, abstractmethod

class Visualizer(ABC):
    @abstractmethod
    def PrintPoligons(self, poligons, explorer):
        pass
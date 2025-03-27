from abc import ABC, abstractmethod
import Explorer as expl

class Visualizer(ABC):
    @abstractmethod
    def PrintPoligons(self, poligons, explorer):
        pass
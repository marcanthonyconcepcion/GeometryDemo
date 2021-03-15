import abc
from typing import Union


class TwoDimensionalShape(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_area(self):
        pass

    @abc.abstractmethod
    def get_perimeter(self):
        pass

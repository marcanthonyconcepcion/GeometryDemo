import abc
from typing import Union


class TwoDimensionalShape(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_area(self) -> Union[int, float]:
        pass

    @abc.abstractmethod
    def get_perimeter(self) -> Union[int, float]:
        pass

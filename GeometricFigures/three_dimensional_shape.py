import abc
from typing import Union


class ThreeDimensionalShape(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_volume(self) -> Union[int, float]:
        pass

    @abc.abstractmethod
    def get_surface_area(self) -> Union[int, float]:
        pass

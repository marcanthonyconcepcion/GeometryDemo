import abc


class TwoDimensionalShape(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_area(self) -> int:
        pass

    @abc.abstractmethod
    def get_perimeter(self) -> int:
        pass

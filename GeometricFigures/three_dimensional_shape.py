import abc

class ThreeDimensionalShape(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_volume(self) -> int:
        pass

    @abc.abstractmethod
    def get_surface_area(self) -> int:
        pass

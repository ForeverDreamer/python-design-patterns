from .abs_factory import AbsFactory
from autos.nullcar import NullCar


class NullFactory(AbsFactory):

    def __init__(self):
        self._nullcar = None

    def create_auto(self):
        self._nullcar = NullCar()
        self._nullcar.name = 'Unknown'
        return self._nullcar

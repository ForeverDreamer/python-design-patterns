from .abs_factory import AbsFactory
from autos.fordfocus import FordFocus


class FordFactory(AbsFactory):

    def __init__(self):
        self._ford = None

    def create_auto(self):
        self._ford = FordFocus()
        self._ford.name = 'Ford Focus'
        return self._ford

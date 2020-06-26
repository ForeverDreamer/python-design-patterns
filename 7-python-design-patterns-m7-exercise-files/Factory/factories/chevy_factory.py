from .abs_factory import AbsFactory
from autos.chevyvolt import ChevyVolt


class ChevyFactory(AbsFactory):

    def __init__(self):
        self._chevy = None

    def create_auto(self):
        self._chevy = ChevyVolt()
        self._chevy.name = 'Chevy Volt'
        return self._chevy

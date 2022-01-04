from .abs_factory import AbsFactory
from autos.jeepsahara import JeepSahara


class JeepFactory(AbsFactory):

    def __init__(self):
        self._jeep = None

    def create_auto(self):
        self._jeep = JeepSahara()
        self._jeep.name = 'Jeep Sahara'
        return self._jeep

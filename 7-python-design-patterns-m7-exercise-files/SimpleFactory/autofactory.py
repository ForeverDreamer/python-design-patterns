from inspect import getmembers,  isclass, isabstract
import autos


class AutoFactory:

    def __init__(self):
        self._autos = {}  # Key = car model name, Value = class for the car
        self.load_autos()

    def load_autos(self):
        classes = getmembers(autos, lambda m: isclass(m) and not isabstract(m) and issubclass(m, autos.AbsAuto))
        for name, cls in classes:
            self._autos.update({name: cls})

    def create_instance(self, carname):
        if carname in self._autos:
            return self._autos[carname]()
        else:
            return autos.NullCar(carname)

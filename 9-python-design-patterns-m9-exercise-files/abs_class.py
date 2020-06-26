from abc import ABC, abstractmethod


class AbsClass(ABC):

    @staticmethod
    @abstractmethod
    def do_something():
        pass

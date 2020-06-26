from abc import ABC, abstractmethod


class AbsAuto(ABC):
    @staticmethod
    @abstractmethod
    def start():
        pass

    @staticmethod
    @abstractmethod
    def stop():
        pass

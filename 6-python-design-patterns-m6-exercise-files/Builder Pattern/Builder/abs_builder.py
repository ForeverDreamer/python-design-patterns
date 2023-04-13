from abc import ABC, abstractmethod
from computer import Computer


class AbsBuilder(ABC):

    def __init__(self):
        self._computer = None

    def get_computer(self):
        return self._computer

    @abstractmethod
    def get_case(self):
        pass

    @abstractmethod
    def build_mainboard(self):
        pass

    @abstractmethod
    def install_mainboard(self):
        pass

    @abstractmethod
    def install_hard_drive(self):
        pass

    @abstractmethod
    def install_video_card(self):
        pass

    def build_computer(self):
        self._computer = Computer()
        self.get_case()
        self.build_mainboard()
        self.install_mainboard()
        self.install_hard_drive()
        self.install_video_card()


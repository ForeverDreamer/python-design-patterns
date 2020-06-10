from abc import ABC, abstractmethod


class AbsOrderCommand(ABC):

    # def __init__(self, name, description):
    #     self._name = name
    #     self._description = description

    # @property
    # @abstractmethod
    # def name(self):
    #     raise NotImplementedError
    #
    # @property
    # @abstractmethod
    # def description(self):
    #     raise NotImplementedError
    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description
